# Can use python read command
# this allows us to open, read


# using the open command depends on the location
# of the file and other specifics
something = open(RandomExternalFile, "r") #a = append, w = write, r = read, r+ = reading and writing
# can be file name if python program and file in the same directory
# Otherwise it'll be a relative/absolute path to file
# the second part determines what permissions we have with the file



# we should always check if a file is readable before we check it:
print(something.readable())




# always close file after use
something.close

# for instance