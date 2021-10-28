# cli-flashcards
Use flashcards in the terminal.
The program is made in python, and runs in the terminal. I made this because I wanted a simple terminal program to practice with flash cards.
The card decks are in yaml format, so they are easily editable although the program also provides commands to edit the card decks.
[About flashcards](https://en.wikipedia.org/wiki/Flashcard)

## Installation
1. Open up a terminal and cd into this folder
2. Run command: ```pip install -r requirements.txt```
3. Now run ```python flashcards.py```

## Usage
You can create a deck and then add cards to it, then you can practice with it.
The program goes through all the cards in a deck in random order.

For every card you need to say if you know the meaning. Each time you 'know' a card, it will get marked as 'known'. This devides your cards in a 'known' and 'unknown' pile. Aftere going through your cards, the program displays how many cards you have yet to remember and asks if you want to practice again. The next time you practice, the program will only ask the cards you don't know yet.

Commands:
- ```python flashcards.py create [name]```
    - Creates a new flashcard deck
- ```python flashcards.py [deck]```
    - Practice your deck
- ```python flashcards.py [deck] add```
    - Add cards to your deck
- ```python flashcards.py [deck] remove```
    - Remove cards from your deck
- ```python flashcards.py [deck] clear```
    - Mark all cards in deck as 'unknown'
- ```python flashcards.py [deck] list```
    - List all cards in your deck