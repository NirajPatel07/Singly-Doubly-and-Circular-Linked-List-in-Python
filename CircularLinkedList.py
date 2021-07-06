# linkedIn: https://www.linkedin.com/in/nirajpatel007

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtLast(self, data):
        node = Node(data)
        node.next = self.head
        if self.head==None:
            node.next = node
            self.head =node
            print(data, "Inserted.\n")
        else:
            
            temp = self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next = node
            print(data, "Inserted.\n")
            

    def insertAtBeginning(self, data):
        node = Node(data)
        if self.head==None:
            node.next = node
            self.head= node
            print(data, "Inserted.\n")
        else:
            temp = self.head
            node.next = self.head
            
            while temp.next != self.head:
                temp = temp.next
            self.head = node
            temp.next = self.head
            print(data, "Inserted.\n")
            

    def printCircularLinkedList(self):
        if self.head == None:
            print("Linked List is Empty.")
        else:
            temp = self.head
            while True:
                if temp.next!=self.head:
                    print(temp.data, end = "-->")
                else:
                    print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
            print()

cll = circularLinkedList()
cll.insertAtBeginning(23)
cll.insertAtBeginning(14)
cll.insertAtLast(5)
cll.insertAtLast(1)
cll.insertAtLast(9)
cll.insertAtLast(2)
cll.insertAtLast(3)
cll.insertAtBeginning(13)
cll.insertAtBeginning(132)
cll.insertAtLast(88)
cll.printCircularLinkedList()
