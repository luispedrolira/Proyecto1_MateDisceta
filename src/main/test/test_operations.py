import unittest
import Set, Operations

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.set1 = Set()
        self.set1.add_element('A')
        self.set1.add_element('B')
        self.set1.add_element('C')
        
        self.set2 = Set()
        self.set2.add_element('B')
        self.set2.add_element('C')
        self.set2.add_element('D')
        
        self.set3 = Set()
        self.set3.add_element('E')
        self.set3.add_element('F')
        self.set3.add_element('G')
        
        self.ops1 = Operations(self.set1.elements)
        self.ops2 = Operations(self.set2.elements)
        self.ops3 = Operations(self.set3.elements)

    def test_union(self):
        result = self.ops1.union(self.ops2)
        expected_elements = ['A', 'B', 'C', 'D']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_intersection(self):
        result = self.ops1.intersection(self.ops2)
        expected_elements = ['B', 'C']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_difference(self):
        result = self.ops1.difference(self.ops2)
        expected_elements = ['A']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))

    def test_symmetric_difference(self):
        result = self.ops1.symmetric_difference(self.ops2)
        expected_elements = ['A', 'D']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))

    def test_complement(self):
        result = self.ops1.complement()
        expected_elements = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' if char not in self.set1.elements]
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_empty_union(self):
        empty_set = Set()
        result = self.ops1.union(Operations(empty_set.elements))
        expected_elements = ['A', 'B', 'C']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_empty_intersection(self):
        empty_set = Set()
        result = self.ops1.intersection(Operations(empty_set.elements))
        expected_elements = []
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_empty_difference(self):
        empty_set = Set()
        result = self.ops1.difference(Operations(empty_set.elements))
        expected_elements = ['A', 'B', 'C']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))
    
    def test_empty_symmetric_difference(self):
        empty_set = Set()
        result = self.ops1.symmetric_difference(Operations(empty_set.elements))
        expected_elements = ['A', 'B', 'C']
        self.assertEqual(sorted(result.elements), sorted(expected_elements))

if __name__ == '__main__':
    unittest.main()
