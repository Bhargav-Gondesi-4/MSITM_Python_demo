#Exercise 1: Calculate the Sum of Two Numbers using the Psudeo code given
first = float(input('Enter the first number:'))
second = float(input('Enter the second number:'))
sum_result= first+second
#printing the result
print('The sum of given numbers=',sum_result)



#Exercise 2: Find the Maximum of Three Numbers using the pseudo code given
#collecting the input
num_1 = float(input('enter the first number:')) 
num_2 = float(input('enter the second number:'))
num_3 = float(input('enter the third number:'))
# comparing the numbers
if(num_1>num_2):
    if(num_1>num_3):
        print(f'{num_1} is the greatest of the three.')
    else:
        print(f'{num_3} is the greatest of the three.')
else:
    if(num_2>num_3):
        print(f'{num_2} is the greatest of the three.')
    else:
        print(f'{num_3} is the greatest of the three.')


#Exercise 3: Print a List of Numbers from 1 to N  using the given psudeo code
n = int(input('Enter the value of n:'))
#creating the loop for printing the values
for i in range(1,n+1):
    print(i)


#Exercise 4: Calculate the Factorial of a Number using the given pseudo code
#defining the function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
#taking the input and finding out the factorial
n=int(input('enter the desired number:'))
result = factorial(n)
print(f'The factorial of {n} = {result}')
