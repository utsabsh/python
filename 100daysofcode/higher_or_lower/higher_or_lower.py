from art import *
import random
from data import data
import os

# Clear the console
clear = lambda: os.system('cls')
clear()

score = 0

# Display logo
print(logo)

# Format account data
def format_data(account):
    account_name = account["name"]
    account_desct = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {account_desct}, from {account_country}")

# Check answer
def check_Answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Set account A as the previous account B
    account_a = account_b

    # Select a new random account for B
    account_b = random.choice(data)
    
    # If account A and B are the same, select a new account for B again
    if account_a == account_b:
        account_b = random.choice(data)

    # Display account information for comparison
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Prompt user to guess which account has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get the follower count for both accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    clear()
    
    # Display logo
    print(logo)
    
    # Check if the user's guess is correct and update the score
    is_correct = check_Answer(guess, a_follower_count, b_follower_count)
    
    if is_correct:
        score += 1
        print(f"You are right! Your current score: {score}")
    else:
        print(f"Sorry, you are wrong! Final score: {score}")
        game_should_continue = False
