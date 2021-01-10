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
        print("graph1")
        g_algo = GraphAlgo(second_graph())
        x, y = g_algo.shortest_path(1, 5)  # check1
        self.assertTrue(x == 20)
        ans_list1 = [1, 3, 6, 5]
        print(y)

        for i in ans_list1:
            self.assertIn(i, y)

        x, y = g_algo.shortest_path(2, 5)  # check2
        print(y)
        self.assertTrue(x == 21)
        ans_list2 = [2, 4, 5]
        for i in y:
            self.assertIn(i, ans_list2)

        print("graph2")
        g_algo2 = GraphAlgo(three_graph())
        p = g_algo2.shortest_path(1, 5)
        print(p)
        p = g_algo2.shortest_path(2, 5)
        print(p)
        p = g_algo2.shortest_path(1, 6)
        print(p)
        p = g_algo2.shortest_path(1, 3)
        print(p)
        p = g_algo2.shortest_path(1, 4)
        print(p)
        g_algo2.get_graph().remove_edge(1, 3)
        p = g_algo2.shortest_path(1, 4)
        print(p)
        p = g_algo2.shortest_path(1, 1)
        print(p)

        print("graph3")
        graph3 = DiGraph()
        g_algo3 = GraphAlgo(graph3)
        graph3.add_node(1)
        graph3.add_node(2)
        graph3.add_node(3)
        graph3.add_edge(1, 2, 11)
        graph3.add_edge(2, 3, 5)
        p = g_algo3.shortest_path(1, 3)
        print(len(p))
        graph3.remove_node(2)
        p = g_algo3.shortest_path(1, 3)
        print(p)

        if __name__ == '__main__':
            unittest.main()
