import sys

TARGET_AGE = 19
MAX_ATTEMPTS = 3

print("Hello, my name is Roksolana.")
print(f"You have {MAX_ATTEMPTS} attempts to guess my age.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        guess = int(input(f"\n[Attempt {attempt}/{MAX_ATTEMPTS}] Guess my age: "))
    except ValueError:
        print("Invalid input! You wasted an attempt.")
        continue

    if guess == TARGET_AGE:
        print("That's right! You verified my identity.")
        sys.exit()
    elif guess < TARGET_AGE:
        print("Too low! I'm older than that.")
    else:
        print("Too high! I'm younger than that.")

print("\n Game Over. Run the script to try again.")
