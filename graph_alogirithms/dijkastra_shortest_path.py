"""
Dijkastra's algorithm finds the shortest path between two nodes in a grpah.
Given a source node, this algorithm finds the shortest path between this node
and all other nodes. This algorithm can be used to find the shortest path between any two
 nodes, because once the destination node is reached, we can stop the execution of the algorithm.

In this program we will select Boston(BOS) as the source vertex and Los Angeles as the destination,
we will try to compute the shortest path that exists among all routes.
    0     1    2    3    4     5   6    7    8
    BOS, BWI, DFW, JFK, LAX, MIA, ORD, PVD, SFO

The time complexity of the algorithm is: O(|n| * |k|)

This complexity can be reduced to

"""
from graph import adj_mtx, AP

source = AP.LAX.value
destination = AP.PVD.value


def dijkastra_shortest_path(adj_matrix, src, dst):
    lv, visited, parent, curr_nd = float('inf'), {}, {}, src
    visited[curr_nd] = True
    current_distances = {item.value: lv if item.value != src else 0 for item in AP}  # O(n) operation
    while True:  # will run for at most O(n) times
        min_idx, min_v = 0, float('inf')
        for k, v in enumerate(adj_matrix[curr_nd]):  # edge relaxation  # O(k)
            if current_distances[k] > current_distances[curr_nd] + adj_matrix[curr_nd][k]:
                current_distances[k] = current_distances[curr_nd] + adj_matrix[curr_nd][k]
                parent[k] = curr_nd
            if v < min_v and k not in visited:
                min_idx, min_v = k, v

        curr_nd = min_idx
        visited[curr_nd] = True
        if len(visited) == len(current_distances):
            break
    path = reconstruct_path(parent, src, dst)
    print 'optimal path: ',
    print_path(path)
    print 'with cost: ',  current_distances[dst]
    return current_distances, parent


def reconstruct_path(parent, src, dst):
    """
    reconstruct the path, given the parents list. the idea is, starting from the destination, we check
    from which parent the destination was reached. then moving on to that node, we check it's parent again to
    find from where that node was reached. when this search reaches the source, the full path is found.
    :param parent:
    :param src:
    :param dst:
    :return:
    """
    l, dest = [], dst
    while dst != src:
        l.append(AP(parent[dst]))
        dst = parent[dst]
    revl = list(reversed(l))
    revl.append(AP(dest))
    return revl


def print_path(path):
    """
    print the human readable path, given the numericals
    :param path:
    :return:
    """
    for i in xrange(len(path) - 1):
        print path[i].name + '-->',
    print path[i + 1].name


#  main execution of the algorithm
if __name__ == "__main__":
    dijkastra_shortest_path(adj_mtx, source, destination)
