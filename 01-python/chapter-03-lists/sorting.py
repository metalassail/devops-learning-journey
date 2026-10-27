# Sorting a list permanently using the sort() method:
# cars.py

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # Before sorting
cars.sort()
print(cars) # After sorting

cars1 = ['tata', 'mahindra', 'maruti', 'hyundai']
cars1.sort()
print(cars1)

# Reverse Sort
cars1.sort(reverse=True)
print(cars1)

# Temporary Sorting using the sorted method

bikes = ['TVS', 'Norton', 'Bajaj', 'RE']
print(bikes)
print(sorted(bikes))

#  Printing list in reverse order
bikes.reverse()
print(bikes)
print(len(bikes))
