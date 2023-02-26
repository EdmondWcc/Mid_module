import time

MAX_LENGTH = 0
inter = 0

def floyd_recursion(distance, MAX_LENGTH, inter):
    """
    Recursive function to compute Floyd's algorithm for finding the shortest distance between nodes.

    Parameter:
    distance: a graph containing the weights of nodes, input by the user.
    MAX_LENGTH: the number of nodes in the graph.
    inter: an intermediate node that the shortest path may contain.

    Argument:
    Compare the distance between each iteration of the start node and the end node, 
    and then compare it to the distance going through an intermediate node. 
    The smaller the distance, become the shorter the path. 
    A base case to quit the function when inter equals MAX_LENGTH, meaning that all possible intermediate iterations have been checked.

    Return:
    A new graph containing the shortest distance between each pair of nodes.
    """ 
    if inter == MAX_LENGTH:  # Base case when all possible iterations has been checked
        return
    for start_node in range(MAX_LENGTH):  # Two For loops to iterate all pairs of nodes
        for end_node in range(MAX_LENGTH):
            if (start_node == end_node or start_node == inter or end_node == inter):
                # Skip when start node equal to end node, start or end node equal to intermediate node
                continue
            if distance[start_node][end_node] > distance[start_node][inter] + distance[inter][end_node]:
                # Compare if going through intermediate node the distance is shorter
                distance[start_node][end_node] = distance[start_node][inter] + distance[inter][end_node]
    floyd_recursion(distance, MAX_LENGTH, inter + 1)  # Function calls itself again to compute the next intermediate node

def graph_input():
    """
    Function to request the user to enter a graph to compute the shortest paths.

    Argument:
    The number of nodes must be greater than 0, otherwise, the program stops.
    
    Return:
    The graph and number of nodes input by the user.
    """
    print('Input the graph to calculate the shorest path.')
    print('If there is no path from one node to another, please enter 999. All values must be greater than 0.')
    MAX_LENGTH = int(input('Please enter the number of node in the graph:'))
    if MAX_LENGTH <= 0:
        print('The number of node must be greater than 0.')
        exit()
    else:
        graph = []
        for i in range(0, MAX_LENGTH): # User to input weights for each node
            row = list(map(int, input("Please enter the weights for each node: ").split()))
            graph.append(row)
        return graph, MAX_LENGTH

if __name__ == '__main__': # Main program
    graph, MAX_LENGTH = graph_input()
    st = time.perf_counter()  # Get the start time
    floyd_recursion(graph, MAX_LENGTH, inter)
    et = time.perf_counter()  # Get the end time
    print('The calculated shorest paths are:\n', graph)
    runtime = et - st  # Calculate the function execution time
    print('The Floyd function used', runtime, 'seconds to execute.')
