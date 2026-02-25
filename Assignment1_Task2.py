#Create the personalized greeting
#Take the First name and last name from user
fName= input("Enter your first name: ")
lName= input("Enter your last name: ")
#Storing both First and last name in variable
name = fName + " " + lName + "!"
print("Hello,",name,"Welcome to Python program.")

#Using format string
print(f"Hello, {fName} {lName}! Welcome to Python program.")
