"""
Control Structures
Loops (for, while)
Comprehensions (list, dictionary,Comprehentions)
"""
age = 31
if age<18:
    print("You are not an adult")
elif age > 65:
    print("You are senior citizens")
else:
    print("You are a youth ")

grade = 88 

if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else: 
    print("Not good grade")


"""
children under 13 get discount for price = shs 1000
Teenagers between 13 and 18 get discount for price = shs 500
Adults above pay full price = shs 2000
otherwise senior citizen pay full price = shs 5000
"""
age = int(input("what is your age: "))
price = 2000

if age >=60:
    print(price + 3000)
elif age >= 18:
    print(price)
elif age >= 13:
    print(price-500)
else:
    print(price-1000)

#loops (for, while)
"""
for loop iterates over a sequence (list, tuple , dictionary,set string)
the while loop repeates as long as  a condition is met
"""

# Example 

cars = ['Audi', 'Tyota' 'BMW', 'Subaru','jeep', 'Tesla' 'RangRover']

for car in cars :
    print(car)

#Example 4 count 1 t0 10

count = 1
while count <= 10:
    print("count 1 to 10", count)
    count +=1



#Exercise 
"""
1.create your own list of favorite colors using for loop
2.create a reverse of the input 12345 to be 54321 using while loop
"""

#For number 1:
my_favorite_colors = ['Black', 'Yelow', 'Green','red','Orange']

for color in my_favorite_colors :
    print (color)

# reversed_list = my_favorite_colors[::-1]
#    for col in reversed_list:
#        print(col)

#Number 2

count = 5
while count >= 1:
    print(count)
    count -=1 
