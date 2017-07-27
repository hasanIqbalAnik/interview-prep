"""
Prim's algorithm finds the minimum spanning tree.

The basic of the algorithm works like this:
0. initialize visited array as empty,
1. pick any vertex from a set of vertices, mark it as source.
2. set the current distance to this vertex as 0 and infinity in every other cases.
3. for all edges from the source pick the one with the least edge cost,
4. while picking it, we have to check whether the new node from that edge is not already visited.
5. add all edges of it in the queue
5. recalculate the distances, if the new distance is less than the previous one, replace
6. the algorithm terminates when the queue is empty.

Time Complexity: O(E * V) -> where E is the number of edges, V is the number of nodes: this is my estimation


"""


from graph import adj_mtx, AP
import heapq as hq  # python priority queue implementation


# todo correct runtime analysis
lv, visited, heap, parent = float('inf'), {}, [], {}  # O(n)


def prims_mst(adj_matrix, src):
    hq.heappush(heap, (0, (src, None)))  # O(logn)
    curr_dist = {item.value: lv if item.value != src else 0 for item in AP}
    parent[src] = None

    while len(heap) != 0:
        curr_nd = hq.heappop(heap)[1][0]  # first element of the tuple is the value, second is the node  # O(1)
        visited[curr_nd] = True  # O(1)
        for nd, dst in enumerate(adj_matrix[src]):  # O(n) -> n is the number of nodes
            if nd not in visited and curr_dist[nd] > curr_dist[curr_nd] + adj_matrix[curr_nd][nd]:
                curr_dist[nd] = curr_dist[curr_nd] + adj_matrix[curr_nd][nd]
                hq.heappush(heap, (curr_dist[nd], (nd, curr_nd)))  # O(logn)
                parent[nd] = curr_nd

prims_mst(adj_mtx, 0)
print parent