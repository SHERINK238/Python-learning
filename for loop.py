
countOfStudent=int(input("enter the num of stu in class: "))
studentName=[]
for index in range(0,countOfStudent):
    name=input(f"enter the name of student {index+1}: ")
    studentName.append(name)
#studentName.pop()
#print(studentName)


for printIndex in range(0,countOfStudent):
    print(f"Student {printIndex+1} : {studentName[printIndex]}")

print(studentName[len(studentName)-1])