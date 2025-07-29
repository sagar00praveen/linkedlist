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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
n = int(input("enter nuber of elenents"))
for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    dll.iab(val)

dll.display()
