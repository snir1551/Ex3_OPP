from typing import List, Dict
from queue import PriorityQueue
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.node_data import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface):
        self.__graph = graph

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def load_from_json(self, file_name: str) -> bool:
        pass

    def dijkstra(self, node: NodeData) -> Dict[int, NodeData]:
        queue1 = PriorityQueue()
        map_path = Dict[int, NodeData]
        for ni in self.__graph.get_all_v().values():
            NodeData.set_weight(ni, float('inf'))
            NodeData.set_info(ni, "WHITE")
            map_path.update({NodeData.get_key(ni): None})
            queue1.put(ni)

        NodeData.set_weight(node, 0)
        queue1.get()


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
