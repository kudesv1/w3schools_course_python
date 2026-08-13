myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove items and add new items.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) # this will raise an error because the set no longer exists

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# You can use the | operator instead of the union() method, and you will get the same result.

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#   copy()	 	                            Returns a shallow copy	
#   difference()	                -	    Returns a new frozenset with the difference	
#   intersection()	                &	    Returns a new frozenset with the intersection	
#   isdisjoint()	 	                    Returns True if there is NO intersection between two frozensets	
#   issubset()          	        <= / <	Returns True if this frozenset is a (proper) subset of another	
#   issuperset()        	        >= / >	Returns True if this frozenset is a (proper) superset of another	
#   symmetric_difference()	        ^	    Returns a new frozenset with the symmetric differences	
#   union()                	        |	    Returns a new frozenset containing the union

#   add()	 	                            Adds an element to the set
#   clear()	 	                            Removes all the elements from the set
#   copy()	 	                            Returns a copy of the set
#   difference()	                -	    Returns a set containing the difference between two or more sets
#   difference_update()	            -=	    Removes the items in this set that are also included in another, specified set
#   discard()	 	                        Remove the specified item
#   intersection()	                &	    Returns a set, that is the intersection of two other sets
#   intersection_update()	        &=	    Removes the items in this set that are not present in other, specified set(s)
#   isdisjoint()	 	                    Returns True if NO items of this set is present in another set
#   issubset()	                    <=	    Returns True if all items of this set is present in another set
#                                   <	    Returns True if all items of this set is present in another, larger set
#   issuperset()	                >=	    Returns True if all items of another set is present in this set
#                                   >	    Returns True if all items of another, smaller set is present in this set
#   pop()	 	                            Removes an element from the set
#   remove()	 	                        Removes the specified element
#   symmetric_difference()	        ^	    Returns a set with the symmetric differences of two sets
#   symmetric_difference_update()	^=	    Inserts the symmetric differences from this set and another
#   union()	                        |	    Return a set containing the union of sets
#   update()	                    |=	    Update the set with the union of this set and others

# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"
colors.discard("green")
# Print the number of items
print(len(colors))