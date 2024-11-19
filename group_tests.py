import unittest
import group

class MyTestCase(unittest.TestCase):

    def test_group_test_uneven(self):
        expected = [[1,2,3],[4,5,6],[7]]
        actual = group.groups_of_3([1,2,3,4,5,6,7])
        self.assertEqual(expected, actual) 

    def test_group_test_triple(self):
        expected = [[1, 2, 3], [4, 5, 6]]
        actual = group.groups_of_3([1, 2, 3, 4, 5, 6])
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main()
