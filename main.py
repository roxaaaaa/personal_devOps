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
import logging


# Logging Configuration


logging.basicConfig(
    filename="game.log",              # Save logs to a file
    level=logging.INFO,               # Log INFO and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)

MAX_ATTEMPTS = 3
TARGET_AGE = 19


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

    logging.info(
        "Game started with target age %d and %d attempts", target, attempts)

# Loop through the range of allowed attempts (1 to attempts)
    for attempt in range(1, attempts + 1):

        logging.debug("Attempt %d started", attempt)

        try:
            prompt = f"\n[Attempt {attempt}/{attempts}] Guess my age: "
            user_input = input(prompt)

            logging.info("User input received: %s", user_input)

            guess = int(user_input)

        except ValueError:
            print("Invalid input! You wasted an attempt. "
                  "Please enter a number.")
            logging.warning("Invalid input (not an int): %s", user_input)
            continue

        # Logic to check if the guess is correct, high, or low
        if guess == target:
            print(" That's right! You verified my identity.")
            logging.info("Correct guess on attempt %d", attempt)
            sys.exit(0)
        elif guess < target:
            print("Too low! I'm older than that.")
            logging.info("User guessed too low: %d", guess)
        else:
            print("Too high! I'm younger than that.")
            logging.info("User guessed too high: %d", guess)

    # If the loop finishes without a correct guess
    print("\n Game Over. Run the script to try again.")
    logging.info("Game over. User failed to guess the age.")


if __name__ == "__main__":
    """
    Main Guard.
    Ensures that start_game() only runs if this file is executed directly,
    not if it is imported as a module in another script.
    """
    start_game(TARGET_AGE, MAX_ATTEMPTS)
