#Julian Lizarraga, Darris Aguilar
#2/5/2025
#Lab 2

import random  # Importing random module for computer's choice
import Check_input  # Importing custom module for user input validation


def display_scores(p_score, c_score):
    """Displays the current scores of the player and the computer."""
    print(f"Player Score: {p_score}, Computer Score: {c_score}")


def weapon_menu():
    """Displays a menu for the player to choose a weapon and returns the selected weapon."""
    while True:
        user_choice = input("Choose your weapon:\nEnter \nR for Rock, \nP for Paper, \nS for Scissors, \nB for Back: ").upper()
        if user_choice in ['R', 'P', 'S', 'B']:
            print(f"You chose {user_choice}")
            return user_choice  # Return valid weapon choice
        print("Invalid choice. Please enter R, P, S, or B.")


def comp_weapon():
    """Randomly selects a weapon for the computer and returns it."""
    comp_choice = random.choice(['R', 'P', 'S'])
    print(f"Computer chose {comp_choice}")
    return comp_choice  # Return computer's choice


def find_winner(player, comp):
    """Determines the winner of a round based on player and computer choices."""
    if player == comp:
        print("Tie")
        return 0  # Tie
    elif (player == 'R' and comp == 'S') or (player == 'S' and comp == 'P') or (player == 'P' and comp == 'R'):
        print("Player wins")
        return 1  # Player wins
    else:
        print("Computer wins")
        return 2  # Computer wins


def play_rock_paper_scissors():
    """Main function to run the Rock-Paper-Scissors game."""
    print("-Rock-Paper-Scissors-")
    p_score, c_score = 0, 0  # Initialize player and computer scores

    while True:
        # Display game menu and get user choice
        print("RPS Menu:")
        user_action = Check_input.get_int_range("Enter a choice \n1. Play game.\n2. Show Score.\n3. Quit. \n", 1, 3)

        if user_action == 1:
            # Loop for playing rounds of the game
            while True:
                user_weapon = weapon_menu()  # Get player's weapon choice
                if user_weapon == 'B':  # Allow player to go back to menu
                    break
                comp_choice = comp_weapon()  # Get computer's weapon choice
                winner = find_winner(user_weapon, comp_choice)  # Determine winner
                if winner == 1:
                    p_score += 1  # Update player score
                elif winner == 2:
                    c_score += 1  # Update computer score

        elif user_action == 2:
            # Display current scores
            display_scores(p_score, c_score)

        elif user_action == 3:
            # Show final score and exit game
            print("Final Score:")
            display_scores(p_score, c_score)
            print("Goodbye.")
            break

# Run the game
play_rock_paper_scissors()