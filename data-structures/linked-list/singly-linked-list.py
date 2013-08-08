# /usr/bin/python
# An implementation of linked list

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = self.tail = None

    def addFirstNode(self, newNode):
        ''' A function to add the first node to the list'''

        self.head = self.tail = newNode

    def addNodeTail(self,  data):
        ''' Function to add an element to the tail of the list '''

        newNode = ListNode(data)

        # Empty list
        if self.head == None:
            self.addFirstNode(newNode)
    
        # Non-empty list
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.tail.next = None

    def addNodeHead(self, data): 
        '''Function to add an element to the head of the list '''

        newNode = ListNode(data)
        
        # Empty list
        if self.head == None:
            self.addFirstNode(newNode)
        
        # Non-empty list
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
    

    def delFirstNode(self):
        ''' Function to delete the single node '''

        self.head = self.tail = None

    def delNodeTail(self):
        ''' Function to delete an element from the list '''

        node = self.head

        # Empty list
        if self.head == None:
            print "List is empty"
            return 

        # Single node list
        elif self.head == self.tail:
            self.delFirstNode()
            return 

        # Multiple node list
        else:
            while node.next.next != None:
                node = node.next
            node.next = None
            self.tail = node

    def delNodeHead(self):
        ''' Function to delete a node from head '''

        node = self.head

        # Empty list
        if self.head == None:
            print "List is empty"
            return

        # Single node list
        if self.head == self.tail:
            self.delFirstNode()
            return    
        
        # Multi-node list
        if self.head != self.tail:
            node = node.next
            self.head = node
            return


    def delNode(self, element):
        ''' Function to delete a user specified given node '''

        node = self.head
        found = False
    
        # If there's only one node and it doesn't contain the given element
        if self.head == self.tail and self.head.data != element:
            print "Element not found in the list"
            return
        
        # If the head node contains the element
        if self.head.data == element:
            self.delNodeHead()
            return
        
        # To check if the node is in the rest of the list
        while node.next != None:
            if node.next.data == element:
                found = True
                break
      
            else:
                node = node.next

        # If node was found
        if found:
            if node.next.next != None:
                node.next = node.next.next

            else:
                self.delNodeTail()

        # If the element was not found in the list
        else:
            print "Element not found in the list"
      
def display(list):
    ''' Function to display the linked list '''

    print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    node = list.head
    if list.head == None:
        print "List is empty! Fill something in the list in-order to delete"
        print "Head -> None <- Tail",

    else:
        print "Head -> ",
        while node is not None:
            print " %d " % (node.data),
            node = node.next 
            if node is not None:
                print "->",
        print " <- Tail",
    print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"


if __name__ == "__main__":
    ''' Main function '''

    list = List()
    while True:
        print "+-+-+-+-+-+-+-+-+-Singly Linked list+-+-+-+-+-+-+-+-+-+"
        print "+ 1. Add a node to the tail                           +"
        print "+ 2. Add a node to the head                           +"
        print "+ 3. Remove a node from tail                          +"
        print "+ 4. Remove a node from head                          +"
        print "+ 5. Remove a node                                    +"
        print "+ 6. Exit                                             +"
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        s = int(raw_input('Enter your Choice: '))
        if s == 1:
            inp = int(raw_input('Enter the element you want to insert to the tail: '))
            list.addNodeTail(inp)
            display(list)

        elif s==2:
            inp = int(raw_input('Enter the element you want to insert to the head: '))
            list.addNodeHead(inp)
            display(list)

        elif s==3:   
            list.delNodeTail()
            display(list)
            
        elif s==4:
            list.delNodeHead()
            display(list)

        elif s==5:
            inp = int(raw_input('Enter the element you want to delete from the list: '))
            list.delNode(inp)
            display(list)

        elif s==6:
            break;

        else:
            print "Invalid input"
