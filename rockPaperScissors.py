import random

gameRunning = True

# create scores
computerScore = 0
userScore = 0

while gameRunning == True:

    # we need a choice of rock, paper or scissors from the user
    userChoice = input("Welcome to my game of rock, paper, scissors! \n Please choose an option: ")

    print("You chose: ", userChoice + ".")
    userChoice = userChoice.lower()

    # we need a choice of rock, paper or scissors from the computer - change this to a random choice
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    print("Computer chose: " + computerChoice + ".")

    # compare choices to see who wins
    if (userChoice == "rock" and computerChoice == "rock"):
        print ("Tie.")
    elif (userChoice == "scissors" and computerChoice == "scissors"):
        print ("Tie.")
    elif (userChoice == "paper" and computerChoice == "paper"):
        print ("Tie.")
    elif (userChoice == "rock" and computerChoice == "scissors"):
        print("You win.")
        userScore += 1
    elif (userChoice == "paper" and computerChoice == "rock"):
        print ("You win.")
        userScore += 1
    elif (userChoice == "scissors" and computerChoice == "paper"):
        print ("You win.")
        userScore += 1
    elif (userChoice == "paper" and computerChoice == "scissors"):
        print ("Computer wins.")
        computerChoice += 1
    elif (userChoice == "rock" and computerChoice == "paper"):
        print ("Computer wins.")
        computerChoice += 1
    elif (userChoice == "scissors" and computerChoice == "rock"):
        print ("Computer wins.")
        computerChoice += 1
    # else:
    #     print (userChoice + " is not a valid option. Please chose either rock, paper or scissors.")

    # display the scores
    print("The score is: Computer ", computerScore, "-", userScore, " User")

    quitting = input("Do you want to continue? Yes or no")
    quitting = quitting.lower()

    if quitting == "no":
        gameRunning = False

    print("Thank you for playing my game")