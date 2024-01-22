class Queue:
    def __init__(self):
        self.q = []
        pass
    def enqueue(self, a):
        self.q.append(a)
    def dequeue(self):
        if self.q :
            return self.q.pop(0)
        else :
            print("Nothing in Queue")
    def display(self):
        print(self.q)

def main():
    q1 = Queue()
    a = 0
    while a != 4:
        print("Menu\n1.Enqueue()\n2.Dequeue()\n3.Display()\n4.Exit()\n")
        a = int(input("Enter Choice : "))
        if a == 1:
            b = int(input("Enter Element to Add : "))
            q1.enqueue(b)
        elif a == 2:
            print(f"{q1.dequeue()} was Removed from Queue")
        elif a == 3:
            print("Queue -->")
            q1.display()
        elif a == 4:
            print("!!!EXIT!!!")
        else :
            print("Try Again")

if __name__ == '__main__':
    main()