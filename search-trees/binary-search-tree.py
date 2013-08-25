# /usr/bin/python
# An implementation of binary search tree

import os, random
import timeit
from random import shuffle
import string

class Node:
    def __init__(self, trainNumber, trainName, trainSource, trainDest):
        self.trainNumber = trainNumber
        self.trainName = trainName
        self.trainSource = trainSource
        self.trainDest = trainDest
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.trainNumber)

class TreeNode:
    def __init__(self):
        self.root = None

    def insertTrainNumberNode (self, trainNumber, trainName, trainSource, trainDest):
        ''' A function to insert Node based on train number'''

        if self.root == None: # if there is only root node
            self.root = Node(trainNumber, trainName, trainSource, trainDest)

        else:
            current = self.root

            while True:
                if trainNumber < current.trainNumber:
                    if current.left == None: # Reached the left most leaf node
                        current.left = Node(trainNumber, trainName, trainSource, trainDest) 
                        break
                    else:
                        current = current.left
                    
                elif trainNumber > current.trainNumber:
                    if current.right == None: # Reached the right most leaf node
                        current.right = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.right
                else:
                    break

    def insertTrainNameNode (self, trainNumber, trainName, trainSource, trainDest):
        ''' A function to insert Node based on the name of the train'''

        if self.root == None:
            self.root = Node(trainNumber, trainName, trainSource, trainDest)

        else:
            current = self.root

            while True:
                if trainName < current.trainName:
                    if current.left == None:
                        current.left = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.left
                    
                elif trainName > current.trainName:
                    if current.right == None:
                        current.right = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.right
                else:
                    break

    def insertTrainSourceNode (self, trainNumber, trainName, trainSource, trainDest):
        ''' A function to insert Node based on the source of the train'''

        if self.root == None:
            self.root = Node(trainNumber, trainName, trainSource, trainDest)

        else:
            current = self.root

            while True:
                if trainSource < current.trainSource:
                    if current.left == None:
                        current.left = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.left
                    
                elif trainSource > current.trainSource:
                    if current.right == None:
                        current.right = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.right
                else:
                    break

    def insertTrainDestinationNode (self, trainNumber, trainName, trainSource, trainDest):
        ''' A function to insert Node based on the destination of the train'''

        if self.root == None:
            self.root = Node(trainNumber, trainName, trainSource, trainDest)

        else:
            current = self.root

            while True:
                if trainDest < current.trainDest:
                    if current.left == None:
                        current.left = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.left
                    
                elif trainDest > current.trainDest:
                    if current.right == None:
                        current.right = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.right
                else:
                    break

    def bft(self, choice):
        ''' Performs Breadth first traversal '''

        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.level > current_level: 
                current_level += 1
                out.append("\n") # A newline is appended to the ouput list in-order to differntiate levels

            if choice == 1: 
                out.append(str(current_node.trainNumber) + " " )
                      
            if choice == 2: 
                out.append(str(current_node.trainName) + " " )

            if choice == 3:
                out.append(str(current_node.trainSource) + " " )

            if choice == 4:
                out.append(str(current_node.trainDest) + " " )

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print "".join(out)

    def bst(self, search, choice):
        ''' Performs binary search based on the choice '''

        current = self.root

        print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        print "+                 Search Results                      +"
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        print "Did you mean: " + str(search) + " ?"
        if choice == 1:
            while True:
                if search < current.trainNumber: # Traverse through the left subtree
                    if current.left == None:     # If there is no child node - Exit
                        break
                    else:
                        current = current.left
                    
                elif search > current.trainNumber:  # Traverse through the right subtree
                    if current.right == None:       # If there is no right child node - 
                        break
                    else:
                        current = current.right
                elif search == current.trainNumber:
                    print "Train Number: " + str(current.trainNumber) + "\n" + \
                            "Train Name: " + str(current.trainName) + "\n" + \
                            "Train Source: " + str(current.trainSource) + "\n" + \
                            "Train Destination: " + str(current.trainDest)
                    break
                else:
                    print "You've entered an invalid train number"
                    break


        if choice == 2:
            while True:
                if search < current.trainName:
                    if current.left == None:
                        break
                    else:
                        current = current.left
                    
                elif search > current.trainName:
                    if current.right == None:
                        break
                    else:
                        current = current.right
                elif search == current.trainName:
                    print "Train Number: " + str(current.trainNumber) + "\n" + \
                            "Train Name: " + str(current.trainName) + "\n" + \
                            "Train Source: " + str(current.trainSource) + "\n" + \
                            "Train Destination: " + str(current.trainDest)
                    break
                else:
                    print "You've entered an invalid train name"
                    break

        if choice == 3:
            while True:
                if search < current.trainSource:
                    if current.left == None:
                        break
                    else:
                        current = current.left
                    
                elif search > current.trainSource:
                    if current.right == None:
                        break
                    else:
                        current = current.right
                elif search == current.trainSource:
                    print "Train Number: " + str(current.trainNumber) + "\n" + \
                            "Train Name: " + str(current.trainName) + "\n" + \
                            "Train Source: " + str(current.trainSource) + "\n" + \
                            "Train Destination: " + str(current.trainDest)
                    break
                else:
                    print "You've entered an invalid train source"
                    break

        if choice == 4:
            while True:
                if search < current.trainDest:
                    if current.left == None:
                        break
                    else:
                        current = current.left
                    
                elif search > current.trainDest:
                    if current.right == None:
                        break
                    else:
                        current = current.right
                elif search == current.trainDest:
                    print "Train Number: " + str(current.trainNumber) + "\n" + \
                            "Train Name: " + str(current.trainName) + "\n" + \
                            "Train Source: " + str(current.trainSource) + "\n" + \
                            "Train Destination: " + str(current.trainDest)
                    break
                else:
                    print "You've entered an invalid train destination"
                    break

def stringGen (size = 20, chars = string.ascii_lowercase):
    ''' A function to generate strings for train name, source and destination '''
    return ''.join (random.choice(chars) for x in range(size))

if __name__=="__main__":
    ''' Main function '''

    tree = TreeNode()
    inp = []
    
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+                 Welcome to BST                      +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+           Generating 10^5 rand numbers              +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
   
    traintrainName = []
    trainSrc = []
    trainDest = []
    trainNumber = range(100000)   # Generates 10^5 random numbers
    for x in range(100000): traintrainName.append(stringGen())  # Generates 10^5 random train names
    for x in range(100000): trainSrc.append(stringGen())        # Generates 10^5 random train sources
    for x in range(100000): trainDest.append(stringGen())       # Generates 10^5 random train destination
    shuffle(trainNumber)    # Shuffles the random numbers generated
    inp = zip(trainNumber, traintrainName, trainSrc, trainDest) # Generates tuples from the random numbers

    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+         Inserting random numbers into tree          +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
   
    print "Select your way to inserting and searching the tree "
    print "1. Based on train number"
    print "2. Based on train name"
    print "3. Based on train source"
    print "4. Based on train destination"
    choice = int(raw_input("Enter your choice: "))
   
    for x in inp: # Traversing tuples from the whole list
        count = 0
        for y in x: # Traversing elements in a tuple
            if count == 0:      # Train number
                trainNumber = y
            elif count == 1:    # Train Name
                trainName = y
            elif count == 2:    # Train source
                trainSrc = y
            else:               # Train destination
                trainDest = y 
            count = count + 1

        if choice == 1:     # if based on train number
            tree.insertTrainNumberNode(trainNumber, trainName, trainSrc, trainDest)

        elif choice == 2:   # if based on train name
            tree.insertTrainNameNode(trainNumber, trainName, trainSrc, trainDest)

        elif choice == 3:   # if based on train source
            tree.insertTrainSourceNode(trainNumber, trainName, trainSrc, trainDest)

        elif choice == 4:   # if based on train destination
            tree.insertTrainDestinationNode(trainNumber, trainName, trainSrc, trainDest)

        else: 
            break

    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+                 Binary tree traversal               +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    tree.bft(choice)


    while True: 
        print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        print "+                     Binary search                   +"
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        if choice == 1: # Search based on train number
            search = int(raw_input("Enter the train number which you want to search: "))
            tree.bst(search, choice)

        elif choice == 2:   # Search based on train name
            search = raw_input("Enter the train name which you want to search: ")
            tree.bst(search, choice)

        elif choice == 3:   # Search based on train source
            search = raw_input("Enter the train source which you want to search: ")
            tree.bst(search, choice)
    
        elif choice == 4:   # Search based on train destination
            search = raw_input("Enter the train destination which you want to search: ")
            tree.bst(search, choice)
      
        
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        again = raw_input("Would you like to search again [y/n]? ")
        if again == 'y' or again == 'Y':
            continue
        elif again == 'n' or again == 'N':
            print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
            print "+                     Thank you!!                     +"
            print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
            break
        else:
            print "Invalid input. Program is going to exit!"
            print "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
            print "+                     Thank you!!                     +"
            print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
            break

