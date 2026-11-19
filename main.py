import random

# Define the number and type of card
Number = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
Type = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

# Make every card only appear once
deck = []
for n in Number:
    for t in Type:
        deck.append(f'{n} of {t}')

random.shuffle(deck)

# Deal 7 cards
my_hand = []
for i in range(7):
    my_hand.append(deck.pop(0))

print("Your hand is:")
for card in my_hand:
    print(card)

# Deal bot 7 cards - hidden
bot_hand = []
for i in range(7):
    bot_hand.append(deck.pop(0))

print("\nBot has 7 cards (hidden)")
