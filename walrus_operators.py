correctPin = "4321"

# userPin = input("Enter PIN: ")

# while userPin != correctPin:

while (userInput := input("Enter PIN: ")) != correctPin:
    # Assignment of input to userInput and returning the value
    # to the larger expression
    print("Wrong PIN, try again")
    userInput = input("Enter PIN: ")

print("Access granted")