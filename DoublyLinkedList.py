# linkedIn: https://www.linkedin.com/in/nirajpatel007

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head == None:
            print( "Linked List is Empty.\n" )
        else:
            tempHead = self.head
            print("Linked List is:")
            while tempHead:
                if tempHead.next:
                    print(tempHead.data, end = " --> ")
                else:
                    print(tempHead.data)
                tempHead = tempHead.next
            print()

    def printListReverse(self):
        if self.head == None:
            print( "Linked List is Empty.\n" )
        else:
            tempHead = self.head
            print("Linked List is:")
            while tempHead.next != None:
                tempHead = tempHead.next
            while tempHead:
                if tempHead.prev:
                    print(tempHead.data, end = " --> ")
                else:
                    print(tempHead.data)
                tempHead = tempHead.prev
            print()

    def insertAtBeginning(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            print("Inserted: ", data, "\n")
        else:
            tempHead = self.head
            self.head = node
            tempHead.prev = self.head
            self.head.next = tempHead
            print("Inserted: ", data, "\n")

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            print("Inserted: ", data, "\n")
        else:
            tempHead = self.head
            while tempHead.next:
                tempHead = tempHead.next
            tempHead.next = node
            node.prev = tempHead
            print("Inserted: ", data, "\n")

    def insertAfterGivenNode(self, data, nodeData):
        node = Node(data)
        if self.head==None:
            self.head = node
            print("Inserted: ", data, "\n")
        else:
            tempHead = self.head
            while tempHead:
                if tempHead.data == nodeData:
                    remainingLinkedList = tempHead.next
                    tempHead.next = node
                    node.prev = tempHead
                    tempHead.next.next = remainingLinkedList
                    if remainingLinkedList:
                        remainingLinkedList.prev =  node
                    print("Inserted: ", data, "\n")
                    flag=1
                    break
                else:
                    tempHead = tempHead.next
            if flag==0:
                print("Insert Operation Failed as Given Node is Not Present\n")
            
    def deleteAtBegin(self):
        if self.head == None:
            print("Linked List is Empty.")
        elif self.head.next == None:
            temp = self.head.data
            self.head = None
            print("Deleted: ", temp, "\n")
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            print("Deleted: ", temp, "\n")
        

    def deleteAtEnd(self):
        if self.head == None:
            print("Linked List is Empty.")
        elif self.head.next == None:
            temp = self.head.data
            self.head = None
            print("Deleted: ", temp, "\n")
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            tempData = temp.data
            temp.prev.next = None
            print("Deleted: ", tempData, "\n")
    
    def deleteNodeByValue(self, data):
        if self.head == None:
            print("Linked List is Empty")
        elif self.head.next == None:
            if self.head.data == data:
                self.head = None
                print("Deleted: ", data, "\n")
            else:
                print("Data Not Present.\n")
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            print("Deleted: ", data, "\n")
        else:
            tempHead = self.head
            while tempHead.next:
                if tempHead.data==data:
                    break
                tempHead = tempHead.next
            if tempHead.next:
                tempHead.next.prev = tempHead.prev
                tempHead.prev.next = tempHead.next
                print("Deleted: ", data, "\n")
            else:
                if tempHead.data == data:
                    tempHead.prev.next = None
                    print("Deleted: ", data, "\n")
                else:
                    print("Data Not Present")
                    
            
            
            
        
    
dll = doublyLinkedList()
dll.insertAtBeginning(5)
dll.deleteAtEnd()
dll.insertAtBeginning(8)
dll.insertAtBeginning(9)
dll.insertAtEnd(13)
dll.insertAtEnd(17)
dll.insertAtEnd(19)
dll.printList()
dll.insertAfterGivenNode(44, 9)
dll.printList()

dll.deleteNodeByValue(19)
dll.printList()
dll.printListReverse()



















            
