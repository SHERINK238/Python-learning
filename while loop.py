countOfStudent=int(input("enter the num of stu in class: "))
i=1
studentName=[]
while(i<=countOfStudent):
    name=input(f"Enter the name {i} ")
    studentName.append(name)
    i=i+1

prtIndex=0
count=len(studentName)
while(count>0):
    print(f"Enter the name of student {prtIndex+1}: {studentName[prtIndex]}")
    prtIndex=prtIndex+1
    count-=1