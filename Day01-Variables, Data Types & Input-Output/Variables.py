x = 5
y = "John"
print(x)
print(y)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

#  You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y)) 

x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive. This will create two variables
a = 4
A = "Sally"

# assgin multible varibles
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange" # assign the same value to multiple variables in one line
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

# Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

