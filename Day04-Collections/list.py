# this is the "list"
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(type(list2))
print(len(list3))

# access List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) # print the second item in the list
print(thislist[-1]) # print the last item in the list
print(thislist[2:5]) # return the third, fourth and fifth item
print(thislist[:4]) # This example returns the items from the beginning to, but NOT including, "kiwi"

thislist = ["apple", "banana", "cherry"] # Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
# change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
thislist.insert(2, "watermelon") # The insert() method inserts an item at the specified index
print(thislist)

# Add list item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # append an item
print(thislist)

thislist = ["apple", "banana", "cherry"] 
thislist.insert(1, "orange") # Insert an item as the second position
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # Add the elements of tropical to thislist
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # The pop() method removes the specified index If you do not specify the index, the pop() method removes the last item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] # The del keyword also removes the specified index
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist  # The del keyword can also delete the list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear() # The clear() method empties the list. The list still remains, but it has no content
print(thislist) 

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist: # Print all items in the list, one by one
  print(x) 

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # Print all items by referring to their index number
  print(thislist[i])  
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist): # Print all items, using a while loop to go through all the index numbers
  print(thislist[i])
  i = i + 1  

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] # with out comprehension
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"] # with comprehension

newlist = [x for x in fruits if "a" in x]

print(newlist) 

# sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # sort() method that will sort the list alphanumerically, ascending, by default
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort() # Sort the list numerically
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # To sort descending, use the keyword argument reverse = True
print(thislist)

def myfunc(n):  # Sort the list based on how close the number is to 50
      return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() # The reverse() method reverses the current sorting order of the elements
print(thislist)

# copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # Make a copy of a list with the copy() method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) # Make a copy of a list with the list() method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] # Make a copy of a list with the : operator
print(mylist)

# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 # using the + operator
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)  # appending all the items from list2 into list1, one by one
print(list1) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) # Use the extend() method to add list2 at the end of list1
print(list1)

