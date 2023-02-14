
from math import sqrt, pi

class Polygon:
    """Represents a 2-D polygon."""
    
    def __init__(self, coords):
        self.coords = coords
        
    @property
    def coords(self):
        return self._coords
    
    @coords.setter
    def coords(self, coords):
        if coords[0] != coords[-1]:
            coords.append(coords[0])
           
        # Check that polygon has at least three points
        if len(coords) < 3:
            raise Exception("coords must contain at least three points")
       
        self._coords = coords
       
        # Calculate area
        x = [c[0] for c in coords]
        y = [c[1] for c in coords]
        s = 0
        perim = 0
        for i in range(len(coords) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i]
            perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
       
        self._area = s/2
        self._perimeter = perim
        self._ipq = 4 * pi * self._area / self._perimeter**2
        
    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter
    
    @property
    def ipq(self):
        return self._ipq

