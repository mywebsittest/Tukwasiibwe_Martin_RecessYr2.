#Python best practices


#Python operators
"""
+    Addition    x + y    
-    Subtraction    x - y    
*    Multiplication    x * y    
/    Division    x / y    
%    Modulus    x % y    
**    Exponentiation    x ** y    
//    Floor division    x // y  
"""
#Example of Python logical operators
"""
Name of the operator    Example Symbol
and                     and 
or                      or 
not                     not 

#Example Python Bitwise Operators
Name   Sybmol with Examples
AND      & 
OR       |
XOR      ^
NOT      ~

#Python cases
1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. lowercase
"""
"""
=    Assignment    x = 5    
==    Equal    x == y    
!=    Not equal    x!= y    
>    Greater than    x > y  
"""
"""_summary_
Name of the operator    Symbol for
"""
"""_summary_
Comprensions provide a concise way to create lists and dictionaries
What is the symbol for
lists           [] square brackets // Used to store multiple items in a single variable
dictionaries    {} curly brackets used to store data values in keys: value pairs
"""
#Example 1: Basic List Comprensions
list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

#creat
#even_squares[x**2 for x inrange(20) if x % 2 == 0]

#print(even_squares)

#Create a dictionary comprehensions for my favorite cars and count the length of charactors
favorite_cars = {
    "BMW", "Toyota","Honda", "Nissan", "Ford"
}
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)

#Exercise 2: Create a list of tuple where each tuple contains a number and cube for numbers
#between 1 and 10 using a dictionary comprehension.
cubes_of_numbers = {x: x**3 for x in range(1, 11)}
print(cubes_of_numbers)



