#Exceptions might happen in python

# we want to handle these errors.

try:
    number = float(input("Enter a number:"))
    print(number)
except:
    print("Bro do you even know what a number is?")
# but what if we want to have different exceptions?
# we can make 2 different except blocks


try:
    number = float(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Woops, you divided by zero") # we can also print the error message
except ValueError as err:
    print(err) 

