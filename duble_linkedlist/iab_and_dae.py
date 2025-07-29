
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def iab(self,data):
        newnode=Node(data)
        newnode.next=self.head
        if self.head:
            self.head.prev=newnode
        self.head=newnode
    def dae(self):
        if not self.head:
            print("cant perform delet in an empty")
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        print(f"Deleted :{temp.data}")
        if temp.prev:
            temp.prev.next=None
        else:
            self.head=None
            

    def backtraverse(self):
        print("values for traversing backward....")
        temp=self.head
        if not temp:
            print("empty list")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end="<-->")
            temp = temp.prev
        print("None")    


   

    def display(self):
        temp=self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp=temp.next
        print("None")

dll=DoublyLinkedList()
n= int(input("Enter the number of elements to insert at begin: "))
for i in range(n):
    val=int(input(f"Enter element {i + 1}: "))
    dll.iab(val)
dll.display()

dll.backtraverse()

