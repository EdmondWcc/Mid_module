import time
import unittest

def floyd_recursion(distance, inter=0):
    # Use recursive function to compute Floyd's algorithm

    if inter == MAX_LENGTH:  # Base case when intermediate equal to the number of node
        return
    for start_node in range(MAX_LENGTH):  # Two For loops to iterate all pairs of nodes
        for end_node in range(MAX_LENGTH):
            if (start_node == end_node or start_node == inter or end_node == inter):
                # Skip when start equal to end node, start or end equal to intermediate node
                continue
            if distance[start_node][end_node] > distance[start_node][inter] + distance[inter][end_node]:
                # Compare if going through intermediate node the distance is shorter
                distance[start_node][end_node] = distance[start_node][inter] + distance[inter][end_node]
    floyd_recursion(distance, inter + 1)  # Function calls itself again to compute the next intermediate node

# Main program
print('Input the graph to calculate the shorest path.')
print('If there is no path from one node to another, please input 999.')

MAX_LENGTH = int(input('Please input the number of node in the graph:'))

graph = []
for i in range(0, MAX_LENGTH):
    row = list(map(int, input("Enter the weights for node {i}: ").split()))
    graph.append(row)
    
st = time.perf_counter()  # Get the start time
floyd_recursion(graph)
et = time.perf_counter()  # Get the end time
print('The calculated shorest paths are:\n', graph)
runtime = et - st  # Calculate the function execution time
print('The program used', runtime, 'seconds to execute.')


class TestFloydRecursion(unittest.TestCase):
            
    def test_floyd_recursion3(self):
        graph = [
            [0, 4, 999],
            [999, 0, 3],
            [1, 3, 0]            
        ]
        global MAX_LENGTH
        MAX_LENGTH = 3
        floyd_recursion(graph)
        self.assertListEqual(graph, [
            [0, 4, 7],
            [4, 0, 3],
            [1, 3, 0]
        ])
    
    def test_floyd_recursion4(self):
        graph = [
            [0, 7, 999, 8],
            [999, 0, 5, 999],
            [999, 999, 0, 2],
            [999, 999, 999, 0]
        ]
        global MAX_LENGTH
        MAX_LENGTH = 4
        floyd_recursion(graph)
        self.assertListEqual(graph, [
            [0, 7, 12, 8],
            [999, 0, 5, 7],
            [999, 999, 0, 2],
            [999, 999, 999, 0]
        ])
        
if __name__ == '__main__':
    unittest.main()