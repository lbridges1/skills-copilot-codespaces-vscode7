import random
#write a mini game of rock paper scissors
#player vs computer
#player inputs choice
#computer randomly selects choice
#determine winner
#rock beats scissors
#scissors beats paper
#paper beats rock
#play again
#keep score
#end game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
