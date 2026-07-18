# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try: # The try block will generate an exception, because x is not defined
  print(x)
except:
  print("An exception occurred") 
# Print one message if the try block raises a NameError and another for other errors
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 
  

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

# Try to open and write to a file that is not writable
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 

# To throw (or raise) an exception, use the raise keyword
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero") 

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed") 
