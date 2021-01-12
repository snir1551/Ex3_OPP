import unittest

from src.DiGraph import DiGraph
from src.NodeData import NodeData
import random


class MyTestCase(unittest.TestCase):

    def test_get_key(self):
        for i in range(100):
            key = random.uniform(0, 50)
            key_int = int(key)
            node: NodeData = NodeData(key_int, (1, 2, 3))
            self.assertTrue(node.get_key() == key_int)

    def test_get_pos(self):
        for j in range(100):
            key = random.uniform(0, 50)
            key_int = int(key)
            x = random.uniform(50, 100)
            y = random.uniform(50, 100)
            z = random.uniform(50, 100)
            node: NodeData = NodeData(key_int, (x, y, z))
            self.assertTrue(node.get_pos() == (x, y, z))

    def test_set_pos(self):
        for i in range(100):
            key = random.uniform(0, 50)
            key_int = int(key)
            x = random.uniform(50, 100)
            y = random.uniform(50, 100)
            z = random.uniform(50, 100)
            node: NodeData = NodeData(key_int, (x, y, z))
            self.assertTrue(node.get_pos() == (x, y, z))
            x = random.uniform(50, 100)
            y = random.uniform(50, 100)
            z = random.uniform(50, 100)
            node.set_pos((x, y, z))
            self.assertTrue(node.get_pos() == (x, y, z))

    def test_set_and_get_weight_(self):
        for i in range(100):
            weight = random.uniform(0, 50)
            node: NodeData = NodeData(i, (20, 30, 40))
            self.assertTrue(node.get_weight() == 0)
            node.set_weight(weight)
            self.assertTrue(node.get_weight() == weight)

    def test_get_and_set_info(self):
        node: NodeData = NodeData(1, (20, 30, 40))
        self.assertTrue(node.get_info() == "")
        node.set_info("black")
        self.assertTrue(node.get_info() == "black")
        node.set_info("white")
        self.assertTrue(node.get_info() == "white")

    def test_get_and_set_counter_edges_in(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 20)
        graph.add_edge(1, 3, 20)
        graph.add_edge(2, 3, 20)
        self.assertTrue(graph.get_node(1).get_counter_edges_in() == 0)
        self.assertTrue(graph.get_node(2).get_counter_edges_in() == 1)
        self.assertTrue(graph.get_node(3).get_counter_edges_in() == 2)
        graph.get_node(1).set_counter_edges_in(5)
        self.assertTrue(graph.get_node(1).get_counter_edges_in() == 5)
        graph.get_node(3).set_counter_edges_in(10)
        self.assertTrue(graph.get_node(3).get_counter_edges_in() == 10)

    def test_get_and_set_counter_edges_out(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 20)
        graph.add_edge(1, 3, 20)
        graph.add_edge(2, 3, 20)
        self.assertTrue(graph.get_node(1).get_counter_edges_out() == 2)
        self.assertTrue(graph.get_node(2).get_counter_edges_out() == 1)
        self.assertTrue(graph.get_node(3).get_counter_edges_out() == 0)
        graph.get_node(1).set_counter_edges_out(5)
        self.assertTrue(graph.get_node(1).get_counter_edges_out() == 5)
        graph.get_node(3).set_counter_edges_out(10)
        self.assertTrue(graph.get_node(3).get_counter_edges_out() == 10)
        graph.get_node(2).set_counter_edges_out(20)
        self.assertTrue(graph.get_node(2).get_counter_edges_out() == 20)


if __name__ == '__main__':
    unittest.main()
