#Error Handling
#Exceptions handling with try , except,else and finally
#Custome Exceptions

""" 
    NOTES
    Error Handling- Help handle unexpected situations and errors.
    1.Try: contains code that might throw an exception
    NB: If an exception occurs the rest of the code in the try block is skipped or ignored
    2. Except : Catches and handles exceptions.
     - You can specify different handlers for different actions
    
    3. Else: The code runs if no exception occurs
    if no exceptios raised in the try block it runs
    4. Finally: It runs whether an exception is raised / occured or not
    More :
    try/except
        atch and recover from exceptions raised by Python, or by you.
    try/finally
        Perform cleanup actions, whether exceptions occur or not.
    raise
        Trigger an exception manually in your code.
    assert
        Conditionally trigger an exception in your code.
    with/as
        Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).
 """

#EXample 1: Handle exception with division by zero
try:
    number = int(input("Enter the number: "))
    result = 20/number

except ValueError:
    print("Invalid number! please enter a valid number")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")

else:
    print(f"Result is {result}")

finally:
    print("Execution completed successfully")

#exercise 1:write a function that converts a string to an interger and handle
#both value error if a string cannnot be converted to an integer and typeError if the input is not a string
#use multiple except blocks to handle these exeception

def converting_to_integer(value_input):
    try:
        # Attempt to convert the input value to an integer
        result = int(value_input)
    except ValueError:
        # Handle the case where the input value cannot be converted to an integer
        print("ValueError: The input string cannot be converted to an integer.")
        return None
    except TypeError:
        # Handle the case where the input is not a string
        print("TypeError! The input is not a string.")
        return None
    else:
        # If no exception occurs, return the result
        return result
    finally:
        # This block always executes
        print("Execution complete.")

converting_to_integer()


#Example 2:Execption raised for error in the input, if funds are insufficient 

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance 
        self.amount = amount
        self.message = f"attempt to withdraw {self.amount} with only {self.balance}in account"
        super().__init__(self.message)

def withdraw (balance, amount):
    return balance - amount

try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)

except InsufficientFundsError as e:
    print('Error:{e.message}')

else :
    print(f"Withdraw successfull. New balance is {new_balance}")

finally:
    print("transaction complete")


# Note
"""
Summary
Defining a custom excepption
Class Customerror(Exception):
    # Custom exceprtion for specific error cases
    
  def _init_(self, message):
    self.message = message
    super()._init_(self.message)
    
#  rasing a custom exception
def check_value(value):
    if value is < or value:
        raise CustomError('Value can't be negative')
    return value
    
# Handle exceptions with try, except, else and finally
try:
    result = check_value(-10)
except CustomError as e
    print(f"Custom error caught: {e.message}")
"""

#Exercise 2:create a custon exception InvalidAgeError  and write a function that raises 
#this exception if the given age is negative. Handle this custom expection when calling the function.

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age input: {age}. Ones age cannot be negative integer."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return f"This is a valid age: {age}"

try:
    age = -5  # Example of an invalid age
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e.message}")
else:
    print("This age is valid.")
finally:
    print("Age verification completed successfuly.")