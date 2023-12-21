import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: )")
    computer_choice = random.choice(["rock","paper","scissors"])
    choices = {"player": player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return f"It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return f"Rock smashes scissors! You Win!"
        else:
            return f"Paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return f"Scissors cuts paper! You lose."
        else:
            return f"Paper covers rock! You win!."
    elif player == "scissors":
        if computer == "paper":
            return f"scissors cuts paper! You Win!"
        else:
            return f"rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
    





