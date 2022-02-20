import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

answer = random.randint(0,1)

if (answer == 0):
    print("Heads")
else:
    print("Tails")