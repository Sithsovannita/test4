import random
from os import system
number_to_guess=random.randint(0,100)
while True:
    while True:
        try:
            guess=int(input("Guess number between 0 and 100:"))
            break
        except ValueError as va:
            print("Invalid input.")
    if guess==number_to_guess:
         system('cls')
         print("congrat you're won.")
    elif guess<number_to_guess:
        system('cls')
        # print(f"To low.try to guess more {guess+1}upper")
        print(f"To low.{100-(guess/2)}")
    else:
        system('cls')
        print(f"To hight.try to guess low than {guess-1}lower")
