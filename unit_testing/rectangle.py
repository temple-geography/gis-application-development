# Creating a class called Rectangle which has two methods: one for finding the area
# and one for finding the perimeter:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def rectangle_area(self):
        area = abs(self.length * self.width)
        return area
    
    def rectangle_perim(self):
        perimeter = abs(2*self.length) + abs(2*self.width)
        return perimeter


# Example of calling on method
#x = Rectangle(5,4)
#x.rectangle_area() 
