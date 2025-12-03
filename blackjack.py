############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

from art import logo
#print(logo)
import random

# Function to deal card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to calculate the score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, c_score):
    if p_score == c_score:
        print("Draw")
    elif c_score == 0:
        print("Lose, opponent has Blackjack")
    elif p_score == 0:
        print("Win with a Blackjack")
    elif p_score > 21:
        print("You went over. You Lose.")
    elif c_score > 21:
        print("Computer went over. You Win.")
    elif p_score > c_score:
        print("You Win")
    else:
        print("You Lose")

def play_game():
    print(logo)
    player_card = []
    computer_card = []
    computer_score = -1
    player_score = -1
    is_game_over = False

    for _ in range (0, 2):
        player_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)

        print(f"Player card: {player_card}, player score: {player_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                player_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Player final hand: {player_card}, player final score: {player_score}")
    print(f"Computer's final card: {computer_card}, computer final score: {computer_score}")

while input("Do you want to play a game of BlackJack? (y/n): ") == 'y':
    print("\n" * 10)
    play_game()