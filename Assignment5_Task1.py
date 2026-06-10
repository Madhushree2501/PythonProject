#Creating the Dictionary of the Student marks amd takes the student name from user and display the marks.
Student_marks = {'Alice':85, 'Mark':90, 'Peter':80}
Student_name = input('Enter Student Name: ')
if Student_name in Student_marks:
    print(Student_marks[Student_name])
else:
    print('Student Not Found')
