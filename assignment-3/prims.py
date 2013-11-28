# /usr/bin/python
# An implementation of prims algorithm

import os, random
from random import shuffle
import string
import networkx as nx
import time 

#A = adjacency matrix, u = vertex u
def adjacent(A, u):
    ''' Creates an adjacancy list of a given vertex '''
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x <> u:
            L.append(x)
    return L

#Q = min queue
def extractMin(Q):
    ''' Removes and returns the minimum value from the queue '''
    q = Q[0]
    Q.remove(Q[0])
    return q

#Q = min queue, V = vertex list
def decreaseKey(Q, K):
    ''' Maintains the minimum Queue '''
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

#V = vertex list, A = adjacency list, r = root
def prim(V, A, r):
    ''' A function to calculate the MST using prim's algorithm '''
    u = 0
    v = 0
    result =[]
    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=[None]*len(V)

    # initialize and set each value of the array K (key) to some large number (simulate infinity)
    K = [999999]*len(V)

    # initialize the min queue and fill it with all vertices in V
    Q=[0]*len(V)
    for u in range(len(Q)):
        Q[u] = V[u]

    # set the key of the root to 0
    K[r] = 0
    decreaseKey(Q, K)    # maintain the min queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        u = extractMin(Q)    # pop the first vertex off the min queue
        result.append(u)
        # loop through the vertices adjacent to u
        Adj = adjacent(A, u)
        for v in Adj:
            w = A[u][v]    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v) > 0 and w < K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                decreaseKey(Q, K)    # maintain the min queue
    return result

def random_adjacency_matrix(n):   
    matrix = [[random.randint(0, 1) for i in range(n)] for j in range(n)]

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    return matrix

if __name__ == "__main__":
    ''' Main function '''
    
    ''' This adjacency matrix is used only for demonstrating
    an example in the textbook '''
        #  a   b   c   d   e   f    g   h   i
    A = [ [0,  4,  0,  0,  0,  0,   0,  10,  0], # a
          [4,  0,  8,  0,  0,  0,   0, 11,  0], # b
          [0,  8,  0,  7,  0,  4,   0,  0,  2], # c
          [0,  0,  7,  0,  9, 14,   0,  0,  0], # d
          [0,  0,  0,  9,  0, 10,   0,  0,  0], # e
          [0,  0,  4, 14, 10,  0,   2,  0,  0], # f
          [0,  0,  0,  0,  0,  2,   0,  1,  6], # g
          [8, 11,  0,  0,  0,  0,   1,  0,  7], # h
          [0,  0,  2,  0,  0,  0,   6,  7,  0]] # i

    V = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]

    count=0
    vertices=100
    while count < 10:

        print vertices,
        vertex_list = []
        for i in range(vertices):
            vertex_list.append(i)

        matrix = random_adjacency_matrix(vertices)

        first_time = time.time()
        result = prim(vertex_list, matrix, 0)
#        print result
        print " " , (time.time() - first_time)
        count = count + 1
        vertices = vertices + 100
