thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {   # The values in dictionary items can be of any data type
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

thisdict = dict(name = "John", age = 36, country = "Norway") # It is also possible to use the dict() constructor to make a dictionary
print(thisdict)

# access items
thisdict = { # You can access the items of a dictionary by referring to its key name, inside square brackets
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model") # There is also a method called get() that will give you the same result
x = thisdict.keys() # The keys() method will return a list of all the keys in the dictionary
x = thisdict.values() # The values() method will return a list of all the values in the dictionary
x = thisdict.items() # The items() method will return each item in a dictionary, as tuples in a list

# change items
thisdict = { # You can change the value of a specific item by referring to its key name
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = { # The update() method will update the dictionary with the items from the given argument
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# remove items
thisdict = { # The pop() method removes the item with the specified key name
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

thisdict = { # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 

thisdict = { # The del keyword removes the item with the specified key name
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

thisdict = { # The clear() method empties the dictionary
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

# loop in dictionaries
for x in thisdict: # You can loop through a dictionary by using a for loop
      print(x) 
      
for x in thisdict.values(): # You can also use the values() method to return values of a dictionary
      print(x)     

for x in thisdict.keys(): # You can use the keys() method to return the keys of a dictionary
      print(x) 

# Copy a Dictionary
thisdict = { # Make a copy of a dictionary with the copy() method
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = { # Make a copy of a dictionary with the dict() function
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 

# Nested Dictionaries
myfamily = { # Create a dictionary that contain three dictionaries
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}  

print(myfamily["child2"]["name"]) # Print the name of child 2

for x, obj in myfamily.items(): # You can loop through a dictionary by using the items() method like this
    print(x)

    for y in obj:
            print(y + ':', obj[y])


