# Rock-paper-scissors game
import random

# The possible choices
choices = ['rock', 'paper', 'scissors']

def play_game():
  # Get the user's choice
  user_choice = input("Enter your choice: ")

  # Make sure the user entered a valid choice
  while user_choice not in choices:
    print("Invalid choice. Try again.")
    user_choice = input("Enter your choice: ")

  # Get the computer's choice
  computer_choice = random.choice(choices)

  # Compare the choices and determine the winner
  if user_choice == computer_choice:
    print("Computer chose "+computer_choice+" It's a tie!")
  elif (user_choice, computer_choice) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
    print("Computer chose "+computer_choice+" You win!")
  else:
    print("Computer chose "+computer_choice+" You lose")

while True:
  print("Choices:", ', '.join(choices))
  play_game()

  # Ask the user if they want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() != 'y':
    break

print("Thanks for playing!")
