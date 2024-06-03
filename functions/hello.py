def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name} you were born in {2024-age}")

def my_country(country="Uganda"):
    print(f"Hello Akirachix from {country}")   

def greet(name):
    print(f"Hello {name}")  

def greet(*names):
    print(f"Hello{names}") 

def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence 

              
    