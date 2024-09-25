# Exercise 1: Reuqest user input and print a greeting
# Print a greeting message using the user's name
print("Exercise 1:")
a = input('Please state your name:')
print(f'Hello {a}!')
print("\n\n")

# Exercise 2: Variables and Data Types
# Create two drinks variable (Milk and Water) and swap their values
# Print the old and new values of the variables
print("Exercise 2:")
drink1='Milk'
drink2= 'Water'
print(f"Drinks before swapping drink1 = {drink1}, and drink2 = {drink2}")
drink1,drink2= drink2,drink1
print(f"Drinks after swapping drink1 = {drink1}, and drink2 = {drink2}")
print("\n\n")


# Exercise 3: String Concatenation
# Create two variables with your first and last name, and print them together
print("Exercise 3:")
first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")
print(f"Hello{first_name+last_name}")
print("\n\n")


# Exercise 4: Simple Arithmetic
# Perform basic arithmetic operations and print the results
# Addition, Subtraction, Multiplication, Division
print("Exercise 4:")
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))
print(f"the sum of {num1}+{num2} = {num1+num2}")
print(f"the difference between {num1} and {num2} = {num1-num2}")
print(f"the product of {num1} and {num2}= {num1*num2}")
print(f"{num1}/{num2} = {num1/num2}")
print("\n\n")


# Exercise 5: Lists
# Create a list of 5 numbers and print the first and last element
print("Exercise 5:")
l = [90,98,97,99,86]
length = len(l)
print(f"the first element of  the give list is {l[0]} and the last element of the given list is {l[length-1]} ")
print("\n\n")


# Exercise 6: For Loop
# Use the list from Ex.5. Print each element in the list of numbers using a for loop
print("Exercise 6:")
l = [90,98,97,99,86]
for i in l:
    print(i)
print("\n\n")


# Exercise 7: If-Else Condition
# Write an if-else statement to check if a number is greater than or equal to 10
print("Exercise 7:")
num = int(input('enter a number:'))
if num>10:
    print(f"the given number {num} is greater than 10.")
elif num ==10:
    print(f"the given number {num} is equal to 10.")
else:
    print(f"the given number {num} is less than 10.")
print("\n\n")

# Exercise 8: Functions
# Create a function that takes a name as input and prints a greeting
print("Exercise 8:")
def greet(name):
    print(f"Hello {name}!")
name1 = input('enter your name:')
greet(name1)
print("\n\n")

# Exercise 9: Dictionaries
# Create a dictionary with three key-value pairs and print the value of one key
print("Exercise 9:")
dictionary = {'name':'Bhargav','age':25,'gender':'male'}
key = list(dictionary.keys())
print(f"one of the key in the key value pairs is {key[0]}")
print("\n\n")

# Exercise 10: While Loop
# Write a while loop that prints numbers from 1 to 5
print("Exercise 10:")
i = 1
while i <6:
    print(i)
    i=i+1 
print("\n\n")

# Exercise 11: String Formatting
# Task: Format the following variables into a string: "name", "age", and "city"
# Example output: "John is 30 years old and lives in New York."
print("Exercise 11:")
name = input("enter the name:")
age = int(input('enter the age:'))
city = input('enter the city where you live:')
print(f"{name} is {age} years ols and lives in {city}")
print("\n\n")

# Exercise 12: Function with Default Arguments
# Task: Write a function that takes two numbers and an optional operation (add, subtract, multiply, divide).
# If no operation is provided, it defaults to addition.
print("Exercise 12:")

def calculate(num1, num2, operation):
    if operation == 'subract':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        return num1/num2
    else:
        return num1+num2
n1 = int(input('enter the first number:'))
n2 = int(input('enter the second number:'))
op = input('enter the operation name:')
calculate(n1,n2,op) 
# Example usage:
# print(calculate(5, 3))  # Expected output: 8
# print(calculate(5, 3, "subtract"))  # Expected output: 2
print("\n\n")

# Exercise 13: Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# Task: Create a list of years [1990, 1991, 1992, 1993, 1994, 1995] and generate a new list with the approximate age of a person born in that year.
# To generate a new list, start with an empty list [], and use append() to add elements to it.
print("Exercise 13:")
years = [1990,1991,1992,1993,1994,1995]
current_age =[]
for i in years:
    age = 2024 - i
    current_age.append(age) 
for i in range(0,len(years)):
    print(f"year = {years[i]}, approximate age ={current_age[i]}")
       