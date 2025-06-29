import array
    #answer to question 1
# There are 2 different types of arrays in python, from the numpy and array modules.
# The numpy array is more powerful and flexible, while the array module provides a more basic array type.
myarr = array.array('i', [1, 2, 3, 4, 5])
print(myarr[0])  # Prints the first element of the array



    # Answer to question 3
# Reversing a string using slicing
my_string = "hello"
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

# Reversing a list using slicing
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)


    # Answer to question 4
testlist = ["abc", "def", "ghi", 0]
print(testlist[0][1])  # Prints the second character of the first string in the list
print(testlist[1])  # Prints the second string in the list
print(testlist[3])  # Prints the fourth element in the list


    #answer to question 5
fruits = {"apple", "banana", "cherry", "tomato", "orange", "kiwi", "melon", "mango"}
vegetables = {"carrot", "broccoli", "spinach", "tomato", "cucumber", "pepper", "onion", "garlic"}

print("Union:", fruits | vegetables)  # Prints the union of fruits and vegetables
print("Intersection:", fruits & vegetables)  # Prints the intersection of fruits and vegetables
print("Difference:", fruits - vegetables)  # Prints the difference of fruits and vegetables
print("Symmetric Difference:", fruits ^ vegetables)  # Prints the symmetric difference of fruits and

fruits2 = ["apple", "banana", "cherry", "tomato", "orange", "kiwi", "melon", "mango"]
vegetables2 = ["carrot", "broccoli", "spinach", "tomato", "cucumber", "pepper", "onion", "garlic"]
print("Union2:", fruits2 | vegetables2)  # Prints the union of fruits and vegetables
print("Intersection2:", set(fruits2) & set(vegetables2))  # Prints the intersection of fruits and vegetables
print("Difference2:", set(fruits2) - set(vegetables2))  # Prints the difference of fruits and vegetables
print("Symmetric Difference2:", set(fruits2) ^ set(vegetables2))  # Prints the symmetric difference of fruits and vegetables