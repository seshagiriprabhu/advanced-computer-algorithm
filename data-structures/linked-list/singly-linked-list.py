# /usr/bin/python
# An implementation of linked list

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirstNode(self, newNode):
        ''' A function to add the first node to the list'''

        self.head = newNode
        self.tail = newNode

    def addNodeTail(self,  data):
        ''' Function to add an element to the tail of the list '''

        newNode = ListNode(data)

        if self.head == None:
            self.addFirstNode(newNode)

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.tail.next = None

    def addNodeHead(self, data): 
        '''Function to add an element to the head of the list '''

        newNode = ListNode(data)

        if self.head == None:
            self.addFirstNode(newNode)

        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
    

    def delFirstNode (self):
        ''' Function to delete the single node '''

        self.head = None
        self.tail = None

    def delNodeTail(self):
        ''' Function to delete an element from the list '''

        node = self.head
        if self.head == None:
            print "List is empty"
            return 

        elif self.head == self.tail:
            self.delFirstNode()
            return 

        else:
            while node.next.next != None:
                node = node.next
            node.next = None
            self.tail = node

    def delNodeHead (self):
        ''' Function to delete a node from head '''

        node = self.head

        if self.head == None:
            print "List is empty"
            return

        if self.head == self.tail:
            self.delFirstNode()
            return    
        
        if self.head != self.tail:
            node = node.next
            self.head = node
            return


    def delNode(self, element):
        ''' Function to delete a user specified given node '''

        node = self.head
        found = False
       
        if self.head == self.tail and self.head.data != element:
            print "Element not found in the list"
            return
        
        if self.head.data == element:
            self.delNodeHead(element)
            return
        
        while node.next != None:
            if node.next.data == element:
                found = True
                break
      
            else:
                node = node.next

        # If node found
        if found:
            if node.next.next != None:
                node.next = node.next.next

            else:
                self.delNodeTail()

        else:
            print "Element not found in the list"
      
def display(list):
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
