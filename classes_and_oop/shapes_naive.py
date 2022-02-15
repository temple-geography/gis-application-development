
from math import sqrt

#%%
# Second attempt
class Polygon:
    
    def __init__(self, coords, area, perimeter):
        self.coords = coords
        self.area = area
        self.perimeter = perimeter

#%%
# Third attempt with derived attributes
class Polygon:
    
    def __init__(self, coords):
        self.coords = coords
        x = [c[0] for c in coords]   #list comprehension
        y = [c[1] for c in coords]   # list comprehension
        s = 0        #placeholder before loop
        perim = 0    #placeholder before loop
        for i in range(len(coords) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i] #adding value to s and setting it equal to that
            perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
       
        self.area = s/2
        self.perimeter = perim
        
        
#%%
# Fourth attempt with private attributes
class Polygon:
    
    def __init__(self, coords):
        self.coords = coords
        x = [c[0] for c in coords] 
        y = [c[1] for c in coords]
        s = 0
        perim = 0
        for i in range(len(coords) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i]
            perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
       
        self._area = s/2           #private attribute 
        self._perimeter = perim    #private attribute 

    @property    #decorator 
    def area(self):
        return self._area  #returns value of private attribute 
    
#this stops the user from assigning their own value to the property

    @property
    def perimeter(self):
        return self._perimeter
           
if __name__ == "__main__":
    
    poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    
#####################


from math import sqrt   

class Polygon:
    
    def __init__(self, coords):
        self.coords = coords
        x = [c[0] for c in coords]
        y = [c[1] for c in coords]
        s = 0
        perim = 0
        for i in range(len(coords) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i]
            perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
    
        
    @property
    def area(self):
        return self.area
    
    @property 
    def perimeter(self):
        return self._perimeter
    
    @coords.setter 
    def coords(self, coords):
        self._coords = coords 
### add method that is a function that changes the state of the object 
#### such as shift the coordinates 
#### def translat (self, delta_x, delta_y)
####..................................
###...................................
#ending self.coords = c

###rebuild list of coordinate tuples 

### translate method        

#%%
class Polygon:
    
    def __init__(self, coords):
        self.coords = coords

    @property    
    def area(self):
        return self._area  

    @property
    def perimeter(self):
        return self._perimeter
    
    @property
    def coords(self):
        return self._coords

    
    @coords.setter
    def coords(self,coords):
        self._coords = coords
        x = [c[0] for c in coords] 
        y = [c[1] for c in coords]
        s = 0
        perim = 0
        for i in range(len(coords) - 1):
            s += x[i]*y[i+1] - x[i+1]*y[i]
            perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
       
        self._area = s/2          
        self._perimeter = perim
       
           
if __name__ == "__main__":
    
    poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])