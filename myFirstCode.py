# # use CTRL + / to comment multiple lines

# # Display text in the console
# print("Hello World!")

# # Creating variables
myFirstName = "John" # String variable - text
myLastName = "Smith"
myAge = 60 # Interger variable - whole number
myTestResult = 78.98 # Float variable - decimal number
myBool = True # Boolean variable - can only be true or false. Case senitive - always use a capital T or F

# # Calculate and print the answer
# print(myAge * 10)

# # Change the variable myAge from 60 to 61 and then print the new result
myAge = 30
# print(myAge)

# # Ask what type of varaible is myAge and print the answer
# print(type(myAge))

# # Joins both string varaibles together
# print(myFirstName + myLastName)

# # Calculate both interger varaibles together
# print(myAge + myTestResult)

# x = 100
# y = 50

# # Changes the string value to interger, calcualte and print the answer
# print(int(x) + int(y))

# print(x + y) # addition
# print(x * y) # multiplication
# print(x / y) # division
# print(x - y) # subtraction
# print(x ** 2) # x squared
# print(x ** 3) # x cubed
# print(x > y) # Is x more than y? Print true
# print(x <= y) # Is x less and or equal to y?
# print(x == y) # Is x equal to why?
# print(x != y) # Are these not equal?

# Conditional fuctions
if myFirstName == "John":
    print("Hello John")

if myAge < 1:
    print("You are a baby")
elif myAge >= 1 and myAge <= 3:
    print("You are a toddler")
elif myAge >= 4 and myAge <= 12:
    print("You are a child")
elif myAge >= 13 and myAge <= 19:
    print("You are a teenager")
elif myAge >= 16 and myAge <= 24:
    print("You are an young adult")
else:
    print("You are an adult")
