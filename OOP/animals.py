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
                                         

