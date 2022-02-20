import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCsv = input("Give me Everybody's names, use comma to separate names ")

names = namesAsCsv.split(", ")

numbering = random.randint(0, len(names) - 1)

answer = names[numbering] 

# or use answer = random.choice(names)

print(f" {answer} is going to pay for the meal today. ")