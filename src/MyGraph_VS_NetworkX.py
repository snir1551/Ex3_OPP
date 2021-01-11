import json
import networkx as nx
from networkx.readwrite import json_graph
from unittest import TestCase
import time
import matplotlib.pyplot as plt
from GraphAlgo import GraphAlgo


class MyGraphVSNetworkX:
   pass

if __name__ == '__main__':

    nodes = [10, 100, 1000, 10000, 20000, 30000]
    edges = [80, 800, 8000, 80000, 160000, 240000]
    graph_algo = GraphAlgo()
    for ve, ed in zip(nodes, edges):
        graph_algo.load_from_json(f"../data/G_{ve}_{ed}_0.json")
        start_time = time.time()
        graph_algo.connected_components()
        our_time = time.time() - start_time
        start_time = time.time()
        nx_time = time.time() - start_time

        print("our connected_component: ", our_time)
        print("nx connected_component: ", nx_time)
        # g.plot_graph()
