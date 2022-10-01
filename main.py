# importing random module
import random as rd

# Rules About The Game
print("Rules to conquer stone paper scissor game \n"
      + "stone vs paper -> paper wins \n"
      + "stone vs scissor -> stone wins \n"
      + "paper vs scissor -> scissor wins \n")

# getting rounds details from user
rounds = int(input("Enter Number Of Rounds You need To Play : "))

# assigning default score
userPoint = 0
comPoint = 0

# looping for number of rounds
for i in range(rounds):
    print("Enter choice \n 1 for stone, \n 2 for paper, and \n 3 for scissor \n")
    result = None

    # take the input from user
    choice = int(input("User turn: "))

    # loop for invalid choice
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    # initializing value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'stone'
    elif choice == 2:
        choice_name = 'paper'
    elif choice == 3:
        choice_name = 'scissor'

    # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # Random choices Using randint method of numpy.random module
    comp_choice = rd.randint(1, 3)

    # initializing value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'stone'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    elif comp_choice == 3:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " versus " + comp_choice_name)

    # check of a draw
    if choice == comp_choice:
        print("Draw=> ")
        result = 'Draw'

        # condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins => ")
        result = "paper"
    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins =>")
        result = "Rock"
    elif ((choice == 2 and comp_choice == 3) or
          (choice == 3 and comp_choice == 2)):
        print("scissor wins =>")
        result = "scissor"

    # Printing Result
    if result == 'Draw':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
        userPoint = userPoint + 1
    elif result == comp_choice_name:
        print("<== Computer wins ==>")
        comPoint = comPoint + 1


# conditions for score board
scoreBoard = int(input("Do You wanna View The Score Board? \n1. view\n2.exit\n Enter the choice : "))
if scoreBoard == 1:
    if userPoint > comPoint:
        print("You have Won the game and Scored a point of ", userPoint)
        print("\nThanks for playing")
    elif userPoint < comPoint:
        print("Computer have Won the game and Scored a point of ", comPoint)
        print("\nThanks for playing")
    else:
        print("Match Draw")
        print("\nThanks for playing")

else:
    # Outro
    print("\nThanks for playing")