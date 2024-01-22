class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v : [] for v in range(self.vertices)}
    def movement(self, v1, v2):
        self.adj_list[v1].append(v2)
    def printlist(self):
        for i in self.adj_list:
            print(i, end='-->')
            print(sorted(self.adj_list[i]))
    def traverse(self, firstindex):
        visited = set()
        dfs = []
        self.DFS(firstindex, visited, dfs)
        return dfs
    def DFS(self, current, visited, dfs):
        visited.add(current)
        dfs.append(current)
        for i in sorted(self.adj_list[current]):
            if i not in visited :
                self.DFS(i, visited, dfs)

if __name__ == '__main__':
    a = int(input("Enter  Number of Vertices : "))
    g = Graph(a)
    print("Directed UnWeighted Graph---->\n")
    for i in range(a):
        b = int(input(f"Out Degree for {i} : "))
        for j in range(b):
            c = int(input(f"Entry Number {j+1} for {i} : "))
            g.movement(i, c)
    g.printlist()
    d = int(input("Starting Vertex for DFS Traversal : "))
    DFS = g.traverse(d)
    print(f"DFS Traversal---->\n{DFS}")