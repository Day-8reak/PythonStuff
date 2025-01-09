# not all things can be represented with strings,
# numbers, and booleans

# with classes we can define our own datatypes, let's say a student data type:
class student:
    #this is python's version of a constructor
    def __init__(self, name, major, gpa, is_on_probation, course1, course2, course3, course4): # an initialize function which defines what students are
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4

    #class functions are functions you can use in a class
    #like normal functions but for specific classes
    def on_honour_roll(self): # always need to put self as a parameter for these functions
        if self.gpa >= 3.5:
            return True
        else: 
            return False


# inheritance is where another class inherits everything from another class
# generally great for when we have a subcategory of a thing (class car, and then 
# subarus are a subclass of cars)

#inheritance:
class ComputerScienceStudent(student):
    # we can override a previous function:
    def on_honour_roll(self): 
        if self.gpa >= 3.7:
            return True
        else: 
            return False
    
