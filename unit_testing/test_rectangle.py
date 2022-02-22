import unittest
from rectangle import Rectangle

# creating a test case including expected and actual outputs of methods
# of the class being tested

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        rec = Rectangle(3, 2)
        expected = 6
        actual = rec.rectangle_area()
        self.assertEqual(expected, actual)
    def test_rectangle_perim(self):
        rec_1 = Rectangle(3,2)
        expected = 10
        actual = rec_1.rectangle_perim()
        self.assertEqual(expected, actual)
  

# test using unittest in command line with: python -m unittest