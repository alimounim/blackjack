# 🃏 Blackjack Game (Python)

This is a simple command-line Blackjack game built in Python.
It follows classic Blackjack rules and lets the user play against the computer (dealer).

## 🎯 Features

Unlimited deck size

Face cards (J, Q, K) = 10

Ace can count as 11 or 1

Dealer draws until reaching 17 or higher

Detects Blackjack, busts, and win/lose conditions

Clean functions for dealing cards, calculating score, and comparing results

## 🧠 How the Game Works

The player and computer each get two cards to start.

The player chooses to:

Hit → get another card

Stand → end their turn

If the player goes over 21, they automatically lose.

After the player finishes, the computer draws cards until its score is 17+.

The program compares scores and prints the result.

## 🗂️ File Overview

deal_card() → draws a random card

calculate_score() → handles Blackjack logic and Ace adjustments

compare() → decides the winner

play_game() → runs one full round of the game

## ▶️ How to Run

Make sure Python is installed, then run:

python main.py


You will be asked:

Do you want to play a game of BlackJack? (y/n):


Press y to start playing!

## ✅ Example Output
Player card: [10, 7], player score: 17
Computer's first card: 9
Type 'y' to get another card, type 'n' to pass:

## 📌 Notes

This is a practice project to learn Python functions, loops, and game logic.

Cards are not removed from the deck, matching the project instructions.

The BlackJack logo is imported from art.py.
