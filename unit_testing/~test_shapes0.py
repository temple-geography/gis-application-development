from shapes import Polygon
from math import isclose

def test_area():
    example_polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    assert example_polygon.area == 1.0

def test_perimeter():
    example_polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    assert example_polygon.perimeter == 4.0

def test_ipq():
    example_polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    assert example_polygon.ipq == 0.7853981633974483

