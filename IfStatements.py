if True:
    print("that's true")

isMale = True;
isFemale = False;

if isFemale:
    print("You're female")
if isMale:
    print("You're male")

# we can also combine multiple conditions with and, or and shit
# we can also have nested ifs, so if statements in if statements


# of course there's also elif to check if a statement is true after the first one fails:
if isMale:
    print("Hello")
elif not isFemale:
    print("Yup")