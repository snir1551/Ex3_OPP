import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def first_graph():
    graph = DiGraph()
    for i in range(0, 8):
        graph.add_node(i, (i + 1, i, i + 2))
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 3, 10)
    graph.add_edge(3, 2, 10)
    graph.add_edge(3, 4, 10)
    graph.add_edge(4, 3, 10)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 4, 10)  # for check
    graph.add_edge(5, 6, 10)
    graph.add_edge(6, 5, 10)
    graph.add_edge(7, 6, 10)
    graph.add_edge(7, 0, 10)
    graph.add_edge(1, 7, 10)
    graph.add_edge(1, 6, 10)
    graph.add_edge(2, 5, 10)
    return graph


class MyTestCase(unittest.TestCase):

    def test_shortest_path(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(0,1,1)
        graph.add_edge(1,2,4)
        g_algo = GraphAlgo(graph)
        p =g_algo.shortest_path(0, 1)
        print(p)
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)




if __name__ == '__main__':
    unittest.main()
