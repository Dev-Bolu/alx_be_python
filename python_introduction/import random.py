import random

while True:
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        match guess:
            case n if n < secret_number:
                print("Too low! Try again.")
            case n if n > secret_number:
                print("Too high! Try again.")
            case n if n == secret_number:
                print(f"🎉 Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
                break  # Exit the guessing loop

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break  # Exit the outer loop if not "yes"
