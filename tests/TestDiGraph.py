import unittest
from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):
    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)
        graph.add_node(0)
        self.assertTrue(graph.v_size() == 1)
        graph.add_node(0)
        self.assertTrue(graph.v_size() == 1)
        graph.add_node(1)
        self.assertTrue(graph.v_size() == 2)
        for i in range(1000):
            graph.add_node(i)

        self.assertTrue(graph.v_size() == 1000)

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 50)
        self.assertTrue(graph.e_size() == 1)


if __name__ == '__main__':
    unittest.main()
