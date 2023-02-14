import unittest
from shapes import Polygon
from math import isclose

class TestShapes(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])

    def tearDown(self):
        print('Tearing down')
        # If you object require special handling when destroyed, handle it here
    
    def test_area(self):
        self.assertEqual(self.poly.area, 1.0)

    def test_perimeter(self):
        self.assertEqual(self.poly.perimeter, 4.0)

    def test_ipq(self):
        self.assertEqual(self.poly.ipq, 0.7853981633974483)
        
        ## What if there is a small floating point difference?
        # self.assertEqual(self.poly.ipq, 0.785398163397448)
        
        ## Handles small floating point difference; default 7 decimal places of precision
        ## https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        # self.assertAlmostEqual(self.poly.ipq, 0.785398163397448)
        
        ## Use math.isclose() to scale for very large or very small numbers
        ## https://docs.python.org/3/library/math.html#math.isclose
        # self.assertTrue(isclose(self.poly.ipq, 0.785398163397448))
        

if __name__ == "__main__":
    unittest.main()    
