from src.GraphInterface import GraphInterface
from typing import Dict
from src.node_data import NodeData
from src.edge_data import EdgeData


class DiGraph(GraphInterface):
    def __init__(self):
        self.__mc = 0
        self.__edge_size = 0
        self.__dictNode: Dict[int, NodeData] = dict()
        self.__dictEdgeOut: Dict[int, Dict[int, EdgeData]] = dict()
        self.__dictEdgeIn: Dict[int, Dict[int, EdgeData]] = dict()

    def v_size(self) -> int:
        return len(self.__dictNode)

    def e_size(self) -> int:
        return self.__edge_size

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.__dictNode and id2 in self.__dictNode and id2 not in self.__dictEdgeOut.get(id1):
            edge = EdgeData(id1, weight, id2)
            self.__dictEdgeOut.get(id1).update({id2: edge})
            self.__dictEdgeIn.get(id2).update({id1: edge})
            self.__mc += 1
            self.__edge_size += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.__dictNode:
            node = NodeData(node_id, pos)
            self.__dictNode.update({node_id: node})
            self.__mc += 1
            self.__dictEdgeOut.update({node_id: dict()})
            self.__dictEdgeIn.update({node_id: dict()})
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__dictNode:
            len1 = len(self.__dictEdgeOut.get(node_id))
            len2 = len(self.__dictEdgeIn.get(node_id))
            self.__mc += len1
            self.__edge_size -= len1
            self.__mc += len2
            self.__edge_size -= len2
            self.__dictEdgeOut.pop(node_id)
            self.__dictEdgeIn.pop(node_id)
            self.__mc += 1
            self.__dictNode.pop(node_id)
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.__dictNode and node_id2 in self.__dictNode and node_id2 in self.__dictEdgeOut.get(node_id1):
            self.__dictEdgeOut.get(node_id1).pop(node_id2)
            self.__dictEdgeIn.get(node_id2).pop(node_id1)
            self.__mc += 1
            self.__edge_size -= 1
            return True
        else:
            return False

    def get_all_v(self) -> dict:
        return self.__dictNode

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__dictEdgeIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__dictEdgeOut.get(id1)

    def __eq__(self, o: object) -> bool:
        return False

    def __str__(self):
        str_graph = ""
        for x in self.__dictNode:
            str_graph += self.__dictNode[x].__str__()
            for i in self.__dictEdgeIn.get(x):
                str_graph += self.__dictEdgeIn.get(x)[i].__str__()
            for i in self.__dictEdgeOut.get(x):
                str_graph += self.__dictEdgeOut.get(x)[i].__str__()
        return str_graph
        # return "Graph(Mc: %s , Edge Size: %s , Vertex size: %s  , Vertex : %s  , in: %s , out: %s)" % (
        # self.__mc, self.__edge_size, self.v_size(), self.dictNode, self.dictEdgeIn,self.dictEdgeOut)
