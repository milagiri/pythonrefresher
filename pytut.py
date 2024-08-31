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

# The following statement will return an error because you can't modify a tuple
# tuple1[0] = "Benoit"
print(tuple1)

# Add element to the end of a list
list1.append("Sherlock")
print(list1)

list1.append("Sherlock")
print(list1)

list1.remove("Hercule")
print(list1)
# This will return an error because you can't modify a tuple
# tuple1.append("Nancy")

set1.add("Smith")
print(set1)

set1.add("Smith")
print(set1)

# Different types test
set2 = {"string", 45, 32.0}
list2 = ["string", 45, 32.0]
tuple2 = ("string", 45, 32.0)
listoftuples = [("Queen", "Bohemian Rhapsody"), ("Doors", "Riders on the Storm"), ("Bob Dylan", "Hurricane")]

print(set2)
print(list2)
print(tuple2)
print(f"List of tuples: {listoftuples}")
'''

'''
Recap of cans and cants with lists, tuples, and sets

Lists: Mutable, ordered, duplicates ok, different types ok
Tuples: Immutable, ordered, duplicates, ok, elements of different types ok
Sets, Mutable, unordered, unique, elements of different types ok

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

# 9. In keyword for lists, sets, and tuples
'''

friends = {"Sachin", "Avinash", "Prabu"}

person = input("Who are you? ")
will_you_be_my_friend = False

if person in friends:
	print("Hello, friend")
else:
	will_you_be_my_friend = input("Hello, stranger. Will you be my friend? ") == "Yes"

if will_you_be_my_friend:
	friends.add(person)

print(f"My friends are {friends}")
'''

# 10. while loop

'''
number = 9
prompt_str = "Would you like to pay? (Y/n) "

# Take 1
user_input = input(prompt_str).lower()

while user_input != "n":
	user_num = int(input("Guess a number: "))
	if user_num == number:
		print("You got it!")
		break
	elif abs(user_num - number) == 1:
		print("You're close!")
	else:
		print("You're off.")

	user_input = input(prompt_str).lower()


# 11. Take 2 - better
while True:
	user_input = input(prompt_str).lower()

	if user_input == "n":
		break

	user_num = int(input("Guess a number: "))
	if user_num == number:
		print("You got it!")
		break
	elif abs(user_num - number) == 1:
		print("You're close!")
	else:
		print("You're off.")
'''

# 12. for loop with in for lists
'''
friends = ["Adam", "Sachin", "Prabu"]

for friend in friends:
	print(f"{friend} is my friend")
'''

# 13. adding the elements of a list

'''
numbers = [29, 43, 25, 36, 66]
total = sum(numbers)
print(f"The sum of {numbers} is {total}")

print("Now we will do it using a for loop")
fortotal = 0

for number in numbers:
	fortotal += number
	print(f"The sum so far: {fortotal}")
'''

# 14. List comprehensions in Python
'''
numbers = [1,3,5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Prabu", "Adam", "Anjan", "Avinash", "Sachin", "Nikita"]
start_s = [friend for friend in friends if friend.startswith("A")]
print(start_s)
'''

#15. Dictionaries
# Used to store key value pairs in Python

friend_ages = {"Prabu":41, "Sachin":46, "Adam":37}
print(friend_ages)

friend_ages["Suda"] = 45
print(friend_ages)

friend_ages["Sachin"] = 47
print(friend_ages)

friend_ages.pop("Suda")
print(friend_ages)


# List of dictionaries
'''
friends = [
	{"name":"Sachin", "age":47},
	{"name":"Adam", "age":37},
	{"name":"Nikita", "age":32}
]

print(f"{friends[0]["name"]} is {friends[0]["age"]} years old.")

# You can nest lists, tuples, and dictionaries

# Iterating over dictionaries

grades = {"Saatvik":99, "Roger":86, "Nolan":93}



for grade in grades:
	print(f"{grade}'s grade is {grades[grade]}")


for student, grade in grades.items():
	print(f"{student}'s grade is {grade}")

# Checking if a key is in the dictionary
if "Saatvik" in grades:
	print(f'Saatviks grade is {grades["Saatvik"]}')
'''

# 15. Destructuring variables

x,y = 12,15
print(f"{x} and {y}")

friendsandages = {"Prabu":41, "Sachin":46, "Adam":37}

for friend, age in friendsandages.items():
	print(f"{friend} is {age} years old.")

# APIs

'''
Why are APIs important for AI/ML?
APIs play a crucial role in AI and data science projects by enabling:

1. Access to AI models: APIs allow developers to integrate pre-trained AI models into their applications, such as NLP models from GPT-4 API or computer vision models from Google Cloud Vision API.
2. Data acquisition: APIs provide access to large datasets required for training machine learning models. This includes public datasets like those offered by Kaggle or data from social media platforms.
3. AI-powered services: Many companies offer APIs that allow developers to integrate AI capabilities into their applications without building the models themselves. Examples include sentiment analysis, entity recognition, and language translation.
'''

'''
import requests
import json

# Return data about astronauts currently in space
response = requests.get("http://api.open-notify.org/astros")
print(response.text)
'''


'''
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
'''



