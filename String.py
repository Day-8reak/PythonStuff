print("My life Is terrible bro")
# can't put quotation marks in strings unless you type a \ which basically
# means we ignore the normal thing that character does

phrase = "LOWER CASE EXAMPLE"
print(phrase.lower()) # We print phrase but lower case
# we can also do uppercase

#is upper and islower checks if a given string is all upper or lower case
print(phrase.islower())
print(len(phrase)) # returns length of phrase

# we can specify the index of the letter given:
print(phrase[0]) # prints first character


#index returns the index of the first instance of something
print(phrase.index("M"))

#replace allows us to replace certain phrases with others
print(phrase.replace("Lower", "Hello"))
