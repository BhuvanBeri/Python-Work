import random

print("What do you choose? rock paper or scissors?")
inp = input().lower()

names = ["rock", "paper", "scissors"]

random_option = random.choice(names)
print("Computer chose: ", random_option)

if(inp == random_option):
    print("It's tie, please retry")


if(inp == "rock"):
    if(random_option == "paper"):
        print("You loose")
    elif(random_option == "scissors"):
        print("You won")
elif(inp == "paper"):
    if(random_option == "rock"):
        print("You win")
    elif(random_option == "scissors"):
        print("You lose")
elif(inp == "scissors"):
    if(random_option == "rock"):
        print("You lose")
    elif(random_option == "paper"):
        print("You win")