---
title: Time Complexity
author: Michael Ward, Lee Hachadoorian
---

# Definitions: How to describe time complexity

$O$
: Mathematial notation that describes the limiting behavior of a function as it approaches a particular value or infinity. In computer science, it is used to classify algorithms based on their runtime as the input size grows.

$O(1)$
: An algorithm in which runtime is not affected by input size, referred to as constant time

$O(log{n})$
: An algorithm in which runtime increase with the logarithm of input size.

$O(n)$
: An algorithm in which runtime increases linearly with input size, referred to as linear time.

$O(n*log{n})$
: An algorithm in which runtime increases as the product of input size and the log of input size.

$O(n^2)$
: An algorithm in which runtime increases exponentially with input size, referred to as quadratic time.

There are other time complexities in computer science, but these are common.

# Calculating Time Complexity

You can do a rough calculation of time complexity without any experimentation; consider the following code which calculates the approximate reading level of text input:

```
text = input("input text here: ")

letters = sentences = 0
words = 1

for char in text:
    if char.isalpha():
        letters += 1
    if char.isspace():
        words += 1
    if char in ['?', '.', '!']:
        sentences +=1

L = float(letters / words) * 100
S = float(sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

if (index < 1):
    print("Before Grade 1")

elif (index >= 16):
    print("Grade 16+")

else:
    print(f"Grade {index}")
```

Break the code down line by line, consider how many times each line of code is run.

```
letters = sentences = 0
```

Declaring variables and initialzing them happens one time and is independent of the size of input. This line is $O(1)$.


```
for char in text:
```

This line will be repeat $n$ times where $n$ is the number of characters of input. This is dependent on input and will grow linearly with input. Since the fastest growing line is $n$, the whole program can be considered in the realm of $O(n)$.


What about a nested loop? Take a look at this short program that prints half a pyramid:

```
height = int(input("Height: "))

while height < 1 or height > 8:
    height = int(input("Height: "))

for row in range(height):
    for j in range(row+1):
        print("#", end='')
    print()
```

Lets zoom in on the for loop:

```
for row in range(height):
    for j in range(row+1):
        print("#", end='')
    print()
```

The first line of the for loop will run $n$ times, where $n$ is the height of the pyramid. The second line of the for loop will run $n * n + 1$ times, which can be simplified to $n^2$. Since this line is the fasting growing, the whole program can be considered to have a runtime in the realm of $O(n^2)$.

# Space Complexity

Space complexity refers to how your code uses memory space as it grows. Space complexity is harder to manage in Python compared to a language like C where you have more control over how memory is allocated. There are a few tricks in Python to utilizing memory space efficiently:

**Reading files to memory.** Instead of reading a large file to memory, you can use a for loop to read the file line by line. Each new line will replace the previous line in memory

**Using generators instead of lists.** Building a list in memory stores every item in the list. Instead you can use a generator which only yields one value at a time as needed, avoiding storing all the values it produces at once. You can always still build a full list in memory using a generator if needed.

**Using modules that are more efficient than Python's built in structures.** Numpy is faster and more efficient for certain kinds of collections. Lists are heterogenous data stored in non-contiguous memory, whereas arrays are homogenous data stored in contiguous memory. Numpy also integrates C and C++ code into Python, which have faster execution time than Python generally.

For more information on space complexity, refer to PotPP Ch 4.
