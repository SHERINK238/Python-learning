print("HEllO WORLD")

userName = "Sherin"
print("Hello", userName)

userName = input("Enter the name of the user: ")
print("Hello", userName)
print(f"Hello \"{userName}\" \n your lucky number is {5*5}")


userName = input("Enter the name of the user: ")
print("Hello", userName)
print(f"Hello {userName} \n your lucky number is {5*5}")

memoryAddress = id(userName)
print(f"Address of the user saved location {memoryAddress}")


# binary, hexadecimal, decimal

number = 5
print(bin(number))
print(hex(15))
print(hex(55))


# ord - ordinal
print(ord('C'))
print(ord('c'))

print(chr(123))
print(chr(122), chr(97))


# Comparing two numbers

firstNumber = int(input("Enter the num1:"))
secondNumber = int(input("Enter the num2:"))

if firstNumber == secondNumber:
    print("Both numbers are equal")
elif firstNumber > secondNumber:
    print("num1 is greater")
elif firstNumber < secondNumber:
    print("num2 is greater")


# Boolean values
# Only 0 is False. All other numbers, including negatives, are True.

print(bool(5))
print(bool(0))  # False
print(bool('A'))
print(bool(-3))
print(bool(".[]4fgt"))
print(bool(5 != 5))  # False
print(bool(5 != 6))


# Multiple variable assignment

firstValue, secondValue = 5, 10
print(firstValue, secondValue)


# Printing even numbers

startingNumber = int(input("Enter the num to print even num:"))

for currentNumber in range(startingNumber, 50, -3):
    if currentNumber % 2 != 0:
        print(currentNumber)
