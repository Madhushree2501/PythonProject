# Read a file if exists or else thrown an error
try:
    with open("sample.txt","rt") as file:
        content = file.read()
    print(content)

except FileNotFoundError:
    print("The file 'sample.txt' was not found")
