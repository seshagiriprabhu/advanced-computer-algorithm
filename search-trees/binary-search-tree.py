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
        self.trainSrc = trainSource
        self.trainDest = trainDest
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.trainNumber)

class TreeNode:
    def __init__(self):
        self.root = None

    def insertNode (self, trainNumber, trainName, trainSource, trainDest):
        ''' A function to insert Node '''

        if self.root == None:
            self.root = Node(trainNumber, trainName, trainSource, trainDest)

        else:
            current = self.root

            while True:
                if trainNumber < current.trainNumber:
                    if current.left == None:
                        current.left = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.left
                    
                elif trainNumber > current.trainNumber:
                    if current.right == None:
                        current.right = Node(trainNumber, trainName, trainSource, trainDest)
                        break
                    else:
                        current = current.right
                else:
                    break

    def bft_trainNumber(self):
        ''' Performs BFT actions '''

        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.trainNumber) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print "".join(out)

def stringGen (size = 20, chars = string.ascii_uppercase):
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
    trainNumber = range(100000)
    for x in range(100000): traintrainName.append(stringGen())
    for x in range(100000): trainSrc.append(stringGen())
    for x in range(100000): trainDest.append(stringGen())
    shuffle(trainNumber)
    inp = zip(trainNumber, traintrainName, trainSrc, trainDest)

    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+         Inserting random numbers into tree          +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    
    for x in inp:
        count = 0
        for y in x:
            if count == 0:
                trainNumber = y
            elif count == 1:
                traintrainName = y
            elif count == 2:
                trainSrc = y
            else:
                trainDest = y
            count = count + 1
        tree.insertNode(trainNumber, traintrainName, trainSrc, trainDest)

    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "+                 Binary tree traversal               +"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"

    tree.bft_trainNumber()
    
