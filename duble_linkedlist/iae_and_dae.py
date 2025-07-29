class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

    def dae(self):
        if not self.head:
            print("Cannot delete from an empty list...")
            return
        if not self.head.next:
            print(f"Deleted: {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print(f"Deleted: {temp.data}")
        temp.prev.next = None

    def display(self):
        temp = self.head
        print("Doubly linked list:")
        while temp:
            print(temp.data, end="<-->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iae(val)

dll.display()

d = int(input("\nHow many times do you want to delete from end? "))
for i in range(d):
    dll.dae()

dll.display()
