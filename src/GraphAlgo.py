import json
import math
from typing import List, Dict
from queue import PriorityQueue

from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.NodeData import NodeData
import matplotlib.pyplot as my_plot
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.__graph = graph

    # =================== get graph Function =================== #
    def get_graph(self) -> GraphInterface:
        """
         @return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    # =================== Load From Json Function =================== #
    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        load_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                dict_graph = json.load(file)
                for nodes in dict_graph["Nodes"]:
                    try:
                        pos = nodes["pos"]
                        x, y, z = str.split(pos, ",")
                        x = float(x)
                        y = float(y)
                        z = float(z)
                        load_graph.add_node(nodes["id"], (x, y, z))
                    except Exception:
                        load_graph.add_node(nodes["id"])
                for edges in dict_graph["Edges"]:
                    load_graph.add_edge(edges["src"], edges["dest"], edges["w"])
        except IOError as e:
            print(e)
            return False
        self.__graph = load_graph
        return True

    # =================== Save To Json Function =================== #
    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w", encoding='utf-8') as file:
                json.dump(self.__encoder(), fp=file, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    # =================== Shortest Path Function =================== #
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        list = []
        nodes: Dict[int, NodeData] = self.__graph.get_all_v()
        if self.__graph is None or id1 not in self.__graph.get_all_v() or id2 not in self.__graph.get_all_v():
            return math.inf, []
        if id1 is id2:
            list.append(nodes[id1].get_key())
            return 0, list

        pv: Dict[int, NodeData] = self.__dijkstra(nodes[id1])
        if nodes[id2].get_info().__eq__("WHITE"):
            return math.inf, []

        list.append(id2)
        node: NodeData = pv.get(id2)

        while node is not None:
            list.insert(0, node.get_key())
            node = pv.get(node.get_key())

        return nodes[id2].get_weight(), list

    # =================== Connected Component Function =================== #
    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if self.__graph is None or id1 not in self.__graph.get_all_v():
            return []
        id = 0
        stack = []
        lows = dict()
        ids = dict()
        onStack = dict()
        path = []

        for i in self.__graph.get_all_v().keys():
            lows.update({i: 0})
            ids.update({i: 0})
            onStack.update({i: False})

        v = id1
        work = [(v, 0)]
        while work:
            v, i = work[-1]  # i is next successor to process.
            del work[-1]
            if i == 0:  # When first visiting a vertex:
                stack.append(v)
                id += 1
                lows.update({v: id})
                ids.update({v: id})
                onStack.update({v: True})
            recurse = False
            j = 0
            for u in self.__graph.all_out_edges_of_node(v).keys():
                w = u
                if ids.get(w) == 0:
                    work.append((v, j + 1))
                    work.append((w, 0))
                    recurse = True
                    j += 1
                    break
                elif onStack.get(w) is True:
                    j += 1
                    lows.update({v: min(lows.get(v), lows.get(w))})
            if recurse: continue
            if ids.get(v) == lows.get(v):
                path = []
                while stack:
                    node = stack.pop()
                    path.insert(0, node)
                    onStack.update({node: False})
                    lows.update({node: ids.get(v)})
                    if node == v: break
            if work:  # NEW: v was recursively visited.
                w = v
                v, _ = work[-1]
                lows.update({v: min(lows.get(v), lows.get(w))})

        return path

    # =================== Connected Component Function =================== #
    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        if self.__graph is None:
            return []

        id = 0
        stack = []
        lows = dict()
        ids = dict()
        onStack = dict()
        path = []
        path_lists = []

        for i in self.__graph.get_all_v().keys():
            lows.update({i: 0})
            ids.update({i: 0})
            onStack.update({i: False})

        for x in self.__graph.get_all_v().keys():
            if ids.get(x) == 0:
                v = x
                work = [(v, 0)]
                while work:
                    v, i = work[-1]  # i is next successor to process.
                    del work[-1]
                    if i == 0:  # When first visiting a vertex:
                        stack.append(v)
                        id += 1
                        lows.update({v: id})
                        ids.update({v: id})
                        onStack.update({v: True})
                    recurse = False
                    j = 0
                    for u in self.__graph.all_out_edges_of_node(v).keys():
                        w = u
                        if ids.get(w) == 0:
                            work.append((v, j + 1))
                            work.append((w, 0))
                            recurse = True
                            j += 1
                            break
                        elif onStack.get(w) is True:
                            j += 1
                            lows.update({v: min(lows.get(v), lows.get(w))})
                    if recurse: continue
                    if ids.get(v) == lows.get(v):
                        path = []
                        while stack:
                            node = stack.pop()
                            path.insert(0, node)
                            onStack.update({node: False})
                            lows.update({node: ids.get(v)})
                            if node == v: break
                        path_lists.insert(0, path)
                    if work:  # NEW: v was recursively visited.
                        w = v
                        v, _ = work[-1]
                        lows.update({v: min(lows.get(v), lows.get(w))})

        return path_lists

    # =================== Plot Graph =================== #
    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        listX = []
        listY = []
        my_nodes = []
        # img = my_plot.imread("../backgroundGame.png")
        # fig, ax = my_plot.subplots()
        for k, n in self.__graph.get_all_v().items():
            if n.get_pos() is None:
                tup = (random.uniform(35.18, 35.2), random.uniform(32.1, 32.2))
                n.set_pos(tup)
                listX.append(n.get_pos()[0])
                listY.append(n.get_pos()[1])
            else:
                listX.append(n.get_pos()[0])
                listY.append(n.get_pos()[1])
            my_nodes.append(k)
        _, ax = my_plot.subplots()
        for pos, val in enumerate(my_nodes):
            ax.annotate(my_nodes[pos], (listX[pos], listY[pos]))
        for src in self.__graph.get_all_v().keys():
            for dest, w in self.__graph.all_out_edges_of_node(src).items():
                src1 = self.__graph.get_all_v().get(src)
                dest1 = self.__graph.get_all_v().get(dest)
                x1 = src1.get_pos()[0]
                y1 = src1.get_pos()[1]
                x2 = dest1.get_pos()[0]
                y2 = dest1.get_pos()[1]
                my_plot.arrow(x1, y1, (x2 - x1), (y2 - y1), length_includes_head=True,
                              width=0.000003, head_width=0.00015, color='green', zorder=1)
        my_plot.scatter(listX, listY, color="red", s=50, zorder=2)
        my_plot.title("Our Graph")
        my_plot.show()

    # =================== Encoder Function =================== #
    def __encoder(self):
        """
        This method help to building a json object in our format.
        note: use in the save function.
        """
        dict_nodes = self.get_graph().get_all_v()
        dic = {"Edges": [],
               "Nodes": [NodeData.encoder(node) for node in list(dict_nodes.values())]}
        for node in dict_nodes.keys():
            for dest, w in self.__graph.all_out_edges_of_node(node).items():
                dic["Edges"].append({"src": node, "w": w, "dest": dest})
        return dic

    # =================== Algorithm Dijkstra =================== #
    def __dijkstra(self, start_node: NodeData):
        """
        This method marks on each vertex the distance to the source vertex and
        @return path - Dict[int, NodeData] that the shortest path from start_node
        """
        nodes = self.__graph.get_all_v()
        q = PriorityQueue()
        path: Dict[int, NodeData] = dict()
        q.put(start_node)
        for n in nodes.values():
            node: NodeData = n
            node.set_weight(math.inf)
            node.set_info("WHITE")
            path[n.get_key()] = None
        start_node.set_weight(0)
        while not q.empty():
            v: NodeData = q.get()
            for k, w in self.__graph.all_out_edges_of_node(v.get_key()).items():
                n: NodeData = nodes[k]
                weight = v.get_weight() + w
                if weight < n.get_weight():
                    q.put(n)
                    n.set_weight(weight)
                    path[n.get_key()] = v
            v.set_info("BLACK")
        return path



if __name__ == '__main__':
    pass
