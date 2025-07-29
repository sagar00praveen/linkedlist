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

    def dbv(self, val):
        if not self.head:
            print("List is empty. Cannot delete.")
            return
        temp = self.head
        while temp:
            if temp.data == val:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Deleted: {val}")
                return
            temp = temp.next
        print(f"Value {val} not found in list.")

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

d = int(input("\nHow many times do you want to perform delete operation? "))
for i in range(d):
    val = int(input("Enter value to delete: "))
    dll.dbv(val)
    dll.display()
