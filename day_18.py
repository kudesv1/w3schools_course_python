# range(start, stop, step)

x = range(10)

x = range(3, 10)

x = range(3, 10, 2)

for i in range(10):
  print(i)

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

r = range(10)
print(r[2])
print(r[:3])

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

r = range(0, 10, 2)
print(len(r))

# Print 0 through 5
for x in range(6):
  print(x)

# Print 2 through 5
for x in range(2, 6):
  print(x)

cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
  print(x)

cars.append("Honda")

cars.pop(1)

cars.remove("BMW")

# append()	   Adds an element at the end of the list
# clear()	   Removes all the elements from the list
# copy()	   Returns a copy of the list
# count()	   Returns the number of elements with the specified value
# extend()	   Add the elements of a list (or any iterable), to the end of the current list
# index()	   Returns the index of the first element with the specified value
# insert()	   Adds an element at the specified position
# pop()        Removes the element at the specified position
# remove()	   Removes the first item with the specified value
# reverse()    Reverses the order of the list
# sort()	   Sorts the list

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Create a list
cars = ["Ford", "Volvo", "BMW"]
# Print the first item
print(cars[0])
# Change the second item to "Toyota"
cars[1] = "Toyota"
# Print the list
print(cars)