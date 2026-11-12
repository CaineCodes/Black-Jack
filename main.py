import random
from turtle import *

# Card drawing
turtle = Turtle()
turtle.width(3)
turtle.pendown()
turtle.fillcolor(255,0,0)
turtle.begin_fill()
for i in range(2):
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(5)
turtle.right(90)
turtle.forward(70)
turtle.pendown()
turtle.fillcolor(0,0,0)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

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
