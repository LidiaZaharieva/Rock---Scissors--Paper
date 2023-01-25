import random

wins = 0
loses = 0
draws = 0

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Choose [r] ->rock, [p] -> paper, [s] -> scissors:")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    random_number = random.randint(1, 3)

    pc_move = ""

    if random_number == 1:
        pc_move = "Scissors"
    elif random_number == 2:
        pc_move = "Rock"
    elif random_number == 3:
        pc_move = "Paper"

        print(f"The computer chose {pc_move}.")

    if player_move == pc_move:
        draws += 1
        print("Draw")
    elif player_move == rock and pc_move == scissors or player_move == paper and pc_move == rock or \
          player_move == scissors and pc_move == paper:
        wins += 1
        print("You Win")
    else:
        loses += 1
        print("You Lose")

    print(f"You Win: {wins} | You Lose: {loses} | Draws: {draws}")
