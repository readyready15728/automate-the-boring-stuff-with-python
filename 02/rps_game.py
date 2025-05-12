import random
import sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:  # The main game loop
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")
        player_move = input()

        if player_move == "q":
            sys.exit()  # Quit the program
        if player_move in ("r", "p", "s"):
            break  # Break out of the player input loop
        print("Type one of r, p, s or q.")

    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS versus...")

    # Display what the computer chose
    random_number = random.randint(1, 3)

    if random_number == 1:
        computer_move = "r"
        print("ROCK")
    elif random_number == 2:
        computer_move = "p"
        print("PAPER")
    elif random_number == 3:
        computer_move = "s"
        print("SCISSORS")

    # Display and record the win/loss/tie
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins += 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins += 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins += 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses += 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!")
        losses += 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses += 1
