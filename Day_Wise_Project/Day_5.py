import random

print("Welcome to the PyPassword Generator!")
inp1 = int(input("How many letters would you like in your password?\n"))

inp2 = int(input("How many symbols would you like?\n"))

inp3 = int(input("How many numbers would your like?\n"))

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "~"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

password_list = []

for char in range(1, inp1+1):
    password_list.append(random.choice(alphabets))

for char in range(1, inp2+1):
    password_list.append(random.choice(symbols))

for char in range(1, inp3+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Here is your password: ", password)