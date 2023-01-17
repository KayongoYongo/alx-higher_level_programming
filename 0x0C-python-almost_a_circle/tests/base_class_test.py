#!/usr/bin/python3

"""unittest for Base class"""


import unittest
import sys
sys.path.append("..")
from models.base import Base


class ClassBaseTests(unittest.TestCase):
    """test suites for base class"""
    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(50)
        b7 = Base(-5)
        b8 = Base(0)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2) 
        self.assertEqual(b3.id, 3) 
        self.assertEqual(b4.id, 12) 
        self.assertEqual(b5.id, 4) 
        self.assertEqual(b6.id, 50) 
        self.assertEqual(b7.id, -5) 
        self.assertEqual(b8.id, 0)

if __name__ == "__main__":
    unittest.main()
