running = True
while running:
    CorrectUserInput = False
    while not CorrectUserInput:
        try:
            number = int(input("How many times do you want it repeated?: "))
        except ValueError:
            print("Error please try again")
        else:
            CorrectUserInput = True
    while number > 0:
        print("it")
        number -= 1

# First, the whole code is constantly repeated by a while loop that is always true

# Next, it takes in user input through a try and except statement that fails if the user did not input a number, and this is repeated until they can put in a number

# finally, a while loop repeats it the amount of times that the user specified