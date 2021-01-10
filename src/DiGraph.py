from src.GraphInterface import GraphInterface
from typing import Dict
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.__mc: int = 0
        self.__edge_size: int = 0
        self.__dictNode: Dict[int, NodeData] = dict()
        self.__dictEdgeOut: Dict[int, Dict[int, float]] = dict()
        self.__dictEdgeIn: Dict[int, Dict[int, float]] = dict()

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.__dictNode)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edge_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 in self.__dictNode and id2 in self.__dictNode and id1 is not id2 and weight >= 0:
            if id2 not in self.__dictEdgeOut.get(id1):
                self.__edge_size += 1
            self.__dictEdgeOut.get(id1).update({id2: weight})
            self.__dictEdgeIn.get(id2).update({id1: weight})
            self.__update_in_out_size(id1, id2)

            self.__mc += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.__dictNode:
            node: NodeData = NodeData(node_id, pos)
            self.__dictNode.update({node_id: node})
            self.__mc += 1
            self.__dictEdgeOut.update({node_id: dict()})
            self.__dictEdgeIn.update({node_id: dict()})
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.__dictNode:
            if self.__dictEdgeOut.get(node_id) is not None:
                list_keys = []
                for i in self.__dictEdgeOut.get(node_id).keys():
                    list_keys.append(i)
                for i in list_keys:
                    self.remove_edge(node_id, i)

            if self.__dictEdgeIn.get(node_id) is not None:
                list_keys = []
                for i in self.__dictEdgeIn.get(node_id).keys():
                    list_keys.append(i)
                for i in list_keys:
                    self.remove_edge(i, node_id)

            self.__dictEdgeOut.pop(node_id)
            self.__dictEdgeIn.pop(node_id)
            self.__dictNode.pop(node_id)
            self.__mc += 1
            return True

        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.__dictNode and node_id2 in self.__dictNode and node_id2 in self.__dictEdgeOut.get(node_id1):
            self.__dictEdgeOut.get(node_id1).pop(node_id2)
            self.__dictEdgeIn.get(node_id2).pop(node_id1)
            self.__update_in_out_size(node_id1, node_id2)
            self.__mc += 1
            self.__edge_size -= 1
            return True
        else:
            return False

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
         """
        return self.__dictNode

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        return self.__dictEdgeIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.__dictEdgeOut.get(id1)

    def get_node(self, key: int) -> NodeData:
        return self.__dictNode[key]

    def __update_in_out_size(self, node1, node2):
        self.__dictNode[node1].set_counter_edges_out(len(self.__dictEdgeOut[node1].keys()))
        self.__dictNode[node2].set_counter_edges_in(len(self.__dictEdgeIn[node2].keys()))

    def __eq__(self, o: object) -> bool:
        """

        """
        return False

    def __repr__(self):
        """

        """
        str_graph = "Graph: |V|={} , |E|={}".format(self.v_size(), self.e_size())
        return str_graph
