
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def iae(self,data):
        

    def iap(self, data, pos):
        new_node = Node(data)

        if pos <= 0:
            print("Invalid position")
            return

        
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        print("Double Linked List : ")
        while temp:
            print(temp.data, end="<--")
            temp = temp.next
        print(None)

dll = DoubleLinkedList()

dll.iap(100, 1) 

n = int(input("Enter the number of elements to insert at specific positions: "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    pos = int(input(f"Enter the position value for element {i+1}: "))
    dll.iap(value, pos)

dll.display()

