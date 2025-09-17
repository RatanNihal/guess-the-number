import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 chances to guess it.")

secret_number=random.randint(1,100)
chances=7

while chances > 0:
    guess= int(input("Enter your guess: "))
    if guess==secret_number:
        print("Congratulations! You guessed the number correctly!")
        break
    elif guess <secret_number:
        print("Too low! Try a higher number.")
    else: 
        print("Too high! Try a lower number.")
    
    chances -=1
    print(f"You have {chances} chances left.\n")

if chances ==0:
    print(f"You ran out of chances! The number was {secret_number}. Better luck next time!")
