import unittest
from src.DiGraph import DiGraph
from src.NodeData import NodeData
from unittest import TestCase
from src.EdgeData import EdgeData


class TestDiGraph(TestCase):
    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)
        is_add_node = graph.add_node(0)
        # add node: 0
        self.assertTrue(is_add_node)
        self.assertTrue(graph.v_size() == 1)
        is_add_node = graph.add_node(0)
        # we had node 0 so he didn't add him and return false
        self.assertFalse(is_add_node)
        self.assertTrue(graph.v_size() == 1)
        is_add_node = graph.add_node(1)
        # add node: 1
        self.assertTrue(graph.v_size() == 2)
        self.assertTrue(is_add_node)

        # we add nodes from 0 to 999
        for i in range(1000):
            graph.add_node(i)

        self.assertTrue(graph.v_size() == 1000)

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(9)
        graph.add_node(10)
        graph.add_node(11)
        graph.add_node(8)
        # our nodes in graph: 1,2,8,9,10,11
        self.assertTrue(graph.e_size() == 0)
        is_add_edge = graph.add_edge(1, 2, 50)
        # edge: 1->2
        self.assertTrue(is_add_edge)
        self.assertTrue(graph.e_size() == 1)
        is_add_edge = graph.add_edge(1, 2, 40)
        # we had edge but the weight change : 1->2 w=40
        self.assertTrue(is_add_edge)
        self.assertTrue(graph.e_size() == 1)
        is_add_edge = graph.add_edge(1, 2, 50)
        # we had edge but the weight change : 1->2 so he change the weight but not add edge
        self.assertTrue(is_add_edge)
        self.assertTrue(graph.e_size() == 1)
        is_add_edge = graph.add_edge(2, 1, 50)
        # edge: 2->1
        self.assertTrue(is_add_edge)
        self.assertTrue(graph.e_size() == 2)
        for i in range(0, 3):
            for j in range(5, 10):
                graph.add_edge(i, j, 1000)
        # we have edges: 1->2,2->1,1->8,1->9,2->8,2->9
        self.assertTrue(graph.e_size() == 6)
        graph.add_edge(9, 1, -1)
        graph.add_edge(9, 1, -2)
        graph.add_edge(9, 1, -1000)
        self.assertTrue(graph.e_size() == 6)
        graph.add_edge(9, 1, 0)
        self.assertTrue(graph.e_size() == 7)

    def test_get_all_v(self):
        graph = DiGraph()
        tuple0 = (0, 30, 2)
        tuple1 = (50, 50, 50)
        node0 = NodeData(0, tuple0)  # node: key=0 tuple=(0, 30, 2)
        node1 = NodeData(2, tuple0)  # node: key=2 tuple=(0, 30, 2)
        node2 = NodeData(10, tuple1)  # node: key=10 tuple=(50, 50, 50)

        graph.add_node(node0.get_key(), tuple0)
        graph.add_node(node1.get_key(), tuple0)
        graph.add_node(node2.get_key(), tuple1)

        nodes = [node0, node1, node2]

        for node in nodes:
            self.assertIn(node, graph.get_all_v().values())

    def test_remove_node(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)  # we have 0 nodes in the graph
        graph.add_node(1)  # add node 1 to graph
        self.assertTrue(graph.v_size() == 1)  # we have 1 nodes in the graph
        is_remove_node = graph.remove_node(1)  # remove node 1 from graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        self.assertTrue(graph.v_size() == 0)  # we have 0 nodes in the graph
        is_remove_node = graph.remove_node(1)  # tried remove node that not exist in the graph
        self.assertFalse(is_remove_node)  # is_remove_node is false because we tried remove node that not exist
        is_remove_node = graph.remove_node(1)  # tried remove node that not exist in the graph
        self.assertFalse(is_remove_node)  # is_remove_node is false because we tried remove node that not exist
        self.assertTrue(graph.v_size() == 0)  # we have 0 nodes in the graph
        for i in range(5, 10):  # add five nodes to the graph
            graph.add_node(i)

        self.assertTrue(graph.v_size() == 5)  # we have 5 nodes in the graph
        is_remove_node = graph.remove_node(10)  # remove node that not exist in the graph
        self.assertFalse(is_remove_node)  # is_remove_node is false because we tried remove node that not exist
        is_remove_node = graph.remove_node(4)  # remove node that not exist in the graph
        self.assertFalse(is_remove_node)  # is_remove_node is false because we tried remove node that not exist
        self.assertTrue(graph.v_size() == 5)  # we have 5 nodes in the graph
        is_remove_node = graph.remove_node(8)  # remove node from the graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        self.assertTrue(graph.v_size() == 4)  # we have 4 nodes in the graph
        is_remove_node = graph.remove_node(5)  # remove node from the graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        is_remove_node = graph.remove_node(6)  # remove node from the graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        is_remove_node = graph.remove_node(7)  # remove node from the graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        is_remove_node = graph.remove_node(9)  # remove node from the graph
        self.assertTrue(is_remove_node)  # is_remove_node is true because we success to remove
        self.assertTrue(graph.v_size() == 0)  # we have 0 nodes in the graph
        for i in range(5, 10):  # add five nodes to the graph
            graph.add_node(i)
        graph.add_edge(5, 6, 30)  # edge: 5->6
        graph.add_edge(5, 7, 20)  # edge: 5->7
        graph.add_edge(7, 5, 30)  # edge: 7->5
        graph.add_edge(9, 5, 20)  # edge: 9->5
        graph.add_edge(9, 6, 30)  # edge: 9->6
        graph.add_edge(7, 6, 30)  # edge: 7->6
        self.assertTrue(graph.e_size() == 6)
        graph.remove_node(5)  # remove node(5)
        self.assertTrue(graph.e_size() == 2)
        self.assertTrue(graph.get_mc() == 28)

    def test_remove_edge(self):
        graph = DiGraph()
        is_remove_edge = graph.remove_edge(1, 2)  # tried to remove edge that not exist in the graph
        self.assertFalse(is_remove_edge)  # is_remove_edge is false because tried to remove edge that not exist
        self.assertTrue(graph.e_size() == 0)
        graph.add_edge(1, 2, 30)  # tried to connect node1 to node2 and the nodes that not exist in the graph
        graph.add_node(1)
        is_remove_edge = graph.remove_edge(1, 2)  # tried to connect node1 to node2 and the node2 that not exist
        self.assertFalse(is_remove_edge)  # is_remove_edge is false because tried to remove edge that node2 not exist
        self.assertTrue(graph.e_size() == 0)
        graph.add_node(2)
        graph.add_edge(1, 2, 30)
        graph.add_edge(1, 2, 30)
        self.assertTrue(graph.e_size() == 1)
        graph.add_edge(2, 1, 30)
        self.assertTrue(graph.e_size() == 2)
        is_remove_edge = graph.remove_edge(1, 2)
        self.assertTrue(is_remove_edge)  # remove edge 1->2
        self.assertTrue(graph.e_size() == 1)
        is_remove_edge = graph.remove_edge(1, 2)  # tried remove edge that not exist
        self.assertFalse(is_remove_edge)
        self.assertTrue(graph.e_size() == 1)
        is_remove_edge = graph.remove_edge(2, 1)  # remove edge 2->1
        self.assertTrue(is_remove_edge)  # remove edge 1->2
        self.assertTrue(graph.e_size() == 0)

    def test_v_size(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)
        graph.add_node(1)  # add node1
        self.assertTrue(graph.v_size() == 1)
        graph.add_node(2)  # add node2
        graph.add_edge(1, 2, 50)  # connect 1-2
        graph.add_node(3)  # add node3
        graph.add_edge(2, 3, 20)  # connect 2-3
        graph.add_node(4)  # add node4
        self.assertTrue(graph.v_size() == 4)
        graph.remove_node(1)  # remove 1
        self.assertTrue(graph.v_size() == 3)
        graph.remove_node(4)  # remove 4
        self.assertTrue(graph.v_size() == 2)
        graph.remove_node(3)  # remove 3
        graph.remove_node(2)  # remove 2
        self.assertTrue(graph.v_size() == 0)

    def test_e_size(self):
        graph = DiGraph()
        self.assertTrue(graph.v_size() == 0)  # not edges
        self.assertTrue(graph.e_size() == 0)  # not vertex
        graph.add_node(1)  # add node1
        self.assertTrue(graph.v_size() == 1)
        graph.add_node(2)  # add node2
        graph.add_edge(1, 2, 50)  # connect 1-2
        self.assertTrue(graph.e_size() == 1)
        graph.add_node(3)  # add node3
        graph.add_edge(2, 3, 20)  # connect 2-3
        self.assertTrue(graph.e_size() == 2)
        graph.add_node(4)  # add node4
        self.assertTrue(graph.v_size() == 4)
        graph.remove_node(1)  # remove 1
        self.assertTrue(graph.v_size() == 3)
        self.assertTrue(graph.e_size() == 1)
        graph.remove_node(3)  # remove 3
        graph.remove_node(2)  # remove 2
        self.assertTrue(graph.e_size() == 0)
        self.assertTrue(graph.v_size() == 1)

        # node 4 still exist
        graph.add_node(1)  # add node1
        graph.add_edge(1, 4, 10)  # connect 1-4
        self.assertTrue(graph.e_size() == 1)
        graph.add_node(2)  # add node2
        graph.add_node(3)  # add node3
        graph.add_edge(2, 3, -1)  # not add because weight not positive
        self.assertTrue(graph.e_size() == 1)
        self.assertTrue(graph.v_size() == 4)
        graph.add_edge(2, 3, 0)  # connect 2-3
        self.assertTrue(graph.e_size() == 2)
        graph.add_edge(2, 3, 6)  # change the weight
        self.assertTrue(graph.e_size() == 2)
        graph.remove_edge(2, 3)  # remove 2-3
        self.assertTrue(graph.e_size() == 1)
        graph.remove_edge(1, 4)  # remove 1-4
        self.assertTrue(graph.e_size() == 0)

    def test_get_mc(self):
        graph = DiGraph()
        self.assertTrue(graph.get_mc() == 0)
        self.assertTrue(graph.v_size() == 0)
        self.assertTrue(graph.e_size() == 0)
        graph.add_node(1)  # add node1
        self.assertTrue(graph.get_mc() == 1)
        self.assertTrue(graph.v_size() == 1)
        graph.add_node(2)  # add node2
        graph.add_edge(1, 2, -4)  # not connect weight not positive
        graph.add_edge(1, 2, 50)  # connect 1-2
        self.assertTrue(graph.get_mc() == 3)
        self.assertTrue(graph.e_size() == 1)
        graph.add_node(3)  # add node3
        self.assertTrue(graph.get_mc() == 4)
        graph.add_edge(2, 3, 20)  # connect 2-3
        self.assertTrue(graph.get_mc() == 5)
        self.assertTrue(graph.e_size() == 2)
        graph.add_node(4)  # add node4
        self.assertTrue(graph.get_mc() == 6)
        self.assertTrue(graph.v_size() == 4)
        graph.remove_node(1)  # remove 1
        self.assertTrue(graph.get_mc() == 8)
        self.assertTrue(graph.e_size() == 1)
        graph.remove_node(3)  # remove 3
        self.assertTrue(graph.get_mc() == 10)
        self.assertTrue(graph.e_size() == 0)
        self.assertTrue(graph.v_size() == 2)
        # node2 and node4 still exist
        graph.add_node(1)  # add node1
        graph.add_edge(1, 4, 10)  # connect 1-4
        graph.add_node(3)  # add node3
        graph.add_edge(2, 3, -1)  # not connect weight not positive
        self.assertTrue(graph.get_mc() == 13)
        self.assertTrue(graph.v_size() == 4)
        self.assertTrue(graph.e_size() == 1)
        graph.add_edge(2, 3, 5)  # connect 2-3
        self.assertTrue(graph.get_mc() == 14)
        self.assertTrue(graph.e_size() == 2)
        graph.remove_edge(2, 3)  # remove 2-3
        self.assertTrue(graph.get_mc() == 15)
        self.assertTrue(graph.e_size() == 1)
        graph.remove_edge(1, 4)  # remove 1-4
        self.assertTrue(graph.get_mc() == 16)
        self.assertTrue(graph.e_size() == 0)

    def test_all_in_edges_of_node(self):
        graph = DiGraph()

        tuple0 = (0, 30, 2)
        tuple1 = (50, 50, 50)
        node0 = NodeData(0, tuple0)  # node: key=0 tuple=(0, 30, 2)
        node1 = NodeData(1, tuple0)  # node: key=1 tuple=(0, 30, 2)
        node2 = NodeData(2, tuple1)  # node: key=2 tuple=(50, 50, 50)
        node3 = NodeData(3, tuple1)  # node: key=3 tuple=(50, 50, 50)

        graph.add_node(node0.get_key(), tuple0)  # add node0
        self.assertEqual({}, graph.all_in_edges_of_node(node0.get_key()))  # check the list In empty
        graph.add_node(node1.get_key(), tuple0)  # add node1
        graph.add_node(node2.get_key(), tuple1)  # add node2
        graph.add_node(node3.get_key(), tuple1)  # add node3

        graph.add_edge(node1.get_key(), node0.get_key(), 10)  # connect 1->0
        graph.add_edge(node2.get_key(), node0.get_key(), 15)  # connect 2->0
        graph.add_edge(node3.get_key(), node0.get_key(), 20)  # connect 3->0

        ans_list_keys = [node1.get_key(), node2.get_key(), node3.get_key()]
        for i in graph.all_in_edges_of_node(node0.get_key()).keys():
            self.assertIn(i, ans_list_keys)
        graph.remove_node(node2.get_key())  # remove node2
        graph.remove_node(node3.get_key())  # remove node3

        ans_list_keys = [node1.get_key()]
        for i in ans_list_keys:
            self.assertIn(i, graph.all_in_edges_of_node(node0.get_key()).keys())

    def test_all_out_edges_of_node(self):
        graph = DiGraph()

        tuple0 = (0, 30, 2)
        tuple1 = (50, 50, 50)
        node0 = NodeData(0, tuple0)  # node: key=0 tuple=(0, 30, 2)
        node1 = NodeData(1, tuple0)  # node: key=1 tuple=(0, 30, 2)
        node2 = NodeData(2, tuple1)  # node: key=2 tuple=(50, 50, 50)
        node3 = NodeData(3, tuple1)  # node: key=3 tuple=(50, 50, 50)

        graph.add_node(node0.get_key(), tuple0)  # add node0
        self.assertEqual({}, graph.all_out_edges_of_node(node0.get_key()))  # check the list In empty
        graph.add_node(node1.get_key(), tuple0)  # add node1
        graph.add_node(node2.get_key(), tuple1)  # add node2
        graph.add_node(node3.get_key(), tuple1)  # add node3

        graph.add_edge(node1.get_key(), node0.get_key(), 10)  # connect 1->0
        graph.add_edge(node1.get_key(), node2.get_key(), 15)  # connect 1->2
        graph.add_edge(node1.get_key(), node3.get_key(), 20)  # connect 1->2

        ans_list_keys = [node0.get_key(), node2.get_key(), node3.get_key()]
        for i in graph.all_out_edges_of_node(node1.get_key()).keys():
            self.assertIn(i, ans_list_keys)
        graph.remove_node(node2.get_key())  # remove node2
        graph.remove_node(node3.get_key())  # remove node3

        ans_list_keys = [node0.get_key()]
        for i in ans_list_keys:
            self.assertIn(i, graph.all_out_edges_of_node(node1.get_key()).keys())


if __name__ == '__main__':
    unittest.main()
