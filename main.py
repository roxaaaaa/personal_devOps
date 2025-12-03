#!/usr/bin/env python3
"""
Age Guessing Game Module.

This script runs a simple CLI game where the user attempts to guess
the author's age. It demonstrates standard Python documentation practices,
error handling, and loop control flow.

Author: Roksolana
Date: 2023-10-27
"""

import sys


TARGET_AGE = 19
MAX_ATTEMPTS = 3

def start_game(target: int, attempts: int):
    """
    Starts the main game loop.

    This function prompts the user for input, validates that it is an integer,
    and compares it against the target age.

    Args:
        target (int): The actual age the user is trying to guess.
        attempts (int): The maximum number of tries allowed.

    Returns:
        None: The function exits the program via sys.exit() upon success
              or prints a failure message when the loop finishes.
    """
    
    print("Hello, my name is Roksolana.")
    print(f"You have {attempts} attempts to guess my age.")

    #Loop through the range of allowed attempts (1 to attempts)
    for attempt in range(1, attempts + 1):
        try:
            # f-strings are used here for dynamic prompt generation
            user_input = input(f"\n[Attempt {attempt}/{attempts}] Guess my age: ")
            guess = int(user_input)
        except ValueError:
            # This block runs if the user types text (e.g., "twenty")
            print("Invalid input! You wasted an attempt. Please enter a number.")
            continue

        # Logic to check if the guess is correct, high, or low
        if guess == target:
            print(" That's right! You verified my identity.")
            sys.exit(0) # Exit code 0 means "Success"
        elif guess < target:
            print("Too low! I'm older than that.")
        else:
            print("Too high! I'm younger than that.")

    # If the loop finishes without a correct guess
    print("\n Game Over. Run the script to try again.")

if __name__ == "__main__":
    """
    Main Guard.
    
    Ensures that start_game() only runs if this file is executed directly,
    not if it is imported as a module in another script.
    """
    start_game(TARGET_AGE, MAX_ATTEMPTS)