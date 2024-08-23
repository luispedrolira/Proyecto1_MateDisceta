import unittest
import Set

class TestSet(unittest.TestCase):
    
    def setUp(self):
        self.s = ()
    
    def test_add_element(self):
        self.s.add_element(1)
        self.assertTrue(self.s.contains(1))
        self.assertFalse(self.s.contains(2))
        self.s.add_element(1)  # Adding the same element again
        self.assertEqual(self.s.elements, [1])
        self.s.add_element(2)
        self.assertTrue(self.s.contains(2))
        self.assertEqual(self.s.elements, [1, 2])

    def test_remove_element(self):
        self.s.add_element(1)
        self.s.remove_element(1)
        self.assertFalse(self.s.contains(1))
        self.assertEqual(self.s.elements, [])
        self.s.remove_element(2)  # Removing an element not in the set
        self.assertEqual(self.s.elements, [])

    def test_remove_element_empty_set(self):
        self.s.remove_element(1)  # Removing from an empty set
        self.assertEqual(self.s.elements, [])

if __name__ == '__main__':
    unittest.main()