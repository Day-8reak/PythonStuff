from math import * # I don't actually get this import

#Python's really stupidly designed so we can print out values
print(2)

# we can print out mathematical equations:
print(10 * (3 + 5) / (2 - 0.5))

# of course modulo returns remainder
print(10 % 1)

# can obviously store in variables
val = 1

#printing strings and numbers means we need to cast the type of the number to a string:
print(str(val) + " Hello")

# We can get the absolute value of a number:
print(abs(-2))
# We can also get the power of a given number
print(pow(2, 2))
# max returns whichever number is higher, min does the opposite
print(max(1, 2, 3, 4))

# we can also round with round


   #There's a bunch of cool functions we can get if we
    # import the math function from the official python library
# floor rounds down, ceiling rounds up, sqrt returns square root

# to look up math functions check official documentation







    #Input and output section
# this line takes the user input and stores it into variable name
name = input("Give your name: ")
age = input("Give age: ")
print("Hello your name is " + name + " and your age is " + age)