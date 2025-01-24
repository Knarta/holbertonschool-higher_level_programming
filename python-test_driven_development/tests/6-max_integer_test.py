#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_results(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer(["School", 2, 3, 4])
        with self.assertRaises(TypeError):
            max_integer(["School", "Zebra"])
        with self.assertRaises(TypeError):
            max_integer("School")
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, 4.7])
        with self.assertRaises(TypeError):
            max_integer([1, 2], [3, 4])
        with self.assertRaises(TypeError):
            max_integer([[1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
