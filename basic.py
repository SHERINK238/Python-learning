print("HEllO WORLD")


Name="Sherin"
print("Hello",Name)

Name=input("Enter the name of the user: ")
print("Hello",Name)
print(f"Hello \"{Name}\" \n your lucky number is {5*5}")


Name=input("Enter the name of the user: ")
print("Hello",Name)
print(f"Hello {Name} \n your lucky number is {5*5}")

address_identity=id(Name)
print(f"Address of the user saved location {address_identity}")


#binary , hexadecimal , decimal

print(bin(5))
print(hex(15))
print(hex(55))

#ord -ordinal
print(ord('C'))
print(ord('c'))

print(chr(123))
print(chr(122),chr(97))



# num1=45
# num2=90
#
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
if(num1==num2):
    print("Both numbers are equal")
elif(num1>num2):
    print("num1 is greater")
elif(num1<num2):
    print("num2 is greater")


# else:
#     print("Both numbers not are equal")



#only for 0 false all other true including negatives also true
print(bool(5))
print(bool(0)) #false
print(bool('A'))
print(bool(-3))
print(bool(".[]4fgt"))
print(bool(5!=5))  #false
print(bool(5!=6))


a,b=5,10
print(a,b)


userNum=int(input("enter the num to print even num:"))
for i in range(userNum,50,-3):
    if(i%2!=0):
        print(i)


print(hex(55))
print(bool([]))
print(bool(""))
print(bool(None))


#-5 to 256 same address in cd script only not idle python site

s=5
d=5
print(id(s),id(d)) # same add

s=257
d=257
print(id(s),id(d)) # diff add


# num1=45
# num2=90
#
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
if(num1==num2):
    print("Both numbers are equal")
elif(num1>num2):
    print("num1 is greater")
elif(num1<num2):
    print("num2 is greater")


# else:
#     print("Both numbers not are equal")



#only for 0 false all other true including negatives also true
print(bool(5))
print(bool(0)) #false
print(bool('A'))
print(bool(-3))
print(bool(".[]4fgt"))
print(bool(5!=5))  #false
print(bool(5!=6))


a,b=5,10
print(a,b)


userNum=int(input("enter the num to print even num:"))
for i in range(userNum,50,-3):
    if(i%2!=0):
        print(i)




