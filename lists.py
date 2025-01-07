friends = ["Khoi", "Aurko", "Akhilesh", "no one", "My imagination"]

# if we want to print out a specific number in the list we can print out the index:
print(friends[1]) # prints Aurko - 2nd element in the list

# can specify range:
print(friends[0:2]) # prints between 0 - 2nd value. Notice how the beginning of the range is included but the end of it isn't
print(friends[2:]) # prints any value after the second
print(friends[:3]) # prints first three values


# can modify lists:
friends[0] = "Mike"



    # Lists continued
luckyNums = [75, 69, 42, 21, 6942, 69421, 7512, 75, 6, 9, 8]
friends.extend(luckyNums)
# now the friends list includes all the numbers
# append allows us to add lists:
friends.append(7659)

#can insert values in certain positions which pushes all other items 1 unit back:
friends.insert(3, 6969)
print(friends)

#can also remove values:
friends.remove(7512) # only accepts one value
print(friends)