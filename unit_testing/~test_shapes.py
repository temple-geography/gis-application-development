import pytest
from .shapes import Polygon

@pytest.fixture
def example_polygon():
    return Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])

def test_area(example_polygon):
    assert example_polygon.area == 1.0

def test_perimeter(example_polygon):
    assert example_polygon.perimeter == 4.0

def test_ipq(example_polygon):
    assert example_polygon.ipq == 0.7853981633974483
    
    ## What if there is a small floating point difference?
    # assert example_polygon.ipq == 0.785398163397448
    
    ## Use pytest.approx() for an approximate comparison
    ## https://docs.pytest.org/en/latest/reference/reference.html#pytest.approx
    # assert example_polygon.ipq == pytest.approx(0.785398163397448)
        

