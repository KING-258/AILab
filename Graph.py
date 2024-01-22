class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v : [] for v in range(self.vertices)}
    def movement1(self, v1, v2):
        self.adj_list[v1].append(v2)  #Directed UnWeighted Graph
    def movement2(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  #UnDirected UnWeighted Graph
    def movement3(self, v1, v2, w):
        string = f"{v1}, {w}"
        self.adj_list[v1].append(string)  #Directed Weighted Graph
    def movement4(self, v1, v2, w):
        string = f"{v1}, {w}"
        self.adj_list[v1].append(string)
        string = f"{v2}, {w}"
        self.adj_list[v2].append(string)  #UnDirected Weighted Graph
    def printlist(self):
        for i in self.adj_list:
            print(i, end='-->')
            print(self.adj_list[i])
if __name__ == '__main__':
    a = int(input("Enter  Number of Vertices : "))
    g = Graph(a)
    print("Menu\n1.DirectedUnweightedGraph\n2.UndirectedUnweightedGraph\n3.DirectedWeightedGraph\n4.UndirectedWeightedGraph\n")
    b = int(input("Enter Choice : "))
    if(b == 1):
        print("Directed UnWeighted Graph---->\n")
        for i in range(a):
            c = int(input(f"Out Degree for {i} : "))
            for j in range(c):
                d = int(input(f"Entry Number {j+1} for {i} : "))
                g.movement1(i, d)
    elif(b == 2):
        print("UnDirected UnWeighted Graph---->\n")
        for i in range(a):
            c = int(input(f"Out Degree for {i} : "))
            for j in range(c):
                d = int(input(f"Entry Number {j+1} for {i} : "))
                g.movement2(i, d)
    elif(b == 3):
        print("Directed Weighted Graph---->\n")
        for i in range(a):
            c = int(input(f"Out Degree for {i} : "))
            for j in range(c):
                d = int(input(f"Entry Number {j+1} for {i} : "))
                e = int(input("Weight for Movement : "))
                g.movement3(i, d, e)
    elif(b == 4):
        print("UnDirected Weighted Graph---->\n")
        for i in range(a):
            c = int(input(f"Out Degree for {i} : "))
            for j in range(c):
                d = int(input(f"Entry Number {j+1} for {i} : "))
                e = int(input("Weight for Movement : "))
                g.movement4(i, d, e)
    print("Adjacency List---->")
    g.printlist()