---
title: Creating Classes in Python
author: Lee Hachadoorian
---

A class is a template for creating objects with closely related data (attributes) and behaviors (methods). Classes are often used to represent real world entities such as a person, place, or thing. An employee object might have attributes like name and age, and methods like hire, promote, and terminate. Classes can also represent program functionalities such as a collection of related algorithms, or a GUI application window.

In the geospatial context, a class could represent a spatial layer or a geographic feature. Since this is a GIS course, we will construct a basic class that could be used to store spatial data, specifically, a polygon.

The following examples make use of the file [shapes_naive.py](shapes_naive.py]. You should download this now and open it in your preferred Python IDE.

# Creating a Class

## An Empty Class

**First attempt (not shown in script)**

A simple, if not very interesting class, can be created with no attributes and no methods. All block level code in Python requires content, and the `pass` statement can be used as a placeholder to stub out a block to be defined later. By convention, class names use `CamelCase`. Type the following code into a script and run it:

```python
class Polygon:
    pass
```

You've just created your first class! Let's create an instance of the class and assign some attributes:

```python
poly = Polygon()

poly.coords = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
poly.area = 1.0
poly.perimeter = 4.0
```

We have given a list of coordinate tuples that define the boundary of a unit square as the `coords` attribute. This square has a perimeter of 4.0 (four sides of length 1 each) and area of 1.0. The attributes can be accessed using dot notation:

```python
print("Area =", poly.area)
```

## A Class with Required Attributes

**Second attempt**

Even though we have named our class `Polygon`, all it is so far is a bucket into which we can dump any attributes we want. We assigned sensible attributes, but shouldn't we make sure that any instance of the class has boundary coordinates, an area, and a perimeter length?

We can make sure that a class is created with specific attributes by defining an `__init__` method. A **method** is a function that is attached to a class. It can have input parameters just like any other user-defined function in Python. `__init__` is the name of a special method that is called when the class is first instantiated.

Open the file `shapes_naive.py` and look at the code labelled "Second attempt":

```python
# Second attempt
class Polygon:
    
    def __init__(self, coords, area, perimeter):
        self.coords = coords
        self.area = area
        self.perimeter = perimeter
```

The first parameter, `self`, is the name that the current instance of the class calls itself, regardless of the identifier assigned by the calling namespace. That is, your name might be "Lee", but you think of yourself as "me". A class could be instantiated with the name `object1`, but it still needs an internal shorthand to refer to itself. By convention, Python coders always name this parameter `self`. *The `self` parameter is always omitted when calling methods of the class (including `__init__`).*

The next three parameters are the values for attributes that we want an instance of the class to always have. These three parameters must be inlcuded when the polygon is instantiated. (This function call uses positional parameters rather than keyword parameters: the order is *coords*, *area*, *perimeter*.)

```python
poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], 1.0, 4.0)
```

If we try to instantiate the class without passing arguments to these three parameters, we will get an error:

```python
poly = Polygon()
```

## A Class with Derived Attributes

**Third attempt with derived attributes**

It may occur to you that if you have the coordinates that define the boundary of a polygon, you should be able to calculate the area and the perimeter. But the class we just created requires the user to pass in the area and perimeter. This is poorly designed for two reasons:

1. It requires the user to calculate values that can be derived from other attributes.
2. An incoherent combination of attributes could be passed in, such as:

```python
poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], 87.3, -494)
```

Examine the code labelled "Third attempt with derived attributes". In this version, there is only one required attribute, `coords`. The area and perimeter are calculated from the coordinates. The perimeter is calculated by using the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) to calculate the distance between each pair of adjacent coordinates. The area is calculated using the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula).

Create a polygon instance by passing in a list of coordinate tuples. Then read the values of the area and perimeter attributes.

> When you retrieved the area, did you get a negative number? This method of calculating the area will produce a positive area if the coordinates wind counterclockwise, and a negative area if the coordinates wind clockwise. Polygons constructed this way follow the **right-hand rule**, so-called because if you are standing on the edge of the polygon looking toward the interior, you would go to the right (counterclockwise) to traverse the permimeter.
> 
> We have been working with a simple polygon, that is, a polygon with no holes, but this way of calculating area is useful for creating polygons with holes. In that case, you would need to specify the coordinates of the exterior ring and one or more interior rings (holes). The coordinates of the exterior ring are given counterclockwise, yielding a positive area. The coordinates of the interior rings are given clockwise, yielding a negative area. The area of the polygon is then the sum of these areas: the area bounded by the exterior ring plus the *negative* areas of the holes. Creating a polygon with holes is left as an exercise. An additional exercise would be to check the coordinates passed in and determine whether they follow the right-hand rule, reversing the order if they don't.

## A Class with Private Attributes

**Fourth attempt with private attributes**

Our previous attempt is an improvement. When we enter the coordinates, the perimeter and area are calculated automatically. But what happens if you run this code:

```python
poly.perimeter = -47
poly.area = "Thor"
```

The perimeter is no longer derived from the coordinates, and the area is not even the right data type! What we need is a way to control or block the ability to change attributes. We do this by creating **private attributes**, and adding a method to the class that allows us to retrieve or change this attribute. The private attribute is given a name beginning with an underscore, which is not accessed directly. For example, if you have instantiated a `Polygon` object with the name `poly`, you would still refer to `poly.perimeter` in your code. Internally, however, the object has a private attribute `_perimeter`. What we need is a way to pass values between `perimeter` and `_perimeter`.

Note that many programming languages use the concept of **getter** and **setter** functions to work with private attributes. Although you may see examples online of doing this in Python, it is considered un-Pythonic. To get the area of `poly`, you would have to access it with something like `poly.get_area()`, rather than the clear and concise `poly.area`.

Python allows us to work with private attributes using the `@property` decorator. To set and get values for a generic attribute `attribute1`, you use the `@property` decorator to get the attribute, and the `@<attribute_name>.setter` decorator to set the attribute. A code template for using this decorator is as follows:

```python
    @property
    def attribute1(self):
        return self._attribute1

    @attribute1.setter
    def attribute1(self, attribute1):
        self._attribute1 = attribute1
```

Since we *don't* want to be able to directly change the area or perimeter of our polygon, we are going to omit the setter decorator. In the init method, we change

```python
        self.area = s/2
        self.perimeter = perim
```

to

```python
        self._area = s/2
        self._perimeter = perim
```

We then add `area` and `perimeter` **properties**:

```python
    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter
```

See the code labelled "Fourth attempt with private attributes" for the complete class definition.

### Exercise

The *isoperimetric quotient* is a measure of shape compactness given by:

<img src="https://latex.codecogs.com/svg.image?IPQ&space;=&space;4\pi&space;\frac{Area}{Perimeter^2}" title="IPQ = 4\pi \frac{Area}{Perimeter^2}" />

Using private attributes and the `@property` decorator, add `ipq` as a read-only attribute to the `Polygon` class.

If you create the attribute correctly, `poly.ipq` should return $0.785...$.

<!-- * Calculating derived attributes when retrieved vs. when "master" attribute is set.-->


## Further Refinement: Getting and Setting the Coordinates

The above approach works for turning `area` and `perimeter` into read-only derived attributes. The user can't change these attributes to something else. The user still *can* however change the `coords` attribute, recreating the problem of the area and perimeter being out of sync with the coordinates.

To fix this, we need to also turn `coords` into a private attribute. Further, we need a `@coords.setter` decorator that recalculates the area and perimeter (and, if you completed the previous exercise, the IPQ) whenever the coordinates are changed, not just at the beginning.

### Exercise

Begin with the following code:

```python
class Polygon:
    
    def __init__(self, coords):
        self.coords = coords
        
```

Now, using the template for the `attribute1` template given above, create `@property` and `@coords.setter` decorators to turn `coords` into a read/write attribute. All of the logic that calculates the values of the derived attributes (perimeter, etc.) should be moved from the old `__init__` to the attribute setter.


## A Class with a Method

In some sense methods are similar to procedures or functions. In Python, methods are in fact defined as functions in the class definition. But they are not just any procedure, they are procedures that represent an object's *behaviors* in the same way that its properties or attributes represent the object's *data*. The behaviors should be conceptually related to the object.

The **state** of an object is the values associated with all of the object's properties. Methods often change the state of an object, either the object itself or another object that it is interacting with. For example, a video game might have an object named `tinder` that is an instance of the `Dragon` class, and an object named `sir_gawain` that is an instance of the `Knight` class. Both objects might have a `health` property. The dragon might have a `bite` method that takes another object as a parameter. If the `sir_gawain` object is passed as a parameter, its `health` is reduced—that is, its state is changed. The dragon might also have a `heal` method, that changes its own state by increasing its `health`.

Polygons can be translated (shifted) in space, so a `translate` method might be useful for a polygon object. The polygon is moved by changing *all* coordinates by the same amount in the x and y axis. All we need to do is read all of the individual coordinates, add a fixed amount to the x coordinates and a (likely different) fixed amount to the y coordinates, then reassign the coordinates of the object. Derived attributes will be automatically updated when we change the coordinates.

The code of our previous polygon class can stay the same. All we need to do is add the following function (method) to the class definition:

```python
    def translate(self, delta_x = 0, delta_y = 0):
        coords = self.coords
        x = [c[0] + delta_x for c in coords]
        y = [c[1] + delta_y for c in coords]
        c = list(zip(x, y))
        self.coords = c
```

Run the class definition code and create an instance of the class. Then run the `translate` function, passing in `delta_x` and/or `delta_y`. (Note that the parameters have a default value of 0, so if you only pass `delta_x`, the polygon will be translated along the x-axis but not the y-axis.

A slightly more complex version of the `translate` function might take a vector (magnitude and direction) and use trigonometry to calculate `delta_x` and `delta_y`.

Note that the line `self.coords = c` will trigger the recalculation of the perimeter and area, but the perimeter and area don't actually change. (Moving the polygon doesn't change its area.) You might be tempted to come up with a way to change the coordinates *without* recalculating the perimeter and area, and it *is* possible (see next section). However, there could be other derived attributes, such as the coordinates of the polygon's centroid, which would change when the coordinates change. Usually you will want to recalculate all derived attributes. If you try to save CPU cycles by recalculating some derived attributes (e.g. the centroid) and not others (e.g. perimeter, area), you will have to be very, very careful about how you set up that class.

## When to Calculate Derived Attributes

Derived attributes might be calculated when the object is created, or when the attribute is read, that is, when `object1.attribute1` is evaluated. That is, another way to create the polygon class would be to put the logic for calculating the perimeter in the `perimeter` function. Deciding when to do so depends on how much startup time is required to instantiate the object and how often the attributes are accessed. If the object has many properties that are expensive to calculate, but rarely accessed, it makes sense to defer calculation until the value is needed.

Even in this case, you want to calculate the value only once. To do so, you would create the private attribute with no value (Python `None`). Then, when the property was accessed, you would check value of the private attribute. If its value was `None`, you would calculate the value and store it in the private attribute. But if the private attribute had a value other than `None`, you would return the existing value.

Here is an example of doing so for the `perimeter` attribute. The corresponding calculation would be *removed* from the coords setter. Further, `self._perimeter` would have to be set (or reset) to `None` in the coords setter.

```python
    @property
    def perimeter(self):
        if self._perimeter is None:
            coords = self.coords
            x = [c[0] for c in coords]
            y = [c[1] for c in coords]
            perim = 0
            for i in range(len(coords) - 1):
                perim += sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)
           
            self._perimeter = perim

        return self._perimeter
```

### Exercise

**To be completed on your own time**

A bounding box is a rectangle that completely encloses a polygon. The bounding box can be constructed knowing only the minimum and maximum *x* and *y* coordinates in the polygon. The minima and maxima can easily be extracted by using `min` and `max` on a list of the *x* coordinates and, separately, on a list of the *y* coordinates.

Once we know the minimums and maximums of the *x* and *y* coordinates, we can use the `Polygon` class to create the bounding box. But if we do that in the `__init__` method, we will immediately encounter an infinite regress! When we instantiate the Polygon class to create the bounding box, we would also construct the bounding box of the bounding box, then the bounding box of the bounding box of the bounding box, etc.

The solution is to add a read-only `bbox` property, and construct the bounding box only when the property is accessed. But use the example above to store the bounding box so that it is only created once, and not recreated each time the property is accessed.

