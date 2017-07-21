"""
Depth first search can be used to detect cycle in a directed graph.
The basic idea is to keep track of visited vertices and run dfs recursively.
If at any point of the execution we encounter a node that is already in the visited
array, then there is a cycle.

Time Complexity is the same as the time complexity of a DFS, O(V+E)
"""

from graph import Graph, adj_lst_directed, AP
from collections import deque


def detect_cycle_util(root_node, airport_graph, visited, total_length=None):
    if root_node not in visited:
        visited[root_node] = True
        for item in airport_graph.get_connections(root_node):
            return detect_cycle_util(item, airport_graph, visited, total_length)
        return False
    else:
        return True


def contains_cycle(airports, init_queue):
    while init_queue:
        root = init_queue.popleft()
        if detect_cycle_util(root, airports, {}, len(airports.get_vertices())):
            return True
    return False

airports = Graph(adj_lst_directed, directed=True)
init_queue = deque(airports.get_vertices())

print contains_cycle(airports, init_queue)
