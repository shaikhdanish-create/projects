import random

# Logo
logo = """
==============================
      HIGHER LOWER GAME
==============================
"""

# Sample data
data = [
    {"name": "Instagram", "description": "Social media platform", "country": "USA", "follower_count": 650},
    {"name": "Cristiano Ronaldo", "description": "Footballer", "country": "Portugal", "follower_count": 600},
    {"name": "Lionel Messi", "description": "Footballer", "country": "Argentina", "follower_count": 500},
    {"name": "Selena Gomez", "description": "Singer and actress", "country": "USA", "follower_count": 430},
    {"name": "Kylie Jenner", "description": "Reality TV star", "country": "USA", "follower_count": 400},
    {"name": "Dwayne Johnson", "description": "Actor and wrestler", "country": "USA", "follower_count": 380},
]

def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)

score = 0
game_should_continue = True

while game_should_continue:

    account_a = random.choice(data)
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'a' or 'b': ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
