from Q import Queue as Queue
class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v: [] for v in range(self.vertices)}
    def movement(self, v1, v2):
        self.adj_list[v1].append(v2)
    def printlist(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            neighbors = sorted(self.adj_list[vertex])
            print(f"{vertex} --> {', '.join(map(str, neighbors))}")
    def bfs_traversal(self, start_vertex):
        visited = set()
        queue = Queue()
        traversal_result = []
        visited.add(start_vertex)
        queue.enqueue(start_vertex)
        while not queue.is_empty():
            current_vertex = queue.dequeue()
            traversal_result.append(current_vertex)
            for neighbor in self.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return traversal_result
        
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
    start_vertex_bfs = int(input("\nEnter the starting vertex for BFS traversal: "))
    bfs_result = graph.bfs_traversal(start_vertex_bfs)
    print("\nBFS Traversal:", bfs_result)