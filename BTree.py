class Node:
    def __init__(self, a):
        self.data = a
        self.lchild = None
        self.rchild = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    def Create(self):
        data = int(input("Data for Node : "))
        if data == -1:
            return None 
        else :
            n = Node(data)
            print(f"Left of {data} Node : ")
            n.lchild = self.Create()
            print(f"Right of {data} Node : ")
            n.rchild = self.Create()
            return n
    def Traversal(self, node):
        print("InOrder Traversal ---->")
        self.InOrder(node)
        print("PreOrder Traversal ---->")
        self.PreOrder(node)
        print("PostOrder Traversal ---->")
        self.PostOrder(node)
    def InOrder(self, node):
        if node != None:
            self.InOrder(node.lchild)
            print(f"{node.data}-")
            self.InOrder(node.rchild)
    def PreOrder(self, node):
        if node != None:
            print(f"{node.data}-")
            self.PreOrder(node.lchild)
            self.PreOrder(node.rchild)
    def PostOrder(self, node):
        if node != None:
            self.PostOrder(node.lchild)
            self.PostOrder(node.rchild)
            print(f"{node.data}-")

def main():
    tree = BinaryTree()
    parent = tree.Create()
    tree.Traversal(parent)

if __name__ == '__main__':
    main()