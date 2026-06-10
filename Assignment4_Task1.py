# Read a file if exists or else thrown an error
try:
    file = open("sample.txt","rt")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found")
