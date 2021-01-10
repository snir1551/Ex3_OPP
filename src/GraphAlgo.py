import json
import math
from typing import List, Dict
from queue import PriorityQueue

from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.NodeData import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.__graph = graph

    def get_graph(self) -> GraphInterface:
        """
         @return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        # graph = DiGraph()
        # graph.add_node(0, (0, 2, 3))
        # graph.add_node(1, (3, 3, 4))
        # graph.add_node(2, (1, 4, 5))
        # graph.add_node(3, (2, 4, 5))
        # graph.add_node(4, (1, 4, 5))
        # graph.add_node(5, (5, 4, 5))
        # graph.add_node(6, (4, 4, 5))
        # graph.add_node(7, (0, 4, 5))
        # listX = []
        # listY = []
        # listZ = []
        # for n in self.__graph.get_all_v().values():
        #    n: NodeData
        #    x, y, z = n.get_pos()
        #    listX.append(x)
        #    listY.append(y)
        #    listZ.append(z)
        # plt.plot(listX,listY,listZ)
        # plt.scatter([0], [0])
        # plt.show()
        pass

    # =================== Shortest Path Function =================== #
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = []
        nodes: Dict[int, NodeData] = self.__graph.get_all_v()
        if nodes[id1] is None or nodes[id2] is None:
            return float('inf'), []
        if id1 is id2:
            list.append(nodes[id1])
            return list

        pv: Dict[int, NodeData] = self.dijkstra(nodes[id1])
        if nodes[id2].get_info().__eq__("WHITE"):
            return None

        list.append(nodes[id2])
        node: NodeData = pv.get(id2)

        while node is not None:
            list.append(nodes[node.get_key()])
            node = pv.get(node.get_key())
        list.reverse()
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
                        load_graph.add_edge(nodes["id"])
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
    graph.add_edge(1, 2, 30)
    graphAlgo = GraphAlgo(graph)
    graphAlgo.save_to_json("file1")
    graphAlgo.load_from_json("file1")
    graph = graphAlgo.get_graph()
    print(graph)

"""
 public HashMap<Integer, node_data> dijkstra(node_data node)
    {
        PriorityQueue<node_data> queue = new PriorityQueue<>(); // init PriorityQueue of node_info
        HashMap<Integer,node_data> mapPath = new HashMap<>(); //init HashMap of key: Integer , value: node_info
        for(node_data ni : graph.getV()) //We go through all the vertices
        {
            ni.setWeight(Double.MAX_VALUE); //set their tag to Max_Value
            ni.setInfo("WHITE"); //  set their info to WHITE
            mapPath.put(ni.getKey(),null); //put in our HashMap (father path)  - key: key of the node , value: null
            queue.add(ni); //add to our PriorityQueue the node
        }
        node.setWeight(0); //set tag of our start node to be 0
        queue.remove(node);//decreaseKey - we're removing the node and add him back
        queue.add(node);
        while(!queue.isEmpty()) // while our PriorityQueue is not empty
        {
            node_data n = queue.remove(); //remove our node that we're working on him
            for(edge_data edge : graph.getE(n.getKey())) //We go through all his neighbors
            {
                node_data ni = graph.getNode(edge.getDest());
                if(ni.getInfo().equals("WHITE")) //if he is WHITE We never went through it
                {
                    if(n.getWeight() < Double.MAX_VALUE) { //if tag smallest than MAX_VALUE
                        double t = n.getWeight() + edge.getWeight();
                        if (ni.getWeight() > t) { //if the tag of the neighbor bigger than new path tag so update the neighbor tag
                            ni.setWeight(t); //neighbor tag to be t
                            mapPath.put(ni.getKey(), n); //update the father path
                            queue.remove(ni);//decreaseKey - we're removing the node and add him back
                            queue.add(ni);
                        }
                    }
                }
            }
            n.setInfo("BLACK"); //we finish with the node set info to BLACK
        }
        return mapPath; //return the father path

    }




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
