# Can use python read command
# this allows us to open, read


# using the open command depends on the location
# of the file and other specifics
something = open("RandomTextFile", "r") #a = append, w = write, r = read, r+ = reading and writing
# can be file name if python program and file in the same directory
# Otherwise it'll be a relative/absolute path to file
# the second part determines what permissions we have with the file


# we should always check if a file is readable before we check it:
print(something.readable()) # returns boolean value


#read entire file
print(something.read())

#reads an individual line, from top to bottom
print(something.readline())

#this will read the second line now
print(something.readline())


#using readlines we can jump to any line in the text
#readlines will have a list with each line being an element:
print(something.readlines())
# we only see the lines yet to be read, so if we've read the first 4
# lines previously, then they won't be part of the array



for line in something.readlines():
        print(line)





something.close()


    #Writing to files
something2 = open("RandomTextFile", "a")

# This will add another line
something2.write("I love my life actually bro")
# the issue with this is that anytime we run the program
#it will append to the line we're currently on, and it doesn't make a new line



# so we need to make a new line
something2.write("\n This a new line and a new day")

something2.close()









#We can also overwrite a file:
something3 = open("RandomTextFile", "w")
something3.write("This is a new file, the old one was completely erased")

# always close file after use
something.close()