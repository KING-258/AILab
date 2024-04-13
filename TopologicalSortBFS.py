class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v: [] for v in range(self.vertices)}
    def movement(self, v1, v2):
        self.adj_list[v1].append(v2)
    def topological_sort(self):
        in_degree = {v: 0 for v in range(self.vertices)}
        for node in self.adj_list:
            for neighbor in self.adj_list[node]:
                in_degree[neighbor] += 1
        queue = [node for node in self.adj_list if in_degree[node] == 0]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) != self.vertices:
            return None
        else:
            return result
    def printlist(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            neighbors = sorted(self.adj_list[vertex])
            print(f"{vertex} --> {', '.join(map(str, neighbors))}")
if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices: "))
    graph = Graph(num_vertices)
    print("\nDirected Unweighted Graph:")
    for vertex in range(num_vertices):
        out_degree = int(input(f"Out Degree for Vertex {vertex}: "))
        for _ in range(out_degree):
            entry = int(input(f"Enter neighbor for Vertex {vertex}: "))
            graph.movement(vertex, entry)
    graph.printlist()
    topo = graph.topological_sort()
    print(f"Topological Sort for the Graph : {topo}")