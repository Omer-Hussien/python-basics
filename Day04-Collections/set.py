thisset = {"apple", "banana", "cherry"}
print(thisset) 

thisset = {"apple", "banana", "cherry", "apple"} # Sets cannot have two items with the same value
print(thisset) 

thisset = {"apple", "banana", "cherry", True, 1, 2} # The values True and 1 are considered the same value in sets, and are treated as duplicates
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0} # The values False and 0 are considered the same value in sets, and are treated as duplicates
print(thisset)

thisset = {"apple", "banana", "cherry"} # To determine how many items a set has, use the len() function
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} # Set items can be of any data type

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # It is also possible to use the set() constructor to make a set

# access set items
thisset = {"apple", "banana", "cherry"} # Loop through the set, and print the values
for x in thisset:
  print(x) 
  
# add sets item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # To add one item to a set use the add() method
print(thisset) 

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # To add items from another set into the current set, use the update() method
print(thisset) 

# remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # To remove an item in a set, use the remove(), or the discard() method
print(thisset)

# loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

# join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # The union() method returns a new set with all items from both sets
print(set3) 

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4 # Use | to join two sets
print(myset) 

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y) # The union() method allows you to join a set with other data types, like lists or tuples
print(z) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) # The intersection() method will return a new set, that only contains the items that are present in both sets
print(set3) 

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2) # Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2) # The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set
print(set1) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) # The symmetric_difference() method will keep only the elements that are NOT present in both sets
print(set3) # You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result

# frozenset
x = frozenset({"apple", "banana", "cherry"}) # Use the frozenset() constructor to create a frozenset from any iterable
print(x)
print(type(x)) 


