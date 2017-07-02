q = [1]
adj_lst = {
            1: [3, 6],
            2: [4, 7],
            3: [1, 5, 7],
            4: [2, 6],
            5: [3, 7],
            6: [1, 4],
            7: [2, 3, 5]
           }


def bfs(q, adj_lst):	
	"""
	Breadth First Search:

	visit all the connected vertices of a graph represented by an adjacency list.

	:param q: a data structure to hold the neighbors, should be an actual queue that supports O(1) insertion and deletion
	:param adj_lst: representation of graph, in this case as an adjacency list. 

	:return seen: vertices visited in breadth first search order. 
	"""
	seen = []
	while q:
		vertex = q[0]
		if vertex not in seen:
			seen.append(vertex)
		for item in adj_lst[vertex]:
			if item not in seen:
				q.append(item)
				seen.append(item)
		del q[0]	
	return seen					


print bfs(q, adj_lst)

