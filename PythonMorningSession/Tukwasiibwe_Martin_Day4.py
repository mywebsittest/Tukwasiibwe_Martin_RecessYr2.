#Dictionaries
#Crreating and using dictonaries
#Dictionary methoda and operations

"""
Dictionaries in python are collections of keys and values.
-unordered 
-mutable 
-indexed by keys 
"""

#Example 1: creating a dictionary 
#create a dictionary for a student persuing software engineering ,
#the key must be your name ,age ,technology interest and year of study
#put your own details 

student_dictionary = {
"name": 'Tukwasiibwe Martin',
"age": "26",
'technology': 'Machine Learning',
'course': 'Software Egineering',
'year': 'Two'
}

print(student_dictionary['age'])

#modify values
#Exerise 1: modify age and tech

student_dictionary['age'] = '43' 
student_dictionary['technology'] = 'Artificial Intelligence, Machine Learning, and Data Science' 
print(student_dictionary)

#Example2 : adding keys and values 
student_dictionary['email']='siibwemart@gmail.com'

print(student_dictionary)

# Excersice 2:remove a key and value

#removed_value = student_dic.pop('course')#
del student_dictionary['year']

print(student_dictionary)

#execrise 3.. use the upadate method to update the age 
student_dictionary.update({'age':'29'})

#Exercise 4: use the if to check if the key 'age' is present 
#in the dictionary

if 'age' in student_dictionary:
 print(f"The key 'age' is present in the dictionary with the value: {student_dictionary['age']}")
else:
 print("The key 'age' is not present in the dictionary.")

#key(), value(), and items() methods
print(student_dictionary.keys())
print(student_dictionary.values())
print(student_dictionary.items())

"""
keys() returns a view of objects that displays alist of all keys
values() returns a view of objects that displays a list of all values
items() retuns a view of objects that displays a list of dictionary keys and 
value tuple pairs
"""

#Exercise 5: use the update method to change the course and add a new key "whatsApp number" 
#to the dictionary

student_dictionary.update({'course': 'BIST', 'WhatsApp': '0752912609'})

# Print the updated dictionary
print(student_dictionary)

