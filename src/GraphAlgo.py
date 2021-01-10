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

    def get_graph(self) -> GraphInterface:
        """
         @return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    # # Tarjan's algorithm, recoursive version.
    # def __sconnect(self,v):
    #     global id,stack,lows,ids,onStack,path,path_lists
    #     stack.append(v)
    #     id+=1
    #     lows.update({v:id})
    #     ids.update({v: id})
    #     onStack.update({v:True})
    #
    #
    #     for u in self.__graph.all_out_edges_of_node(v).keys():
    #         if ids.get(u) == 0 : self.__sconnect(u)
    #         if onStack.get(u) is True : lows.update({v:min(lows.get(v),lows.get(u))})
    #
    #
    #     if ids.get(v) == lows.get(v):
    #         path=[]
    #         while stack:
    #             node = stack.pop()
    #             path.insert(0,node)
    #             onStack.update({node:False})
    #             lows.update({node:ids.get(v)})
    #             if node == v : break

    #     # Tarjan's algorithm, recoursive version.
    #
    # def __sconnect(self, v):
    #     global id, stack, lows, ids, onStack, path, path_lists
    #     stack.append(v)
    #     id += 1
    #     lows.update({v: id})
    #     ids.update({v: id})
    #     onStack.update({v: True})
    #
    #     for u in self.__graph.all_out_edges_of_node(v).keys():
    #         if ids.get(u) == 0: self.__sconnect(u)
    #         if onStack.get(u) is True: lows.update({v: min(lows.get(v), lows.get(u))})
    #
    #     if ids.get(v) == lows.get(v):
    #         path = []
    #         while stack:
    #             node = stack.pop()
    #             path.insert(0, node)
    #             onStack.update({node: False})
    #             lows.update({node: ids.get(v)})
    #             if node == v: break
    #
    # # Tarjan's algorithm, Iterative version.
    # def __dfs(self, v):
    #     global id, stack, lows, ids, onStack, path, path_lists
    #     work =[(v,0)]
    #     while work:
    #         v, i = work[-1]  # i is next successor to process.
    #         del work[-1]
    #         if i == 0:  # When first visiting a vertex:
    #             stack.append(v)
    #             id += 1
    #             lows.update({v: id})
    #             ids.update({v: id})
    #             onStack.update({v: True})
    #         recurse = False
    #         j=0
    #         for u in self.__graph.all_out_edges_of_node(v).keys():
    #             w=u
    #             if ids.get(w)==0:
    #                 work.append((v,j+1))
    #                 work.append((w,0))
    #                 recurse = True
    #                 j += 1
    #                 break
    #             elif onStack.get(w) is True :
    #                 j += 1
    #                 lows.update({v: min(lows.get(v), lows.get(w))})
    #         if recurse: continue
    #         if ids.get(v) == lows.get(v):
    #             path = []
    #             while stack:
    #                 node = stack.pop()
    #                 path.insert(0, node)
    #                 onStack.update({node: False})
    #                 lows.update({node: ids.get(v)})
    #                 if node == v: break
    #             path_lists.insert(0,path)
    #         if work:  # NEW: v was recursively visited.
    #             w = v
    #             v, _ = work[-1]
    #             lows.update({v: min(lows.get(v), lows.get(w))})

    def connected_component(self, id1: int) -> list:
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

    def connected_components(self) -> List[list]:
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

    def plot_graph(self) -> None:
        pass
        listX = []
        listY = []
        for n in self.__graph.get_all_v().values():
            if n.get_pos() is None:
                tup = (random.uniform(0, 50), random.uniform(0, 50))
                n.set_pos(tup)
                listX.append(n.get_pos()[0])
                listY.append(n.get_pos()[1])
            else:
                listX.append(n.get_pos()[0])
                listY.append(n.get_pos()[1])

        my_plot.scatter(listX, listY, color="black", s=50)

        for src in self.__graph.get_all_v().keys():
            for dest in self.__graph.all_out_edges_of_node(src).keys():
                print(src, dest)
                src1 = self.__graph.get_all_v().get(src)
                dest1 = self.__graph.get_all_v().get(dest)

                x1 = src1.get_pos()[0]
                y1 = src1.get_pos()[1]
                x2 = dest1.get_pos()[0]
                y2 = dest1.get_pos()[1]

                my_plot.arrow(x1, y1, (x2 - x1), (y2 - y1),
                          length_includes_head=True, width=0.000003, head_width=1.00015)
            # print number vertexs

        my_plot.show()

    # =================== Shortest Path Function =================== #
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = []
        nodes: Dict[int, NodeData] = self.__graph.get_all_v()
        if self.__graph is None or id1 not in self.__graph.get_all_v() or id2 not in self.__graph.get_all_v():
            return math.inf, []
        if id1 is id2:
            list.append(nodes[id1])
            return list

        pv: Dict[int, NodeData] = self.dijkstra(nodes[id1])
        if nodes[id2].get_info().__eq__("WHITE"):
            return math.inf, []

        list.append(id2)
        node: NodeData = pv.get(id2)

        while node is not None:
            list.insert(0, node.get_key())
            node = pv.get(node.get_key())

        return nodes[id2].get_weight(), list

    # =================== Encoder Function =================== #
    def encoder(self):
        dict_nodes = self.get_graph().get_all_v()
        dic = {"Edges": [],
               "Nodes": [NodeData.encoder(node) for node in list(dict_nodes.values())]}
        for node in dict_nodes.keys():
            for dest, w in self.__graph.all_out_edges_of_node(node).items():
                dic["Edges"].append({"src": node, "w": w, "dest": dest})
        return dic

    # =================== Save To Json Function =================== #
    def save_to_json(self, file_name: str) -> bool:

        try:
            with open(file_name, "w", encoding='utf-8') as file:
                json.dump(self.encoder(), fp=file, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    # =================== Load From Json Function =================== #
    def load_from_json(self, file_name: str) -> bool:
        load_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                dict_graph = json.load(file)
                for nodes in dict_graph["Nodes"]:
                    if "position" in nodes:
                        pos = nodes["position"]
                        load_graph.add_node(nodes["id"], pos)
                    else:
                        load_graph.add_node(nodes["id"])
                for edges in dict_graph["Edges"]:
                    load_graph.add_edge(edges["src"], edges["dest"], edges["w"])
        except IOError as e:
            print(e)
            return False
        self.__graph = load_graph
        return True

    # =================== Algorithm dijkstra =================== #
    def dijkstra(self, start_node: NodeData):
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
    graph = DiGraph()
    graph.add_node(1, (30, 20, 10))
    graph.add_node(2, (5, 5, 5))
    graph.add_node(3, (80, 70, 60))
    graph.add_node(4, (80, 70, 60))
    graph.add_edge(1, 2, 30)
    graph.add_edge(2, 3, 30)
    graph.add_edge(3, 1, 30)
    graph.add_edge(3, 4, 30)
    graphAlgo = GraphAlgo(graph)
    # graphAlgo.save_to_json("file1")
    # graphAlgo.load_from_json("file1")
    # graph = graphAlgo.get_graph()
    print(graphAlgo.connected_components())
    print(graphAlgo.connected_component(4))
    print(graphAlgo.connected_component(3))
    print(graphAlgo.connected_component(2))
    print(graphAlgo.connected_component(1))

"""




    /**
     * Tarjan's strongly connected components algorithm
     * finding the strongly connected components (SCCs) of a directed graph.
     * @return
     */
    private List<List<node_data>> tarjan() {
        List<List<node_data>> components = new ArrayList<>();

        Stack<node_data> stack = new Stack<>();
        int time = 0;
        for(node_data nodeData : graph.getV()) {
            nodeData.setTag(0); // lowlink
            nodeData.setInfo("white"); // set all to not-visited
        }

        for(node_data nodeData : graph.getV()) {
            if(nodeData.getInfo().equals("white")) { // not visited
                dfs(nodeData, time, stack, components);
            }
        }

        return components;
    }

    /**
     * DFS is an algorithm for traversing or searching tree or graph data structures.
     * The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
     * and explores as far as possible along each branch before backtracking.
     * @param nodeData
     * @param time
     * @param stack
     * @param components
     */
    private void dfs(node_data nodeData, int time, Stack<node_data> stack, List<List<node_data>> components ) {
        nodeData.setTag(time);
        time++;
        nodeData.setInfo("black");
        stack.add(nodeData);
        boolean componentRoot = true;

        for(edge_data edge: graph.getE(nodeData.getKey())) {
            node_data neighbor = graph.getNode(edge.getDest());

            if(neighbor.getInfo().equals("white")) { // not visited
                dfs(neighbor, time, stack, components);
            }
            if(nodeData.getTag() > neighbor.getTag()) {
                nodeData.setTag(neighbor.getTag());
                componentRoot = false;
            }
        }

        if(componentRoot) {
            List<node_data> component = new ArrayList<>();

            while(true) {
                node_data nd = stack.pop();
                component.add(nd);
                nd.setTag(Integer.MAX_VALUE);

                if(nd.getKey() == nodeData.getKey()) {
                    break;
                }
            }

            components.add(component);
        }
    }
"""
