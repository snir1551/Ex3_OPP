import math
import unittest

from src import NodeData
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.GraphAlgo import GraphAlgo
from random import seed, randrange, random

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


def second_graph():
    """
                          5
                        /  \
                  (9) /     \(6)
                    /        \
                  / (2)  (11) \
                6-------3------4
                |     /  \     |
                |    /    \    |
           (14) |   /      \   | (15)
                |  / (9)(10 \  |
                | /          \ |
                1--------------2
                       (7)

           """
    graph_second = DiGraph()
    graph_second.add_node(1)
    graph_second.add_node(2)
    graph_second.add_node(3)
    graph_second.add_node(4)
    graph_second.add_node(5)
    graph_second.add_node(6)
    graph_second.add_edge(1, 2, 7)
    graph_second.add_edge(2, 1, 7)
    graph_second.add_edge(1, 3, 9)
    graph_second.add_edge(3, 1, 9)
    graph_second.add_edge(1, 6, 14)
    graph_second.add_edge(6, 1, 14)
    graph_second.add_edge(2, 4, 15)
    graph_second.add_edge(4, 2, 15)
    graph_second.add_edge(2, 3, 10)
    graph_second.add_edge(3, 2, 10)
    graph_second.add_edge(3, 4, 11)
    graph_second.add_edge(4, 3, 11)
    graph_second.add_edge(3, 6, 2)
    graph_second.add_edge(6, 3, 2)
    graph_second.add_edge(4, 5, 6)
    graph_second.add_edge(5, 4, 6)
    graph_second.add_edge(6, 5, 9)
    graph_second.add_edge(5, 6, 9)
    return graph_second


def three_graph():
    """
                 5

           (2)    (11)
        6-------3------4
        |     /  \     |
        |    /    \    |
   (14) |   /      \   | (15)
        |  / (9)(10 \  |
        | /          \ |
        1--------------2
            (7)

   """
    graph3 = DiGraph()
    graph3.add_node(1)
    graph3.add_node(2)
    graph3.add_node(3)
    graph3.add_node(4)
    graph3.add_node(5)
    graph3.add_node(6)
    graph3.add_edge(1, 2, 7)
    graph3.add_edge(2, 1, 7)
    graph3.add_edge(1, 3, 9)
    graph3.add_edge(3, 1, 9)
    graph3.add_edge(1, 6, 14)
    graph3.add_edge(6, 1, 14)
    graph3.add_edge(2, 4, 15)
    graph3.add_edge(4, 2, 15)
    graph3.add_edge(2, 3, 10)
    graph3.add_edge(3, 2, 10)
    graph3.add_edge(3, 4, 11)
    graph3.add_edge(4, 3, 11)
    graph3.add_edge(3, 6, 2)
    graph3.add_edge(6, 3, 2)
    return graph3


class MyTestCase(unittest.TestCase):

    def graph_creator(self, num_of_nodes: int, num_of_ed: int):
        seed(1)
        graph = DiGraph()
        i = 0
        while i < num_of_nodes:
            graph.add_node(i)
            i = i + 1
        while graph.e_size() < num_of_ed:
            rnd = randrange(0, num_of_nodes)
            rnd2 = randrange(0, num_of_nodes)
            rnd3 = random()
            graph.add_edge(rnd, rnd2, rnd3 * 100)
        return graph

    def test_plot_graph(self):
        graph = self.graph_creator(10, 20)
        NodeData.set_pos(graph.get_all_v().get(2), 2, 5)
        NodeData.set_pos(graph.get_all_v().get(8), 8, 7.41)
        NodeData.set_pos(graph.get_all_v().get(1), 10, 10)
        NodeData.set_pos(graph.get_all_v().get(8), 14, 6)

        algo_g = GraphAlgo(graph)
        algo_g.load_from_json("../data/A5")
        algo_g.plot_graph()

if __name__ == '__main__':
    unittest.main()
