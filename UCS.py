class Graph:
    def __init__(self, v):
        self.vertices = v
        self.adj_list = {v: {} for v in range(self.vertices)}
    def movement(self, v1, v2, w):
        self.adj_list[v1][v2] = w
    def printlist(self):
        for i in self.adj_list:
            print(i, end='-->')
            print(self.adj_list[i])
    def ucs(self, start, goal):
        v = set()
        q = [(0, start, [])]
        while q:
            cost, curr, path = q.pop(0)
            if curr not in v:
                v.add(curr)
                path = path + [curr]
                if curr == goal:
                    return path, cost
                for neighbor, weight in self.adj_list[curr].items():
                    if neighbor not in v:
                        total_cost = cost + weight
                        q.append((total_cost, neighbor, path))
                q = sorted(q, key=lambda x: x[0])
        return None

def main():
    a = int(input("Enter the Number of Vertices : "))
    g = Graph(a)
    b = 0
    while b != -1:
        c = int(input("Vertice 1 : "))
        d = int(input("Vertice 2 : "))
        e = int(input("Weight for Movement : "))
        if c == d == -1 :
            b = -1
        else :
            g.movement(c, d, e)
    s = int(input("Enter Starting Vertex : "))
    e = int(input("Enter Goal Vertex : "))
    m = g.ucs(s, e)
    print(m)
    g.printlist()

if __name__ == '__main__':
    main()