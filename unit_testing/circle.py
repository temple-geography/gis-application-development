# Creating a class called Circle which has two methods: one for finding the area
# and one for finding the circumference:

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circle_area(self):
        area = pi * (self.radius**2)
        return area
    
    def circle_circumference(self):
        circumference = (2*pi*self.radius)
        return circumference 

