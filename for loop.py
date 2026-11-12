totalStudents = int(input("Enter the number of students in the class : "))

studentsList = []

for studentIndex in range(totalStudents):
    student = input(f"Enter the name of Student {studentIndex+1} : ")
    studentsList.append(student)

studentsList.pop()
print(studentsList)

for displayIndex in range(len(studentsList)):
    print(f"Student {displayIndex+1} : {studentsList[displayIndex]}")

# print(studentsList[len(studentsList)-1])