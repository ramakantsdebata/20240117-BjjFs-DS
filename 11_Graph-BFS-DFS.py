# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def bfs(self, s):

#     def dfs(self, s):


# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('B', 'E')
# g.add_edge('C', 'F')

# print("BFS traversal starting from vertex 'A':")
# g.bfs('0')

# print("\nDFS traversal starting from vertex 'A':")
# g.dfs('0')


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, s):
        visited = [False] * len(self.graph)
        queue = [s]
        visited[s] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

    def dfs(self, s):
        visited = [False] * len(self.graph)
        stack = [s]

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                print(vertex, end=" ")
                visited[vertex] = True

                if vertex in self.graph:
                    for neighbor in self.graph[vertex]:
                        if not visited[neighbor]:
                            stack.append(neighbor)

# Usage example
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("BFS traversal starting from vertex 0:")
g.bfs(0)

print("\nDFS traversal starting from vertex 0:")
g.dfs(0)
