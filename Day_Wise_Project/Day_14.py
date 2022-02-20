import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    }
]



def format_data(account):
    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_country = account_a["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"

def answer(user_guess, a_follower_count, b_follower_count):

    score = 0
    if (user_guess == "A" and a_follower_count > b_follower_count):
        score += 1
        return f"You won!, your score is {score}"
    elif (user_guess == "B" and a_follower_count < b_follower_count):
        score += 1
        return f"You won!, your score is {score}"
    else:
        return f"You Lost!, your final score is {score}"

account_a = random.choice(data) 
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print (f"Compare A: {format_data(account_a)}.")
print ("Vs")
print (f"Compare B: {format_data(account_b)}.")

user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
a_follower_count = account_a["follower_count"]
b_follower_count = account_a["follower_count"]

final = answer(user_guess, a_follower_count, b_follower_count)
print(final)