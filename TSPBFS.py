class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v: [] for v in range(self.vertices)}

    def movement(self, v1, v2, w):
        self.adj_list[v1].append((v2, w))

    def tsp_bfs(self, start):
        num_vertices = self.vertices
        queue = [(start, [start], 0)]
        min_cost = float('inf')
        min_path = []

        while queue:
            current_node, path, cost = queue.pop(0)

            if len(path) == num_vertices:  # Reached all vertices
                cost += self.adj_list[current_node][0][1]  # Add cost to return to start
                if cost < min_cost:
                    min_cost = cost
                    min_path = path + [start]
            else:
                for neighbor, weight in self.adj_list[current_node]:
                    if neighbor not in path:
                        new_cost = cost + weight
                        if new_cost < min_cost:  # Pruning branches
                            queue.append((neighbor, path + [neighbor], new_cost))

        return min_path, min_cost
    def printlist(self):
            print("Adjacency List:")
            for vertex in self.adj_list:
                neighbors = sorted(self.adj_list[vertex])
                print(f"{vertex} --> {', '.join(map(str, neighbors))}")
# Example usage:
v = int(input("Enter the number of vertices: "))
g = Graph(v)

edges = int(input("Enter the number of edges: "))
print("Enter the edges and weights (vertex1 vertex2 weight):")
for _ in range(edges):
    v1, v2, w = map(int, input().split())
    g.movement(v1, v2, w)

print("Graph created successfully!")
g.printlist()

start_vertex = int(input("Enter the starting vertex: "))
optimal_path, min_cost = g.tsp_bfs(start_vertex)
print("Optimal path:", optimal_path)
print("Minimum cost:", min_cost)
