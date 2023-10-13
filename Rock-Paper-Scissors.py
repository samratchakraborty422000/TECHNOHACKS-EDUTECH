import random

# heading 
print("WELCOME TO ROCK PAPER SCISSORS GAME\nYOU ARE UP AGAINST THE COMPUTER😊\n")

# type of moves
move= [1,2,3]

# taking input from user
user= int(input("Choose 1.Rock, 2.Paper or 3.Scissors: "))

# Generating random move which is computer's move
computer= random.choice(move)
print(f"computer choose {computer}")

# Compare the moves and determine the winner
if user== computer:
    print("IT'S A TIE! 🥲")
elif user== 1 and computer== 3:
    print("YOU WIN THE GAME! 😊")
elif user == 2 and computer == 1:
    print("YOU WIN THE GAME! 😊")
elif user== 3 and computer== 2:
    print("YOU WIN THE GAME! 😊")
else:
    print("YOU LOSE! 😟")