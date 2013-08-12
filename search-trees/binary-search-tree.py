# /usr/bin/python
# An implementation of binary search tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

class TreeNode:
    def __init__(self):
        self.root = None

    def insertNode (self, data):
        ''' A function to insert Node '''

        if self.root == None:
            self.root = Node(data)

        else:
            current = self.root

            while True:
                if value < current.data:
                    if current.left == None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                    
                elif value > current.data:
                    if current.right == None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
                else:
                    break
   

    def deleteNode (self):
        ''' A function to delete a node '''

    

if __name__=="__main__":
    ''' Main function '''

    tree = TreeNode()
    inp = []
    
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+                 Binary Search Tree                  +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"

    s = int(raw_input('How many nodes would you like to insert: '))

    for x in range(s):
        inp.append(int(raw_input('Ener the element #' +`x+1` + ': ')))
    

    tree.insertNode(inp)
    
    
