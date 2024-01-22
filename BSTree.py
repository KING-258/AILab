class BST :
    def __init__(self, data) :
        self.data = data 
        self.lchild = None 
        self.rchild = None 
    def AddNode(self, value) :
        if value < self.data :
            if self.lchild :
                self.lchild.AddNode(value)
            else:
                self.lchild = BST(value)
        elif value > self.data :
            if self.rchild :
                self.rchild.AddNode(value)
            else :
                self.rchild = BST(value)
        else :
            print("Duplicates Not Allowed")
            return
            
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
    a = int(input("Enter Value for Root Node : "))
    bstree = BST(a)
    while a != -1 :
        a = int(input("Enter Value for Next Nodes (Input -1 to Exit): "))
        if a == -1 :
            bstree.Traversal(bstree)
        else :
            bstree.AddNode(a)

if __name__ == '__main__' :
    main()