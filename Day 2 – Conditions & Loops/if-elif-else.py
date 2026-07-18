# An "if statement" is written by using the if keyword
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
# elif
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  

# else
# The else keyword catches anything which isn't caught by the preceding conditions
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# You can also have an else without the elif 
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
