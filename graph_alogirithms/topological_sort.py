"""
Topological Sorting:
Ordering vertices in a directed graph that makes sure that for every edge uv, node u appears before node v in the sorting.

Kahn's algorithm for topological sorting:
1. find out the indegrees of each vertex.
2. if its a DAG then it must have at least one vertex with indegree 0 and one with outdegree zero.
3. find the ones with indegrees of 0
4. add them in a queue
5. while q is not empty, pick one
6. add it to the resultset
7. find it's neighbors, reduce their indegrees by 1
8. if the indegree of this neighbor becomes 0, add it to the queue
9. repeat until the queue is empty

Time complexity: O(V + E) overall

"""
from graph import Graph, adj_lst_directed, AP, adj_lst_gfg
from collections import deque

graph = Graph(adj_lst_gfg, True)


def topological_sort(g):
    indegrees = {x: 0 for x in g.get_vertices()}  # complexity: O(V)
    q = deque()  #
    result = []  # to hold the sorted vertices

    for item1 in g.graph:  # O(V + E)
        for item2 in g.get_connections(item1):
            indegrees[item2] += 1

    for k, v in indegrees.iteritems():  # O(V)
        if v == 0:
            q.append(k)
    while q:  # O(V+E) because each vertex and edge is being read at most once
        current_node = q.popleft()
        result.append(current_node)
        neighbors = g.get_connections(current_node)
        for item in neighbors:
            indegrees[item] -= 1
            if indegrees[item] == 0:
                q.append(item)

    return result


res = topological_sort(graph)
if len(res) != len(adj_lst_gfg):
    print 'there was a cycle'
else:
    print res
