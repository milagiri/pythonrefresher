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

'''
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
'''

# 7. More set operations -- difference, union, intersection

'''
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne", "Jack"}
local_friends = friends.difference(abroad)
abroad_notfriends = abroad.difference(friends)
total_peeps = friends.union(abroad)
friendsabroad = friends.intersection(abroad)

print(f"Friends: {friends}")
print(f"People abroad: {abroad}")
print(f"Local friends = friends - people abroad: {local_friends}")
print(f"People abroad = abroad - friends: {abroad_notfriends}")
print(f"Everyone = friends union abroad: {total_peeps}")
print(f"Friends abroad = friends intersection abroad: {friendsabroad}")

'''

# 8. Boolean and if-else conditional
'''
yourName = input("Who are you? ")
if yourName == "Joe":
	print("Shmoe")
elif yourName == "Mike":
	print("Psych")
elif yourName == "Peter":
	print("Eater")
else:
	print(f"Hello {yourName}")



# Comparing lists
list1 = ["Adam", "Sachin", "Prabu"]
list2 = ["Adam", "Sachin", "Prabu"]
list3 = ["Sachin", "Adam", "Prabu"]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")
print(f"Is list1 == list2 {list1 == list2}")
print(f"Is list1 == list3 {list1 == list3}")

# Comparing sets
set1 = {"Adam", "Sachin", "Prabu"}
set2 = {"Adam", "Sachin", "Prabu"}
set3 = {"Sachin", "Adam", "Prabu"}

print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set3 = {set3}")
print(f"Is set1 == set2 {set1 == set2}")
print(f"Is set1 == set3 {set1 == set3}")

'''


