#Defining Functions
#Function syntax and parameters
#Return values
#Lambda functions
#functions in python are defined using the 'def' keyword , followed by function name
#parentheses (), inside the parentheses you put a paramter name and the colon

#Example 1:
def multiply(a, b):
    return a * b

result = multiply(5,4)
print(result)


#Example 2: Multiple return values

def get_coordinates():
    return 10, 20
x, y = get_coordinates()
print(x, y)

#Exercise 1: Define a function greet with a parameter name , set to 'guest" and print a message 
#i am a software programmer

def greet(guest):
    print(f"{guest}, I am a software programmer")
greet("Martin")

#Example 3:return multiple values 
def get_name_and_position():
    name ='Martin,'
    position = 'Software programmer'
    return name, position
    
name, position = get_name_and_position()
print(name,  position)

#Exercise 4: Return multiple of you name and age

def  get_name_and_age():
    name = 'Martin'
    age = 26
    return name, age
name, age = get_name_and_age()
print(name, age)

#note
"""
def: keyword to define a functoion 
function_name: Name of the function
parameters: Optional, arguments passed to the function
Docstrings: Optional , describes the function purpose
return: optional, returns a value from the function
   
"""

#syntax for defining a function 
# def function_name(parameters):
#     """Docstring Option"""
#     function body
#     return value

# Lambda function
#Lambda functions are small anonymous functions defined using the lambda keyword
#They are restricted to a single expression

#syntax for lambda function 
#lambda parameter: expression

#Example 5: Create a lambda function to add two numbers 

add = lambda a, b: a + b

def add(a, b): return a + b

print(add(45, 70))


#Example 6: use cases of lambda function for sorting 
coordinates=[(1,2),(2,3),(3,1),(5,0)]

coordinates.sort(key = lambda coordinate: coordinate[1])
print(coordinates)

#Map, filter and reduce 
#Example 7:get the squares of 1 to 5 using map , filter and reduce

number_squares = [1, 2, 3, 4, 5]

square = list(map(lambda x: x**2, number_squares))

print(square)

#Exercise 4:Define a function to get user info that accepts arbitrary keyword arguments and prints 
#each key value pair

def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#usage of the function
get_user_info(name = 'Tukwasiibwe', age = 33, tech = 'Data structures and Web development', course = 'BSSE', year='Two')

#Example 8: how to handle a **kwargs in Functions

def ahaabwe_function (a, b, **kwargs):
    print(f"a: {a}, b:{b}")
    
    for key, value in kwargs.items():
        print(f"{key}:{value}")


ahaabwe_function(1, 2 , x = 100, y = 3)





