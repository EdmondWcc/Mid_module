import unittest
from Floyd_main import Floyd_recursion

class TestFloydRecursion(unittest.TestCase):
    
    def test_floyd_recursion(self):
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
