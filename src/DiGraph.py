from GraphInterface import GraphInterface
from typing import Dict
from node_data import NodeData
from edge_data import EdgeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.__mc = 0
        self.__edge_size = 0
        self.dictNode: Dict[int, NodeData] = dict()
        self.dictEdgeOut: Dict[int, Dict[int, EdgeData]] = dict()
        self.dictEdgeIn: Dict[int, Dict[int, EdgeData]] = dict()

    def v_size(self) -> int:
        return len(self.dictNode)

    def e_size(self) -> int:
        return self.__edge_size

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.dictNode and id2 in self.dictNode and id2 not in self.dictEdgeOut.get(id1):
            edge = EdgeData(id1, weight, id2)
            self.dictEdgeOut.get(id1).update({id2: edge})
            self.dictEdgeIn.get(id2).update({id1: edge})
            self.__mc += 1
            self.__edge_size += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.dictNode:
            node = NodeData(node_id, pos)
            self.dictNode.update({node_id: node})
            self.__mc += 1
            self.dictEdgeOut.update({node_id: dict()})
            self.dictEdgeIn.update({node_id: dict()})
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.dictNode:
            len1 = len(self.dictEdgeOut.get(node_id))
            len2 = len(self.dictEdgeIn.get(node_id))
            self.__mc += len1
            self.__edge_size -= len1
            self.__mc += len2
            self.__edge_size -= len2
            self.dictEdgeOut.pop(node_id)
            self.dictEdgeIn.pop(node_id)
            self.__mc += 1
            self.dictNode.pop(node_id)
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.dictNode and node_id2 in self.dictNode and node_id2 in self.dictEdgeOut.get(node_id1):
            self.dictEdgeOut.get(node_id1).pop(node_id2)
            self.dictEdgeIn.get(node_id2).pop(node_id1)
            self.__mc += 1
            self.__edge_size -= 1
            return True
        else:
            return False

    def get_all_v(self) -> dict:
        return self.dictNode

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.dictEdgeIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.dictEdgeOut.get(id1)

    def __eq__(self, o: object) -> bool:
        return False

    def __str__(self):
        str_graph = ""
        for x in self.dictNode:
            str_graph += self.dictNode[x].__str__()
            for i in self.dictEdgeIn.get(x):
                str_graph += self.dictEdgeIn.get(x)[i].__str__()
            for i in self.dictEdgeOut.get(x):
                str_graph += self.dictEdgeOut.get(x)[i].__str__()
        return str_graph
        # return "Graph(Mc: %s , Edge Size: %s , Vertex size: %s  , Vertex : %s  , in: %s , out: %s)" % (
        # self.__mc, self.__edge_size, self.v_size(), self.dictNode, self.dictEdgeIn,self.dictEdgeOut)
