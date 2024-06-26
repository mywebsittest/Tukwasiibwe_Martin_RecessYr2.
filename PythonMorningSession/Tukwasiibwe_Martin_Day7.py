#Inheritance and polymorphism
"""
Inheritance and Method overriding
Polymorphism and Method resolution
order
Abstract classes and interfaces
"""

#Inheritance and method overriding 
"""
--Description
Inheritance and method overriding allows a class(child class) to 
inherit attributes from another class(parent class).
Key concepts
Base class(parent classs): A class whose properties are inherited by another class.
Derived class (child class): Class that inherits attributes and properties from parent class
"""

#Example 1 : syntax Create a class where a dog inherits from animal and overrides with speak method 
class Animal:
    def speak(self):
        return'Mwe Mwe Mwe Mwe'

class Dog(Animal):
    def speak(self):
        return 'Barks'

#implementation of inherited class

animal = Animal()
dog = Dog()

print(animal.speak())

#polymorphismto 
#polymorphism allows objects of different classes be treated as objects of a commom super class
#Method resolution order (MRO). is order in which python looks for a method in a hierarchy classes

#Example 2:How polymorphism works in python 

class Animal:
    def speak(self):
        return'Croock'

class Dog(Animal):
    def speak(self):
        return "Barks"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())

#Exercise 1: Create a simple application to manage different types of vehicles .Implement
#derived clss to demonstrate inheritance and polymorphism.
"""
Requirements
1.Base class to vehicle
Attributes:make, model and year
Method :display_info()
2.Drived classes:
Car: inherit from Vehicle
attributes: number_of_doors
overrides: display_info()
Motocycle: inherit from vehicle
Attributes , type_of_bike(cruiser, sport,touring)
override: display_info()
#Exercise 2:Create a function that accepts a list of vehicles objects and call 
their display_info() methid to print details of each vechile.
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.type_of_bike}")

def display_vehicles_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print("-" * 20)

# Example usage
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 2021, "Sport")

vehicles = [car, motorcycle]
display_vehicles_info(vehicles)


"""
Working with text files 
Handling csv files
JSON and XML file processing 
"""

#1.Working with text files, open, read, write and close
#Note: Python provides inbuilt functions to hadle text files 
#key concepts 

"""
opening File : open() function(r, w, a r+)
Reading File: read() function
Writing File : write() function
close file: close() function
"""
#Example 3: Write a file and read a file 

#writing to a text file
with open("tukwasiibwe.txt","w") as file:
    file.write('I am Tukwasiibwe and I love python.\n')
    file.write('I use python for automation')

#Reading from a text file 

with open('tukwasiibwe.txt', 'r') as file:
    content = file.read()
    print(content)

#Handling csv files
"""
CSV(Commo Separated Values) file widely for data exchange .
Key Concepts:
Read CSV files: Using 'csv.reader()'
writing CSV file: Using 'csv.writer()'
DictReader and DictWriter: the class read and write CSV file as dictionaries 
"""

#Example 4: writing and Reading CSV file

import csv

#writing to a csv file
with open ('tukwasiibwe.csv', 'w', newline='') as csv_file:
    writer= csv.writer
    writer.writerow(['name','position','course'])
    writer.writerow(['v','student','BSE'])
    writer.writerow(['jeff Geoff','Lecture','BSE'])

#read from the csv file 
with open('tukwasiibwe.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

#JSON and XML file processing 
"""
JSON (Javascript Object Notation) and XML (eXtensible Markup Language) are formats used to
structure data.
Key Concepts 
Loading JSON data: using json.load() for reading JSON file 
Dumping JSON Data: using json.dump() for writing JSON file
Parsing JSON Fata: using json.loads() for handling JSON strings
"""

#Example 6: write and read JSON file
import json

#writing to a JSON file

student_data = {
    'name':'tukwasiibwe',
    'course':'BSE',
    'year':'year 2'
}

#open the file 
with open('student_data.json','w') as json_file:
    json.dump(student_data, json_file)

#Reading the JSON file
with open('studend_data.json','r') as json_file:
    student_data = json.load(json_file)
    print(student_data)

#Execrise 2: Write and read the xml file
#Execise 3: Using abstraction calculate the area and perimeter of rectangle

"""
Write and Read an XML File
"""
import xml.etree.ElementTree as ET

# Creating the data
student_data = ET.Element('student')
name = ET.SubElement(student_data, 'name')
name.text = 'tukwasiibwe'
course = ET.SubElement(student_data, 'course')
course.text = 'BSE'
year = ET.SubElement(student_data, 'year')
year.text = 'Year 2'

# Writing to an XML file
tree = ET.ElementTree(student_data)
with open('student_data.xml', 'wb') as xml_file:
    tree.write(xml_file)


# Reading the XML file
tree = ET.parse('student_data.xml')
root = tree.getroot()

student_data = {}
for elem in root:
    student_data[elem.tag] = elem.text

print(student_data)

"""
 Using Abstraction to Calculate the Area and Perimeter of 
 a Rectangle
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")