# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards_in_hand = [] 
        

    def __str__(self):
        
        s = "Hand contains "
        for card in self.cards_in_hand:
            s += str(card) + " "
        return s 

    def add_card(self, card):
        # add a card object to a hand
        self.cards_in_hand.append(card)
            

    def get_value(self):
        aces = 0
        value = 0
        
        for card in self.cards_in_hand:
            card_rank = card.get_rank()
            
            if  card_rank != 'A':
               value += VALUES[card_rank]
            else:
                aces += 1
                
        if aces == 1:
            if value >= 11:
                value = value + 1
            else:
                value = value + 11

        elif aces > 1:
            if value >= 10:
                value = value + aces * 1
            else:
                value = value + 10 + aces * 1           

        return value 
        
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        for suit in SUITS:
            for rank in RANKS:
                deck_card = Card(suit, rank)
                self.cards_in_deck.append(deck_card)
        
        

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards_in_deck)
        

    def deal_card(self):
        return self.cards_in_deck.pop()
        
    
    def __str__(self):
        s = "Deck contains "
        for card in self.cards_in_deck:
            s += str(card) + " "
        return s
 
#globals for deal button
cards_in_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()    

#define event handlers for buttons
def deal():
    
    global outcome, in_play, cards_in_deck, player_hand, dealer_hand
    
    
    cards_in_deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(cards_in_deck.deal_card())
        dealer_hand.add_card(cards_in_deck.deal_card())
    
    
    outcome = "Hit or Stand?"
    in_play = True
    
    #remove this print statements later
    print "Player hand: " + str(player_hand)
    print "Dealer hand: " + str(dealer_hand)
    print "Player value: " , str(player_hand.get_value())
    print "Dealer value: " , str(dealer_hand.get_value())
    print "-------------------------------------"
    print outcome
    
    
    
    

def hit():
    global outcome, in_play
    
    if player_hand.get_value() <= 21 and in_play:
        player_hand.add_card(cards_in_deck.deal_card())
        
    #remove this print statements later
    print "Player hand: " + str(player_hand)
    print "Dealer hand: " + str(dealer_hand)
    print "Player value: " , str(player_hand.get_value())
    print "Dealer value: " , str(dealer_hand.get_value())
    print "-------------------------------------"

    if player_hand.get_value() <= 21:
        outcome = "Hit or Stand?"
        in_play = True
        print outcome
        
    else:
        outcome = "You have busted, Deal again?"
        in_play = False
        print outcome

       
def stand():
    global outcome
    in_play = False
    while dealer_hand.get_value() < 17 and in_play == False:
        dealer_hand.add_card(cards_in_deck.deal_card())
    
    if dealer_hand.get_value() > 21:
        outcome = "Dealer has busted, Deal again?"
    else:
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome = "Dealer win! Deal again?"
        else:
            outcome = "Congratz! You win! Deal again?"
            
    #remove this print statements later
    print "Player hand: " + str(player_hand)
    print "Dealer hand: " + str(dealer_hand)
    print "Player value: " , str(player_hand.get_value())
    print "Dealer value: " , str(dealer_hand.get_value())
    print "-------------------------------------"
    print outcome
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric