# The key function for working with files in Python is the open() function



# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists


# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


f = open("demofile.txt")
f = open("demofile.txt", "rt") # "r" for read, and "t" for text are the default values

f = open("demofile.txt")
print(f.read()) # read() method for reading the content of the file

f = open("D:\\myfiles\welcome.txt") # If the file is located in a different location, you will have to specify the file path, like this
print(f.read()) 

with open("demofile.txt") as f: # You can also use the with statement when opening a file
  print(f.read())

# If you are not using the with statement, you must write a close statement in order to close the file
f = open("demofile.txt")
print(f.readline())
f.close() 

# Open the file "demofile.txt" and append content to the file
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read()) 

# To overwrite the existing content to the file, use the w parameter
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 

# Delete File
# To delete a file, you must import the OS module, and run its os.remove() function
import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the file does not exist")

# To delete an entire folder, use the os.rmdir() method
import os
os.rmdir("myfolder")
