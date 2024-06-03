def add(x,y):
    result=x+y
    return result

def subtract(x,y):
    result = x-y
    return result

def remainder(x,y):
    result = x%y
    return result

def multiply(x,y):
    result=x*y
    return result

def divide(x,y):
    result = x/y
    return result

def power_of(x,y):
    result=x**y
    return result

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
        return total
    
def multiply_many(*numbers):
    total = 1
    for number in numbers:
        total *= number 
        return total  

def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total +=x
    f = kwargs["first_name"]  
    l = kwargs["last_name"]  
    greetings = f"Hello{f}{l} the sum of your numbers is{total}"
    return greetings  

students = [{"age":19, "name":"Eunice"},
            {"age":21, "name":"Agnes"},
            {"age":20, "name":"Amanda"},
            {"age":22, "name":"Asha"}] 
def greetings():
    print(f"Hello,{name},you were born in the year{2024-age}")
   