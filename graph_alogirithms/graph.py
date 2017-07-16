"""
nodes are ordered alphabetically:
    BOS, BWI, DFW, JFK, LAX, MIA, ORD, PVD, SFO
BOS, -------------------------------------------
BWI,
DFW,
JFK,
LAX,
MIA,
ORD,
PVD,
SFO
"""

from enum import Enum


class AP(Enum):
    BOS, BWI, DFW, JFK, LAX, MIA, ORD, PVD, SFO = 0, 1, 2, 3, 4, 5, 6, 7, 8


large_value = float('inf')


class Graph(object):
    def __init__(self, connections, directed=False):
        self.graph = connections if connections else {}
        self.directed = directed

    def add(self, node1, node2):
        if self.graph[node1]:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = node2

    def get_vertices(self):
        return self.graph.keys()

    def get_connections(self, node):
        return self.graph[node] if self.graph[node] else []

    def __str__(self):
        return str(self.graph)

    def __len__(self):
        return len(self.graph)


adj_lst = {
    AP.BOS: [AP.MIA, AP.SFO, AP.PVD, AP.ORD],
    AP.BWI: [AP.ORD, AP.JFK, AP.MIA],
    AP.DFW: [AP.SFO, AP.MIA, AP.LAX, AP.ORD, AP.JFK],
    AP.JFK: [AP.BOS, AP.PVD, AP.ORD, AP.MIA, AP.DFW],
    AP.LAX: [AP.SFO, AP.DFW, AP.MIA],
    AP.MIA: [AP.LAX, AP.DFW, AP.JFK, AP.BOS],
    AP.ORD: [AP.SFO, AP.BOS, AP.PVD, AP.JFK, AP.BWI, AP.DFW],
    AP.PVD: [AP.ORD, AP.JFK],
    AP.SFO: [AP.BOS, AP.ORD, AP.DFW, AP.LAX],
}

adj_mtx = [
    [0, large_value, large_value, 187, large_value, 1258, 867, large_value, 2704],
    [large_value, 0, large_value, 184, large_value, 946, 621, large_value, large_value],
    [large_value, large_value, 0, 1391, 1235, 1121, 802, large_value, 1464],
    [187, 184, 1391, 0, large_value, 1090, 740, 144, large_value],
    [large_value, large_value, 1235, large_value, 0, 2342, large_value, large_value, 337],
    [1258, 946, 1121, 1090, 2342, 0, large_value, large_value, large_value],
    [867, 621, 802, 740, large_value, large_value, 0, 849, 1846],
    [large_value, large_value, large_value, 144, large_value, large_value, 849, 0, large_value],
    [2704, large_value, 1464, large_value, 337, large_value, 1846, large_value, 0]
]

adj_lst_directed = {
    AP.BOS: [AP.JFK],
    AP.JFK: [],
    AP.LAX: [AP.ORD, AP.SFO],
    AP.MIA: [AP.JFK],
    AP.PVD: [],
    AP.ORD: [AP.MIA, AP.PVD, AP.SFO],
    AP.SFO: [AP.BOS],
}

adj_lst_gfg = {
    0: [],
    1: [],
    2: [3],
    3: [1, 5],
    4: [0, 1],
    5: [0, 2]
}

if __name__ == '__main__':
    g = Graph(adj_lst_directed, True)
    print(g.get_connections(AP.BOS))[0]
    g.add(AP.PVD, AP.BOS)
