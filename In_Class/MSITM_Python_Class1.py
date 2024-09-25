# 1. Basic Syntax and variables
name = 'Bhargav Gondesi'
age = 25
print(f"Hello my name is {name} and I am {age} years old")



#2.  Area of Rectangle
length = 11.27
width = 6.96
area = length * width 
print("The area of the rectangle is ",area)



#3. Control Structures(if-else)
a = int(input('Enter a number:'))
if (a<0):
    print('The given number is negative')
elif(a==0): 
    print('The given number is neutral')
else:
    print('The given number is positive')



#4. Control Structures(Loops)
for i in range(1,11):
    print(i)



#5. Function
# Function declaration
def add(a,b):
    return a+b
# Function call
n=int(input('enter the first number: '))
p=int(input('enter the second number: '))
c = add(n,p)
print(f'the sum of the {n} and {p} =',c)


#6. Class Intro + Homework Assignment
# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity
        self.quantity += amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Not enough {self.name} in stock to sell {amount}.")
        else:
            self.quantity -= amount
            print(f"Sold {amount} of {self.name}. Remaining quantity: {self.quantity}")
    
    def add_stock(self,amount):
        self.quantity +=amount
        print(f"Updated {self.name}. Remaining quantity: {self.quantity}")
    
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

# Creating a product instance
laptop = Product(name="Dell", price=1200.00, quantity=10)
print(laptop)
laptop.add_stock(7)
print(laptop)
print(f"the total value {laptop.name} = $ {laptop.get_total_value()}")