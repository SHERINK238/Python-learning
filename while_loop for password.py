correctPin = "4321"
userPin = input("Enter PIN: ")

while userPin != correctPin:
    print("Wrong PIN, try again")
    userPin = input("Enter PIN: ")

print("Access granted")