thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") # Tuples allow duplicate values
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # To determine how many items a tuple has, use the len() function

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male") # A tuple with strings, integers and boolean values

# Access tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # You can access tuple items by referring to the index number, inside square brackets

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # Return the third, fourth, and fifth item

# update tuple
x = ("apple", "banana", "cherry") # Convert the tuple into a list to be able to change it
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

thistuple = ("apple", "banana", "cherry") # Convert the tuple into a list, add "orange", and convert it back into a tuple
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry") # Create a new tuple with the value "orange", and add that tuple
y = ("orange",)
thistuple += y
print(thistuple)

# unpake tuple
fruits = ("apple", "banana", "cherry") 
(green, yellow, red) = fruits # extract the values back into variables. This is called "unpacking"
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits # Assign the rest of the values as a list called "red"
print(green)
print(yellow)
print(red)

# loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): # Print all items by referring to their index number
  print(thistuple[i]) 
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple): # Print all items, using a while loop to go through all the index numbers
  print(thistuple[i])
  i = i + 1 
  
# join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 # To join two or more tuples you can use the + operator
print(tuple3) 

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 # multiply the content of a tuple a given number of times, you can use the * operator
print(mytuple) 

