import random
import art
from game_data import data

game_over = False
score = 0

# Create a random celebrity
def random_celebrity():
    celebrity = random.choice(data)
    return celebrity

last_celebrity = random_celebrity()

# Comparing the user guess with the correct answer
def compare(guess, celeb_1, celeb_2):
    global game_over
    global score
    global last_celebrity

    if celeb_1["follower_count"] > celeb_2["follower_count"]:
        winner = "A"
    else:
        winner = "B"

    if guess != winner:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    else:
        score += 1
        print(f"You're right! Current score: {score}.")

    last_celebrity = celeb_2

def game():
    celeb_1 = last_celebrity
    new_celebrity = random_celebrity()
    if new_celebrity != last_celebrity:
        celeb_2 = new_celebrity
    else:
        celeb_2 = random_celebrity()

    print(art.logo)
    print(f"Compare A: {celeb_1["name"]}, a {celeb_1["description"]}, from {celeb_1["country"]}")
    print(art.vs)
    print(f"Against B: {celeb_2["name"]}, a {celeb_2["description"]}, from {celeb_2["country"]}")

    # Ask the user to guess a celebrity
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare(guess, celeb_1, celeb_2)

while not game_over:
    game()




