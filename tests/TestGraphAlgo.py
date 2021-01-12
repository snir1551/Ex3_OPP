import math
import unittest

from src import NodeData
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData


def first_graph():
    """

                0------>1------>2<------>3
                ↑     / |       |        ↑
                |    /  |       |        |
                |   /   |       |        |
                |  /    |       |        |
                | ↓     ↓       ↓        ↓
                7------>6<----->5<-------4
                       (7)

           """

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
                        ↑  ↑
                  (9) /     \(6)
                    /        \
                  ↓ (2)  (11) ↓
                6<----->3<---->4
                ↑     ↑  ↑     ↑
                |    /    \    |
           (14) |   /      \   | (15)
                |  / (9)(10 \  |
                | ↓          ↓ ↓
                1<------------>2
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
                   6<----->3<---->4
                   ↑     ↑  ↑     ↑
                   |    /    \    |
              (14) |   /      \   | (15)
                   |  / (9)(10 \  |
                   ↓ ↓          ↓ ↓
                   1<------------>2
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

    def test_get_graph(self):
        graph1 = second_graph()
        graph_algo = GraphAlgo(graph1)
        graph2 = graph_algo.get_graph()
        self.assertEqual(graph1, graph2)

    def test_eq(self):
        graph1 = second_graph()
        graph2 = second_graph()
        self.assertEqual(graph1, graph2)
        graph1 = three_graph()
        self.assertNotEqual(graph1, graph2)

    def test_shortest_path(self):
        #  print("second_graph")
        g_algo = GraphAlgo(second_graph())
        x, y = g_algo.shortest_path(1, 5)  # check1
        self.assertTrue(x == 20)
        ans_list1 = [1, 3, 6, 5]
        self.assertEqual(y, ans_list1)

        x, y = g_algo.shortest_path(2, 5)  # check2
        self.assertTrue(x == 21)
        ans_list1 = [2, 4, 5]
        self.assertEqual(y, ans_list1)

        #  print("three_graph")
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

        #  print("graph4")
        """
        0<-1->2->3
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
        x, y = g_algo3.shortest_path(3, 2)  # no way between this vertex
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        graph4.remove_node(2)  # remove node2
        x, y = g_algo3.shortest_path(1, 2)  # node not exist
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        x, y = g_algo3.shortest_path(2, 2)  # node not exist
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        x, y = g_algo3.shortest_path(1, 7)  # node not exist
        self.assertTrue(x == math.inf)
        self.assertTrue(y == [])
        x, y = g_algo3.shortest_path(10, 11)  # node not exist
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

    def test_save_and_load_json(self):
        """
               0->1->2->3
                  1<-
               """
        graph = DiGraph()
        tuple0 = (0, 30, 2)
        tuple1 = (50, 50, 50)
        tuple2 = (20, 20, 20)
        tuple3 = (30, 30, 30)
        node0 = NodeData(0, tuple0)
        node1 = NodeData(1, tuple1)
        node2 = NodeData(2, tuple2)
        node3 = NodeData(3, tuple3)

        graph.add_node(node0.get_key(), tuple0)
        graph.add_node(node1.get_key(), tuple1)
        graph.add_node(node2.get_key(), tuple2)
        graph.add_node(node3.get_key(), tuple3)
        graph.add_edge(1, 2, 11)
        graph.add_edge(2, 1, 11)
        graph.add_edge(2, 3, 5)
        graph.add_edge(1, 0, 3)
        g_algo = GraphAlgo(graph)
        g_algo.save_to_json("file1")

        new_graph_algo = GraphAlgo(None)
        new_graph_algo.load_from_json("file1")
        #  self.assertEqual(new_graph_algo.get_graph(), g_algo.get_graph()) ##to ask
        self.assertTrue(new_graph_algo.get_graph().get_mc() == 8)
        self.assertTrue(new_graph_algo.get_graph().v_size() == 4)
        self.assertTrue(new_graph_algo.get_graph().e_size() == 4)
        new_graph_algo.get_graph().remove_node(0)
        #  self.assertNotEqual(new_graph_algo.get_graph(), g_algo.get_graph())

    def test_connected_component(self):
        #  print("check0 connected_component ")
        """
                 empty graph
                                   """

        graph = DiGraph()
        g_algo = GraphAlgo(graph)
        my_list = []  # non exiting node
        self.assertEqual(my_list, g_algo.connected_component(89))  # empty graph return empty list

        print("check1 connected_component ")

        """
          0->1->2->3
             1<-
                           """

        graph1 = DiGraph()
        g_algo1 = GraphAlgo(graph1)
        graph1.add_node(0)
        graph1.add_node(1)
        graph1.add_node(2)
        graph1.add_node(3)
        graph1.add_edge(1, 2, 11)
        graph1.add_edge(2, 1, 11)
        graph1.add_edge(2, 3, 5)
        graph1.add_edge(1, 0, 3)
        my_list = [0]
        self.assertEqual(my_list, g_algo1.connected_component(0))
        my_list = [1, 2]
        self.assertEqual(my_list, g_algo1.connected_component(1))
        my_list = [2, 1]
        self.assertEqual(my_list, g_algo1.connected_component(2))
        my_list = [3]
        self.assertEqual(my_list, g_algo1.connected_component(3))

        #  print("check2 connected_component ")

        """

                    0------>1------>2<------>3
                    ↑     / |       |        ↑
                    |    /  |       |        |
                    |   /   |       |        |
                    |  /    |       |        |
                    | ↓     ↓       ↓        ↓
                    7------>6<----->5<-------4
                           (7)

               """

        g_algo2 = GraphAlgo(first_graph())
        my_list = [0, 1, 7]
        self.assertEqual(my_list, g_algo2.connected_component(0))
        my_list = [1, 7, 0]
        self.assertEqual(my_list, g_algo2.connected_component(1))
        my_list = [2, 3, 4]
        self.assertEqual(my_list, g_algo2.connected_component(2))
        my_list = [3, 2, 4]
        self.assertEqual(my_list, g_algo2.connected_component(3))
        my_list = [4, 3, 2]
        self.assertEqual(my_list, g_algo2.connected_component(4))
        my_list = [5, 6]
        self.assertEqual(my_list, g_algo2.connected_component(5))
        my_list = [6, 5]
        self.assertEqual(my_list, g_algo2.connected_component(6))
        my_list = [7, 0, 1]
        self.assertEqual(my_list, g_algo2.connected_component(7))

        #  print("check3 connected_component ")

        """
                             5
                           ↑  ↑
                     (9) /     \(6)
                       /        \
                     ↓ (2)  (11) ↓
                   6<----->3<---->4
                   ↑     ↑  ↑     ↑
                   |    /    \    |
              (14) |   /      \   | (15)
                   |  / (9)(10 \  |
                   | ↓          ↓ ↓
                   1<------------>2
                          (7)

              """

        g_algo3 = GraphAlgo(second_graph())
        my_list = [1, 2, 4, 3, 6, 5]
        self.assertEqual(my_list, g_algo3.connected_component(1))
        my_list = [2, 1, 3, 4, 5, 6]
        self.assertEqual(my_list, g_algo3.connected_component(2))
        my_list = [3, 1, 2, 4, 5, 6]
        self.assertEqual(my_list, g_algo3.connected_component(3))
        my_list = [4, 2, 1, 3, 6, 5]
        self.assertEqual(my_list, g_algo3.connected_component(4))
        my_list = [5, 4, 2, 1, 3, 6]
        self.assertEqual(my_list, g_algo3.connected_component(5))
        my_list = [6, 1, 2, 4, 3, 5]
        self.assertEqual(my_list, g_algo3.connected_component(6))

        #  print("check4 connected_component ")
        """
                               5

                        (2)    (11)
                     6<----->3<---->4
                     ↑     ↑  ↑     ↑
                     |    /    \    |
                (14) |   /      \   | (15)
                     |  / (9)(10 \  |
                     ↓ ↓          ↓ ↓
                     1<------------>2
                            (7)

                """

        g_algo4 = GraphAlgo(three_graph())
        my_list = [1, 2, 4, 3, 6]
        self.assertEqual(my_list, g_algo4.connected_component(1))
        my_list = [2, 1, 3, 4, 6]
        self.assertEqual(my_list, g_algo4.connected_component(2))
        my_list = [3, 1, 2, 4, 6]
        self.assertEqual(my_list, g_algo4.connected_component(3))
        my_list = [4, 2, 1, 3, 6]
        self.assertEqual(my_list, g_algo4.connected_component(4))
        my_list = [5]
        self.assertEqual(my_list, g_algo4.connected_component(5))
        my_list = [6, 1, 2, 4, 3]
        self.assertEqual(my_list, g_algo4.connected_component(6))

        #  print("check5 connected_component ")

        """
        4<-0->1  2->3  4->0  5
         
                       """
        graph4 = DiGraph()
        g_algo5 = GraphAlgo(graph4)
        graph4.add_node(0)
        graph4.add_node(1)
        graph4.add_node(2)
        graph4.add_node(3)
        graph4.add_node(4)
        graph4.add_node(5)
        graph4.add_edge(0, 1, 11)
        graph4.add_edge(0, 4, 11)
        graph4.add_edge(2, 3, 5)
        graph4.add_edge(4, 0, 3)
        my_list = [0, 4]
        self.assertEqual(my_list, g_algo5.connected_component(0))
        my_list = [1]
        self.assertEqual(my_list, g_algo5.connected_component(1))
        my_list = [2]
        self.assertEqual(my_list, g_algo5.connected_component(2))
        my_list = [3]
        self.assertEqual(my_list, g_algo5.connected_component(3))
        my_list = [4, 0]
        self.assertEqual(my_list, g_algo5.connected_component(4))
        my_list = [5]
        self.assertEqual(my_list, g_algo5.connected_component(5))

    def test_connected_components(self):
        #  print("check0 connected_components ")
        graph1 = DiGraph()
        g_algo6 = GraphAlgo(graph1)
        my_list = []
        self.assertEqual(my_list, g_algo6.connected_components())  # empty graph

        #  print("check1 connected_components ")

        """
          0->1->2->3
             1<-
                           """
        graph4 = DiGraph()
        g_algo7 = GraphAlgo(graph4)
        graph4.add_node(0)
        graph4.add_node(1)
        graph4.add_node(2)
        graph4.add_node(3)
        graph4.add_edge(1, 2, 11)
        graph4.add_edge(2, 1, 11)
        graph4.add_edge(2, 3, 5)
        graph4.add_edge(1, 0, 3)
        my_list = [[1, 2], [3], [0]]
        self.assertEqual(my_list, g_algo7.connected_components())

        #  print("check2 connected_components ")

        """

                    0------>1------>2<------>3
                    ↑     / |       |        ↑
                    |    /  |       |        |
                    |   /   |       |        |
                    |  /    |       |        |
                    | ↓     ↓       ↓        ↓
                    7------>6<----->5<-------4
                           (7)

               """
        g_algo8 = GraphAlgo(first_graph())
        my_list = [[0, 1, 7], [2, 3, 4], [5, 6]]
        self.assertEqual(my_list, g_algo8.connected_components())

        #  print("check3 connected_components ")
        """
                             5
                           ↑  ↑
                     (9) /     \(6)
                       /        \
                     ↓ (2)  (11) ↓
                   6<----->3<---->4
                   ↑     ↑  ↑     ↑
                   |    /    \    |
              (14) |   /      \   | (15)
                   |  / (9)(10 \  |
                   | ↓          ↓ ↓
                   1<------------>2
                          (7)

              """
        g_algo9 = GraphAlgo(second_graph())
        my_list = [[1, 2, 4, 3, 6, 5]]
        self.assertEqual(my_list, g_algo9.connected_components())

        #  print("check4 connected_components ")
        """
                               5

                        (2)    (11)
                     6<----->3<---->4
                     ↑     ↑  ↑     ↑
                     |    /    \    |
                (14) |   /      \   | (15)
                     |  / (9)(10 \  |
                     ↓ ↓          ↓ ↓
                     1<------------>2
                            (7)

                """
        g_algo10 = GraphAlgo(three_graph())
        my_list = [[5], [1, 2, 4, 3, 6]]
        self.assertEqual(my_list, g_algo10.connected_components())

        #  print("check5 connected_components ")

        """
        4<-0->1  2->3  4->0  5

                       """
        graph4 = DiGraph()
        g_algo11 = GraphAlgo(graph4)
        graph4.add_node(0)
        graph4.add_node(1)
        graph4.add_node(2)
        graph4.add_node(3)
        graph4.add_node(4)
        graph4.add_node(5)
        graph4.add_edge(0, 1, 11)
        graph4.add_edge(0, 4, 11)
        graph4.add_edge(2, 3, 5)
        graph4.add_edge(4, 0, 3)
        my_list = [[5], [2], [3], [0, 4], [1]]
        self.assertEqual(my_list, g_algo11.connected_components())

    def test_plot_graph(self):
        graph4 = DiGraph()
        g_algo = GraphAlgo(graph4)
        g_algo.load_from_json("../data/A0")
        g_algo.plot_graph()
        g_algo.load_from_json("../data/A1")
        g_algo.plot_graph()
        g_algo.load_from_json("../data/A2")
        g_algo.plot_graph()
        g_algo.load_from_json("../data/A3")
        g_algo.plot_graph()
        g_algo.load_from_json("../data/A4")
        g_algo.plot_graph()
        g_algo.load_from_json("../data/A5")
        g_algo.plot_graph()

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
        g_algo3.plot_graph()


if __name__ == '__main__':
    unittest.main()
