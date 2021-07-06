# linkedIn: https://www.linkedin.com/in/nirajpatel007

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    # Print Linked List..............................................................................................

    def printLinkedList(self):
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
            
    # Insertion of Data.................................................................................................
    
    def insertAtBeginning(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            print("Inserted: ", data, "\n")
        else:
            tempHead = self.head
            self.head = node
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
            print("Inserted: ", data, "\n")

    def insertAfterGivenNode(self, data, nodeData):
        node = Node(data)
        flag=0
        if self.head==None:
            print("Insert Operation Failed as Given Node is Not Present")
        else:
            tempHead = self.head
            while tempHead:
                if tempHead.data == nodeData:
                    remainingLinkedList = tempHead.next
                    tempHead.next = node
                    tempHead.next.next = remainingLinkedList
                    print("Inserted: ", data, "\n")
                    flag=1
                    break
                else:
                    tempHead = tempHead.next
            if flag==0:
                print("Insert Operation Failed as Given Node is Not Present\n")

    # Deletion of Data ..................................................................................................

    def deleteFromBeginning(self):
        if self.head==None:
            print("Linked List is Empty\n")
        else:
            temp = self.head.data
            self.head = self.head.next
            print("Deleted: ", temp, "\n")

    def deleteFromEnd(self):
        if self.head == None:
            print("Linked List is Empty\n")
        elif self.head.next == None:
            temp = self.head.data
            self.head = None
            print("Deleted: ", temp, "\n")
        else:
            tempHead = self.head
            while tempHead.next.next:
                tempHead = tempHead.next
            temp = tempHead.next.data
            tempHead.next = None
            print("Deleted: ", temp, "\n")

    def deleteSpecificData(self, data):
        if self.head == None:
            print("Linked List is Empty\n")
        elif self.head.data == data:
            temp = self.head.data
            self.head = self.head.next
            print("Deleted: ", temp, "\n")
        else:
            tempHead = self.head
            while tempHead.next.data!=data:
                tempHead = tempHead.next
            tempData = tempHead.next.data
            nextTemp = tempHead.next.next
            tempHead.next = nextTemp
            print("Deleted: ", tempData, "\n")
                
    
                    
# Creating LinkedList Object
ll = singlyLinkedList()

#I nserting Data
ll.insertAtEnd(11)
ll.insertAtEnd(1)
ll.insertAtEnd(3)
ll.insertAtBeginning(5)
ll.insertAfterGivenNode(15, 3)

ll.printLinkedList()

# Deleting Data
ll.deleteSpecificData(15)
ll.deleteFromBeginning()
ll.printLinkedList()



                
