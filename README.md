# Poker-Hand-Game

A poker hand game that generates 5-card hands which display corresponding grades and points.
The purpose of the project was to create an accurate and easy game strictly within a text editor (no reliance on additional packages).


## Technologies
- Language: Python 3.8.3
- Editor: PyCharm
- Libraries: Counter (collections) & Random


## Setup
No setup is required. The hand analyser is all executed when the user runs the program.


## Walkthrough
Card:

The initial class defines the attributes of each card. A shape attribute is also included (4 symbols are used in text form)

Deck Actions:

Shuffle and deal are core functions that are utilised throughout.

Design:

Colours are implemented into the card display in addition to the heart/diamond symbols. A colour palette is also used for the main console.

Deck Configurations:

Dictionaries are used for defining each suit/number to combat the issue of face cards. Each card is built with a number and symbol in addition to vertical card separators.

Grading:

The grading class defines the logic for how specific hands are triggered in the console at the end of the program. Functions are included for pairs through to four of a kind (royal flush and straight flush use combinations). 

Console:

The console (play function) encompasses all of the aforementioned code. The deck is shuffled and 5 cards are dealt to the player. The grading class is called and a long ‘if/elif’ chain is triggered to check for a corresponding poker hand. Feedback is triggered (i.e. ‘TWO PAIR!’) and points are allocated depending on the strength of the hand.

The feedback (string) is purposefully formatted to be showcased in a centralised display with the players’ hand.


## Status

Project completed.
