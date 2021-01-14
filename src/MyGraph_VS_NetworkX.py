import json
import networkx as nxlib
import timeit
from GraphAlgo import GraphAlgo


def NetworkX():
    g = nxlib.DiGraph()
    nodes = [10, 100, 1000, 10000, 20000, 30000]
    edges = [80, 800, 8000, 80000, 160000, 240000]
    for ve, ed in zip(nodes, edges):
        with open(f"../data/Graphs_on_circle/G_{ve}_{ed}_1.json", 'r') as file:
            object = json.load(file)

        for x in object['Nodes']:
            g.add_node(int(x.get('id')))

        for x in object['Edges']:
            g.add_edge(int(x.get('src')), int(x.get('dest')), weight=float(x.get('w')))

        start = timeit.default_timer()
        nxlib.shortest_path(g, source=1, target=3, method="dijkstra", weight="weight")
        stop = timeit.default_timer()
        print("time Shortest path NetworkX", {ve}, {ed}, stop - start)
        start = timeit.default_timer()
        nxlib.strongly_connected_components(g)
        stop = timeit.default_timer()
        print("time components NetworkX", {ve}, {ed}, stop - start)


def MyGraph():
    nodes = [10, 100, 1000, 10000, 20000, 30000]
    edges = [80, 800, 8000, 80000, 160000, 240000]
    graph_algo = GraphAlgo()
    for ve, ed in zip(nodes, edges):
        graph_algo.load_from_json(f"../data/Graphs_on_circle/G_{ve}_{ed}_1.json")
        start = timeit.default_timer()
        graph_algo.shortest_path(1, 3)
        stop = timeit.default_timer()
        print("time Shortest path MyGraph", {ve}, {ed}, stop - start)
        start = timeit.default_timer()
        graph_algo.connected_components()
        stop = timeit.default_timer()
        print("time components MyGraph", {ve}, {ed}, stop - start)
        start = timeit.default_timer()
        graph_algo.connected_component(1)
        stop = timeit.default_timer()
        print("time component MyGraph", {ve}, {ed}, stop - start)


if __name__ == '__main__':
    NetworkX()
    MyGraph()