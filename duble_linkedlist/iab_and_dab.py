class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iab(self, data):
        newnode = Node(data)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
        self.head = newnode

    def dab(self):
        if not self.head:
            print("Cannot perform delete in an empty list...")
            return
        print(f"Deleted: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def display(self):
        temp = self.head
        print("Doubly linked list:")
        while temp:
            print(temp.data, end="<-->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iab(val)

dll.display()

d = int(input("\nHow many times do you want to delete from beginning? "))
for i in range(d):
    dll.dab()

dll.display()
