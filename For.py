
# python sucks, in this case the length of the given string is
# the number of times we run the code in the for loop
# if we want to use the thing we're looping over we use letter
for letter in "I am the Goat. I will, no I MUST change the world.":
    print(letter)
    if letter == "G" or letter == "g":
        print("My top G")
print("The loop is over")


# obviously we can use arrays as well:
friends = ["Lol", "69", "urmom", "MrBeast", "Barack Obama", "Adolpin hitler", "Jerry"]
for friend in friends:
    print(friend)


# we can also do a range
for index in range(10):
    print(index)

for index in range(3, 10):
    print("Urmom")

# of course the first word doesn't have to be accurate
# we can just call all of them bigChungus if we wanted to