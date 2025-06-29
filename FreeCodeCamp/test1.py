var1 = True
var2 = False
var3 = True 

if var1 is var2:
    print("var1 and var2 are the same")
else:
    print("var1 and var2 are different")

if var1 is var3:
    print("var1 and var3 are the same")
else:
    print("var1 and var3 are different")
"""
if var1 in var3: #cannot use 'in' with boolean values
    print("var1 is in var3")

if var1 in (var2, var3):
    print("var1 is in the tuple (var2, var3)")"""



#can also use += with strings:

sentence = "My name is "
sentence += "John Doe"
print(sentence)


# to print multiple lines, we can use triple quotes

print("""This is a multi-line string.You can write as much as you want here.
It will be printed exactly as you write it.""")

# Many different functions can be used with strings, such as:
name = "John Doe"
print(name.upper())  # Converts to uppercase        
print(name.lower())  # Converts to lowercase
print(name.title())  # Converts to title case (first letter of each word capitalized)
print(name.replace("John", "Jane"))  # Replaces 'John' with 'Jane'
print(name.split())  # Splits the string into a list of words

# we can even use in and is on strings:
if "John" in name:
    print("John is in the name")

    #backslash character can be used to escape characters in strings
escaped_string = "This is a backslash: \\"

    #Backslash also can acces other special charactes and operations:
print("This is a tab:\tAnd this is a new line:\nAnd this is a backslash: \\")




    #Strings are repesented as arrays, so we can access individual characters:print(name[0])  # Prints the first character of the string
print(name[0])  # Prints the first character of the string
print(name[-1])  # Prints the last character of the string
# We can also slice strings to get a substring
print(name[0:4])  # Prints characters from index 0 to 3 (not inclusive of 4)
print([name[-1:0:-1 ]]) # Prints from the last character to the first character (reversed)


comNum = complex(2, 3)  # Creates a complex number with real part 2 and imaginary part 3
print(comNum)  # Prints the complex number
print(comNum.real, comNum.imag)  # Prints the real and imaginary parts of the complex number