class Stack :
    def __init__(self):
        self.s = []
        pass
    def push(self, a):
        self.s.append(a)
    def pop(self):
        if self.s:
            a = self.s.pop()
            return a
        else :
            print("Stack already Empty")
    def peek(self):
        if self.s :
            a = self.s.pop()
            self.s.append(a)
            return a
        else :
            print("Top of Stack Empty")
    def display(self):
        print(self.s)
        
def main():
    s = Stack()
    a = 0
    while(a != 5):
        print("Menu\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\n")
        a = int(input("Enter Choice : "))
        if a == 1 :
            b = int(input("Element to be pushed : "))
            s.push(b)
        elif a == 2 :
            print(f"{s.pop()} was removed from Stack")
        elif a == 3 :
            print(f"{s.peek()} is at top of Stack")
        elif a == 4 :
            print("Stack -->\n")
            s.display()
        elif a == 5 :
            print("Exit")
        else :
            print("Try Again")

if __name__ == '__main__':
    main()