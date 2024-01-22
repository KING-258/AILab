class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
class LL :
    def __init__(self):
        self.head = None
    def AddB(self):
        a = int(input("Enter Value of Data for Node : "))
        n = Node(a)
        if self.head == None :
            self.head = n
        else :
            n.next = self.head
            self.head = n
    def AddE(self):
        a = int(imput("enter Value of Data for Node : "))
        n = Node(a)
        if self.head == None :
            self.head = n
        else :
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = n
    def RemoveB(self):
        if self.head == None :
            print("LL is Empty")
        else :
            a = self.head.data
            self.head = self.head.next
            print(f"{a} was Removed from LL")
    def RemoveE(self):
        if self.head == None :
            print("LL is Empty")
        else :
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            a = temp.next.data
            temp.next = None
            print(f"{a} was Removed from LL")
    def Display(self):
        if self.head == None:
            print("LL is Empty")
        else :
            temp = self.head
            string = ""
            while temp != None:
                string += f"{temp.data}-->"
                temp = temp.next
            string += "NULL"
            print(string)
def main():
    ll = LL()
    a = 0
    while a != 6:
        print("Menu\n1.AddB()\n2.RemoveB()\n3.AddE()\n4.RemoveE()\n5.Display()\n6.Exit()\n")
        a = int(input("Enter Choice : "))
        if a == 1:
            ll.AddB()
        elif a == 2:
            ll.RemoveB()
        elif a == 3:
            ll.AddE()
        elif a == 4:
            ll.RemoveE()
        elif a == 5:
            ll.Display()
        elif a == 6:
            print("***Exit***")
        else :
            print("Try Again")
if __name__ == '__main__':
    main()