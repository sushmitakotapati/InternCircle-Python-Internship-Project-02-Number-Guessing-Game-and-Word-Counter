
import random

number = random.randint(1, 100)
attempts = 0
score = 100

print("\n--- Number Guessing Game ---")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
            score -= 10

        elif guess > number:
            print("Too high!")
            score -= 10

        else:
            print("\nCorrect! You guessed the number.")
            print("Attempts:", attempts)
            print("Final Score:", max(score, 0))
            break

    except ValueError:
        print("Please enter a valid whole number.")
