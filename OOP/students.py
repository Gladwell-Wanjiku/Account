# class Student:
#     name = "Raziah"
#     code = "004"
#     school = "Akirachix"
#     age = "20"

class Student:
    school = "Akirachix"
    def __init__(self, first_name, last_name,age,country,code):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
        self.country = country
        self.code =  code

def greet_student(self):
    greeting = f"Hello {self.first_name}, welcome to {self.school} your code is {self.code}"
    return greeting
def display_initials(self):
    initial = f"Your initials are {self.first_name[0],self.last_name[0]}"



        
