
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


    """def iap(self, data, pos):
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

        temp.next = new_node"""

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

