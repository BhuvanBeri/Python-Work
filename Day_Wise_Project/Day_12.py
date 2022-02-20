import random

answer = random.choice(range(100))

def value(attempts):
    while(attempts != 0):

        guess = int(input("Make a guess: "))
    
        if(guess == answer):
            print(f"You got it! The answer was {answer}.")
                
        elif (guess < answer):
            print("Too low.")
            attempts = attempts - 1
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
                
        elif (guess > answer):
            print("Too high.")
            attempts = attempts - 1
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print("You Lost.")


print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if(difficulty == "easy"):
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    value(attempts)

elif(difficulty == "hard"):
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    value(attempts)
