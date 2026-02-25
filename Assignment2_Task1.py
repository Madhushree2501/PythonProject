#Check if number is Even or Odd
#Take the number from the user
num = int(input("Enter a number: "))
#Using Arithmetic operator modulus to get remainder and checking it is zero
if num % 2 == 0:
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')