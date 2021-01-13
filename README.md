# Ex3

# Description
At this project we used with python <br />
We created classes that represent directed weighted graph and used some algorithms <br />
In the next step we were suppose to compare our implementation performance vs NetworkX and Java implementation <br />



* [About the project](#p1)
* [Compare with Other:](#p2)






<a name="p1"></a>
## About the project:
* At this project have 3 interface : GraphAlgoInterface.py ,GraphInterface.py , NodeDataInterface.py <br />

  DiGraph.py implements GraphInterface interface  <br />
  GraphAlgo.py implements GraphAlgoInterface interface <br />
  NodeData.py implements NodeDataInterface interface <br />

* we created Directed Weighted Graph but in python instead of java, and add a new method(etc strong connected components) <br />
* we added the ability to plot graph and saving the graph to a json format and loading a graph from a json format. <br />
* Comparing the graph performance vs NetworkX library and The java implementation from Ex2. <br />



## Example to a graph with random positions:


<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/kMRyY7vg/Random.jpg' border='0' alt='Random'/></a>



## Example to a graph with given positions:
**A5 graph**
    
    

<a href='https://postimg.cc/4K6ygnXm' target='_blank'><img src='https://i.postimg.cc/8C36Lr3B/A5.png' border='0' alt='A5'/></a>





<a name="p2"></a>
## Compare with Other:

At this project we comparing the graph performance vs NetworkX library and The java implementation from Ex2.
the results:

# DiGraph class summary
| Method  | Description  |
| :------ |:-------------| 
| v_size()| Returns the number of vertices in this graph |
| e_size()| Returns the number of edges in this graph |
| get_all_v()| return a dictionary of all the nodes in the Graph|
| all_in_edges_of_node(int)| return a dictionary of all the nodes connected to (into) node_id|
| all_out_edges_of_node(int)| return a dictionary of all the nodes connected from node_id|
| get_mc(int)| Returns the current version of this graph,on every change in the graph state - the MC should be increased|
| add_edge(int id1,int id2,float weight)|  Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing)|
|add_node(int, tuple)| Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added|
| remove_node(int)|gets the number of edges in the graph.|
| remove_edge(int id1,int id2)| Removes an edge from the graph.node_id1: The start node of the edge.node_id2: The end node of the edge.return: True if the edge was removed successfully, False o.w..Note: If such an edge does not exists the function will do nothing|
|.repr()| Returns a string representation of the graph|


# GraphAlgo class summary
| Method  | Description  |
| :------ |:-------------| 
| get_graph | return: the directed graph on which the algorithm works on|
| load_from_json(str file_name)| loads a graph from a json file.|
| save_to_json(str file_name)| save the graph in JSON format to a file|
| shortest_path(int src, int dst)| returns the shortest path from node src to node dst using Dijkstra's Algorithm|
| connected_component(int key)| finds the Strongly Connected Component(SCC) that node key is a part of |
| connected_components()|Finds all the Strongly Connected Component(SCC) in the graph |
| plot_graph()| Plots the graph.If the nodes have a position, the nodes will be placed there.Otherwise, they will be placed in a random but elegant manner|
| __encoder()| This method help to building a json object in our format.note: use in the save function |
| __dijkstra(NodeData)| private function, part of the shortest_path function |



