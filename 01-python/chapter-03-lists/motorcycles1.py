# Chapter 3 : Modifying, Adding and Removing elements
# Modifying elements in a list:
# motorcycles.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modify an existing value in the list:
motorcycles[0] = 'ducati'
# here we modified the list and replaced the value in field 0 from 'honda' to 'ducati'
print(motorcycles)
# here we print the list again to ensure the changes reflect

motorbikes = ['hero', 'tvs', 'bajaj']
# here we create a new list named motorcycles1
print(motorbikes)
motorbikes.append('re')
print(motorbikes)

friends = []
# New empty list of friends:
friends.append('atul')
friends.append('chetan')
friends.append('mahesh')
friends.append('sriram')
friends.append('lalit')
# Append/add values to the list dynamically:
print(friends)
# Adding values using the insert function:
friends.insert(-1, 'copilot')
print(friends)

# Removing elements from a list using del method:
del friends[-1]
print(friends)
# adding my dear friend back :) :
friends.append('lalit')
print(friends)
# Removing elements from the list using the remove function ()
friends.remove('lalit')
print(friends)
friends.append('lalit')
print(friends)
# Using Pop method to use a value after it has been removed:
popped_friends = friends.pop()
print(f"I am still good friends with {popped_friends.title()}")
print(friends)
# Adding popped friend back :
friends.append('lalit')
print(friends)
# popping a specific value from a specific position in the list:
friends_pop = friends.pop(-1)
print(friends)
print(f"I wish I was still friends with {friends_pop}")
# Adding popped friend back :
friends.append('lalit')
print(friends)
