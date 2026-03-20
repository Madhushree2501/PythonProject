#This program gives the factorial number for provided number.
#The factorial of a number is the product of all positive integers less than or equal to that number.
#Taking the number from  the user
num = int(input("Enter the number: "))
#Here defining the recursive function to check upto base
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(f"Factorial of {num} is:",factorial(num))