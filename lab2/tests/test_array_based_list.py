import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from array_based_list import ArrayBasedList

class TestArrayBasedList(unittest.TestCase):
    def setUp(self):
        self.lst = ArrayBasedList()

    def test_append(self):
        self.lst.append('A')
        self.assertEqual(self.lst.data, ['A'])

    def test_insert(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.insert('C', 1)
        self.assertEqual(self.lst.data, ['A', 'C', 'B'])
        
        with self.assertRaises(IndexError):
            self.lst.insert('D', 5)

    def test_delete(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        deleted = self.lst.delete(1)
        self.assertEqual(deleted, 'B')
        self.assertEqual(self.lst.data, ['A', 'C'])

        with self.assertRaises(IndexError):
            self.lst.delete(5)

    def test_deleteAll(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.lst.deleteAll('A')
        self.assertEqual(self.lst.data, ['B'])

    def test_get(self):
        self.lst.append('A')
        self.assertEqual(self.lst.get(0), 'A')
        
        with self.assertRaises(IndexError):
            self.lst.get(5)

    def test_findFirst(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.assertEqual(self.lst.findFirst('A'), 0)
        self.assertEqual(self.lst.findFirst('B'), 1)
        self.assertEqual(self.lst.findFirst('C'), -1)

    def test_findLast(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.assertEqual(self.lst.findLast('A'), 2)
        self.assertEqual(self.lst.findLast('B'), 1)
        self.assertEqual(self.lst.findLast('C'), -1)

    def test_reverse(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        self.lst.reverse()
        self.assertEqual(self.lst.data, ['C', 'B', 'A'])

    def test_clone(self):
        self.lst.append('A')
        self.lst.append('B')
        cloned = self.lst.clone()
        self.assertEqual(cloned.data, ['A', 'B'])
        
        cloned.append('C')
        self.assertNotEqual(self.lst.data, cloned.data)

    def test_clear(self):
        self.lst.append('A')
        self.lst.clear()
        self.assertEqual(self.lst.data, [])

    def test_length(self):
        self.assertEqual(self.lst.length(), 0)
        self.lst.append('A')
        self.assertEqual(self.lst.length(), 1)

if __name__ == "__main__":
    unittest.main()