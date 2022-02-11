# Unit Testing and the unittest Python Module
# Author: Tate Kamish

# Unit testing is important for varifying that individual pieces (or units) of code
# in your application work properly. To test units of code, we can compare expected
# outputs with actual outputs. This helps account for any possible inputs that may
# have been overlooked when initially writing the unit of code.

#%%
# Using an Equality Comparison

# Let's define a function called 'rectangle_perim' that calculates the perimeter
# of a rectangle and returns it to the user

def rectangle_perim (length, width):
    perimeter = (2*length) + (2*width)
    return perimeter

# To test this unit, we can use an equality comparison of the expected ouput
# versus the actual output. We know the perimeter of a rectangle with a length
# of 5 and a width of 3 is 16, so the following should evaluate as True:

rectangle_perim(5, 3) == 16

# Looks good. But is the function built to handle all possible inputs?
# Let's try a few...
# What happens if the user passes in a string?

rectangle_perim('5', '3') == 16

# Why does the test above evaluate as False?
# Run the line below to see the actual output:

rectangle_perim('5', '3')

# The function does not specify that strings should be treated differently than
# integers or floats, so rectangle_perim('5', '3') populates the local variable
# perimeter with a concatenated string, which is then returned to the user.   
# In this case, the result is '5533'

# What if the rectangle has directional qualities and the user passes
# in a negative number?

rectangle_perim(-5, 3) == 16

# Why does the test above evaluate as False? Check below:

rectangle_perim(-5, 3)
    
# The function is not designed to take the absolute value of a number, so
# rectangle_perim(-5, 3) results in a perimeter of -4

# By performing these tests, we can make some improvements to our function: 
    
def rectangle_perim(length, width):

   if type(length) == int or type(length) == float \
   and type(width) == int or type(width) == float:
        perimeter = abs(2*length) + abs(2*width)
        return perimeter
   else:
       msg = 'Error: Arguments must have the datatype float or int.'
       return (msg)
 
# Now try these again:
    
rectangle_perim('5', '3')
rectangle_perim(-5, 3)

# Great. Our function is now better prepared to handle more types of user input.

#%%
# Using Assertions

# Similar to the equality comparisons, an assertion is a statement of fact. If an
# assertion evaluates as False, it will generate an AssertionError. If it evaluates
# as True, there will be no output.


if __name__ == "__main__":
    
    assert rectangle_perim(-5, 3) == 16
    
    #unittest.main() 

# This type of assertion statement would be included at the end of a module,
# and runs when the whole module is executed.


