# Takes the input to file from user and append the file and display the final content
user_input = input("Enter text to write to file:")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
with open("output.txt", "a") as file:
    file.write("Learning the file handling in Python")
with open("output.txt", "r") as file:
    finalContent =file.read()

print(f"Final Content of output.txt file:\n{finalContent}")

