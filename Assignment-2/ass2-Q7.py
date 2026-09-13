while True:
    value = input("Enter a number or type Quit: ")

    if value == "Quit":
        print("Program ended.")
        break

    num = int(value)

    if num > 0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("You have entered zero")



        








