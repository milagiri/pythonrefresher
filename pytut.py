# All code for learning will go into this file. I will comment out lines that I don't want to run


# 1. Print Hello World
'''
print("Hello world")
'''


# 2. f-string
'''
name = "Suda"
print(f"Hello, {name}")
name = "Saat"
print(f"Hello, {name}")
'''


# 3. User input
'''
name = input("What's your name? ")
print(f"Hello, {name}")
'''

# 4. Converting user input to int
'''
age = input("How old are you? ")
age_in_5_years = int(age) + 5
print(f"Today, you are {age} years old. In five years, you will be {age_in_5_years}")
'''

# 5. Rounding floating point numbers to x decimal places
'''
pi = 3.1415926535
print(f"Pi rounded to two decimal places is {pi:.2f}")
'''

# 6. Lists, tuples, and sets

list1 = ["Sherlock", "Hercule", "Jane"]
tuple1 = ("Sherlock", "Hercule", "Jane") 
# you can't modify a tuple, no adding and removing
set1 = {"Sherlock", "Hercule", "Jane"} 
# tuples and lists maintain order, you can't add duplicate elements to a set

# You can access individual elements in lists and tuples using subscript notation. Can't do this in sets.
print(list1[0])
print(tuple1[1])
# The following statement will return an error
# print(set1[2])

# You can modify a list. You can't modify a tuple

list1[0] = "Nancy"
print(list1)

# The following statemetn will return an error because you can't modify a tuple
# tuple1[0] = "Benoit"
print(tuple1)

# Add element to the end of a list
list1.append("Sherlock")
print(list1)

list1.append("Sherlock")
print(list1)


list1.remove("Hercule")
print(list1)
# This will return an error ecuase you can't modify a tuple
# tuple1.append("Nancy")


set1.add("Smith")
print(set1)

set1.add("Smith")
print(set1)