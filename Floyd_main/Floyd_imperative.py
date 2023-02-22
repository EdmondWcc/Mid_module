import time
import sys
import itertools

NO_PATH =  sys.maxsize #no path available
graph = [
            [0, 3, 5, 2],
            [float('inf'), 0, 1, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
#graph = [[0,   7,  NO_PATH, 8], [NO_PATH,  0,  5,  NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]] # define the given graph
MAX_LENGTH = len(graph[0]) # the no. of node

def floyd(distance): 
#A simple implementation of Floyd's algorithm 

    for intermediate, start_node,end_node in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)): 
    # Assume that if start_node and end_node are the same 
    # then the distance would be zero 
        if start_node == end_node: 
            distance[start_node][end_node] = 0 
            continue 
        # return all possible paths and find the minimum 
        distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node] ) 
        # Any value that have sys.maxsize has no path 
    print (distance) 

st = time.perf_counter() #get the start time
floyd(graph)
et = time.perf_counter() # get the end time
runtime = et - st # calculate the function execution time
print ('The program used', runtime, 'seconds to execute.')

