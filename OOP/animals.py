class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass

class Bird(Animal):
        def make_sound(self):
            print("chirp")
        def move(self):
            print("The bird is flying")
class Fish(Animal):
     def make_sound(self):
          print("click")
     def move(self):
          print("swimming")
class Dog(Animal):
     def make_sound(self):
          print("barking")
     def move(self):
          print("The dog is running")
class Human(Animal):
     def drink(self):
          print("Drinking water")
     def move(self):
          print("walk")
     def make_sound(self):
          print("Talk") 

          
def calculate_total_score(student_data):
    for student in student_data:
        total_score = sum(student['scores'])
        student['total_score'] = total_score
    return student_data


student_data = [
    { 'name': 'John', 'scores': [90, 80, 85] },
    { 'name': 'Jane', 'scores': [95, 92, 88] },
    { 'name': 'Jim', 'scores': [70, 80, 75] },
    { 'name': 'Jill', 'scores': [85, 90, 84] }
]
result = calculate_total_score(student_data)
for student in result:
    print(f"{student['name']}'s total score is {student['total_score']}")    
                                         

