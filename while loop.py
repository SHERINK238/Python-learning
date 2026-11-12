totalStudents = int(input("Enter the number of students : "))
currentIndex = 0
studentsList = []

# range(start - 0 default, stop - mandatory, increment - optional (default =1))
while(currentIndex <= totalStudents-1):
    student = input(f"Enter the name of student {currentIndex} : ")
    studentsList.append(student)
    currentIndex = currentIndex + 1

displayIndex = 0
remainingCount = len(studentsList)

while(remainingCount > 0):
    print(f"Enter the name of student {displayIndex} : ", studentsList[displayIndex])
    displayIndex = displayIndex + 1
    remainingCount = remainingCount - 1