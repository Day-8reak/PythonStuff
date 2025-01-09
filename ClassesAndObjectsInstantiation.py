from ClassesAndObjects import student
#we're importing specifically the student class from
# the ClassesAndObjects file
 
student1 = student("Aiden Henderson", "Computer Science", 12, False, "Concurrent Systems", "Linear Algebra", "Databases", "Automata and Computability")
student2 = student("Maxwell Huang", "Computer Engineering", 2, True, "Concurrent Systems", "Linear Algebra", "Databases", "Automata and Computability")


print(student1.gpa)


# We absolutely can have a class and instances of that class in the
# same file, generally we avoid that though because of modularization
class Question:
    def __init__(self, prompt, answer, weight):
        self.prompt = prompt
        self.answer = answer
        self.weight = weight

questions = [
    Question("Is Aiden Henderson a 10/10 \n (a) no he's ugly af \n (b) yeah he's so hot \n (c) 10/10?? He's the sexiest man alive \n \n", "c", 99),
    Question("Is Maxwell Huang a 10/10 \n (a) no he's ugly af \n (b) yeah he's so hot \n (c) 10/10?? He's the sexiest man alive \n\n", "b", 99)
]

print(questions[1].weight)