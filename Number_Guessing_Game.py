import random

print("Hi Welcome to the Number Guessing game.\nYou have 7 chances to guess the right number. Let's start.")

low = int(input("Enter the LOWER Bound number: "))
high = int(input("Enter the UPPER Bound number: "))

num = random.randint(low, high)

print(
    f"\nYou have 7 chances to guess the right number between {low} and {high}. Let's start!")

# total number of attempts or guess chances
gc = 7
# guess counter
ch = 0

while ch < gc:
    # increment operation
    ch += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {ch} attempts")
        break

    if guess < num:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    if ch == gc:
        print(f"Sorry! The number was {num}. Better luck next time.")
