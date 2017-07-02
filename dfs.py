adj_lst = {
            1: [3, 6],
            2: [4, 7],
            3: [1, 5, 7],
            4: [2, 6],
            5: [3, 7],
            6: [1, 4],
            7: [2, 3, 5]
           }

def dfs(vtx, visited):
	"""
	Depth First Search:

	Traverses the graph in a depth first fashion. In this case, the graph is represented by an adjacency list. 
	
	:param vtx: vertex 

	:return a visited set
	"""
	visited.append(vtx)
	for item in adj_lst[vtx]:
		if item not in visited:
			dfs(item, visited)		

s = []
dfs(1, s)
print s

# here it's space efficient than bfs because we are using one less data structure 