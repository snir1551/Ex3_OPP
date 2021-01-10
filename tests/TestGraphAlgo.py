import math
import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
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

    def test_shortest_path(self):
        print("graph2")
        g_algo = GraphAlgo(second_graph())
        x, y = g_algo.shortest_path(1, 5)  # check1
        self.assertTrue(x == 20)
        ans_list1 = [1, 3, 6, 5]
        self.assertEqual(y, ans_list1)

        x, y = g_algo.shortest_path(2, 5)  # check2
        self.assertTrue(x == 21)
        ans_list1 = [2, 4, 5]
        self.assertEqual(y, ans_list1)

        print("graph3")
        g_algo2 = GraphAlgo(three_graph())
        x, y = g_algo2.shortest_path(1, 5)  # check3 node5 not connected
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        x, y = g_algo2.shortest_path(5, 5)  # check4 node5 not connected and solo
        self.assertTrue(x == 0)
        ans_list1 = [5]
        self.assertEqual(y, ans_list1)
        x, y = g_algo2.shortest_path(1, 6)  # check5
        self.assertTrue(x == 11)
        ans_list1 = [1, 3, 6]
        self.assertEqual(y, ans_list1)
        x, y = g_algo2.shortest_path(1, 3)  # check6
        self.assertTrue(x == 9)
        ans_list1 = [1, 3]
        self.assertEqual(y, ans_list1)
        x, y = g_algo2.shortest_path(1, 4)  # check7
        self.assertTrue(x == 20)
        ans_list1 = [1, 3, 4]
        self.assertEqual(y, ans_list1)
        g_algo2.get_graph().remove_edge(1, 3)  # remove edge between node1 and node3
        x, y = g_algo2.shortest_path(1, 4)  # check8
        self.assertTrue(x == 22)
        ans_list1 = [1, 2, 4]
        self.assertEqual(y, ans_list1)
        x, y = g_algo2.shortest_path(1, 1)  # check9
        self.assertTrue(x == 0)
        ans_list1 = [1]
        self.assertEqual(y, ans_list1)

        print("graph4")
        """
        0->1->2->3
           1<-
        """
        graph4 = DiGraph()
        g_algo3 = GraphAlgo(graph4)
        graph4.add_node(0)
        graph4.add_node(1)
        graph4.add_node(2)
        graph4.add_node(3)
        graph4.add_edge(1, 2, 11)
        graph4.add_edge(2, 1, 11)
        graph4.add_edge(2, 3, 5)
        graph4.add_edge(1, 0, 3)
        x, y = g_algo3.shortest_path(2, 0)
        self.assertTrue(x == 14)  # check10
        ans_list1 = [2, 1, 0]
        self.assertEqual(y, ans_list1)
        graph4.remove_node(2)  # remove node2
        x, y = g_algo3.shortest_path(1, 2)  # node not exist
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        x, y = g_algo3.shortest_path(2, 2)  # node not exist
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])

        # print("graph5")
        # graph5 = DiGraph()
        # g_algo5 = GraphAlgo(graph5)
        # for i in range(0, 8):
        #     graph5.add_node(i)
        # for i in range(0, 8):
        #     graph5.add_edge(i, i + 1, i + 1)
        # for i in range(0, 8):
        #     x, y = g_algo3.shortest_path(i, 11)
        #     self.assertTrue(x == math.inf)
        #     self.assertTrue(y == [])
        #     print(x)

    def test_save_to_json(self):
        graph = DiGraph()
        g_algo = GraphAlgo(graph)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 7)
        g_algo.save_to_json("file1")

    def test_load_from_json(self):
        g_algo = GraphAlgo(None)
        g_algo.load_from_json("file1")
        g_algo_check = g_algo
        print(g_algo_check.get_graph().get_mc())


if __name__ == '__main__':
    unittest.main()
