# Basically dictionaries are like arrays, but instead of each
# value having a corresponding index, it has a key, which is how we identify it

# for instance we can have keys of the shortened month name, and then the values are the full months:
# We could also have the month's numerical value, but then it would be similar
#to an array
MonthConversions = { # All keys must be unique
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}
#
print(MonthConversions["Feb"])