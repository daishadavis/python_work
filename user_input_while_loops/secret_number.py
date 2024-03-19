import random

name = input("Enter name: ")
print(f"Hello {name}, I'm think of a number between 1 and 2,000")

secret_number = random.randrange(2_000)

n = 0
while True:
    n = n + 1
    print("Number of guesses", n)
    guess = input("Guess: ")
    if int(guess) < secret_number:
        print("to low")
    elif int(guess) > secret_number:
        print("to high")
    elif int(guess) == secret_number:
        print("Congradulations you found the secret number.")
        break


