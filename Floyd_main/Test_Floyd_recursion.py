from Floyd_recursion import floyd_recursion
import unittest

class TestFloydRecursion(unittest.TestCase):
    def test_shortest_path_3_nodes(self):
        # Test case for the graph with 3 nodes
        graph = [[0, 4, 999], [999, 0, 3], [1, 3, 0]]
        expected_output = [[0, 4, 7], [4, 0, 3], [1, 3, 0]]
        MAX_LENGTH = len(graph[0])
        floyd_recursion(graph, MAX_LENGTH, inter=0)
        self.assertEqual(graph, expected_output)

    def test_shortest_path_4_nodes(self):
        # Test case for the graph with 4 nodes
        graph = [[0, 7, 999, 8], [999, 0, 5, 999], [999, 999, 0, 2], [999, 999, 999, 0]]
        expected_output = [[0, 7, 12, 8], [999, 0, 5, 7], [999, 999, 0, 2], [999, 999, 999, 0]]
        MAX_LENGTH = len(graph[0])
        floyd_recursion(graph, MAX_LENGTH, inter=0)
        self.assertEqual(graph, expected_output)
        
    def test_shortest_path_5_nodes_negative(self):
        # Test case for the graph with 5 nodes and with negative weight
        graph = [[0, 3, 8, 999, -4], [999, 0, 999, 1, 7], [999, 4, 0, -5, 999], [2, 999, 999, 0, 999], [999, 999, 999, 6, 0]]
        expected_output = [[0, 3, 8, 2, -4], [3, 0, 11, 1, -1], [-3, 0, 0, -5, -7], [2, 5, 10, 0, -2], [8, 11, 16, 6, 0]]
        MAX_LENGTH = len(graph[0])
        floyd_recursion(graph, MAX_LENGTH, inter=0)
        print(graph)
        self.assertEqual(graph, expected_output)

if __name__ == '__main__':
    unittest.main()
