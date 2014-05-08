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
score = 20

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#global for drawing

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
TITLE = "WELCOME TO BLACKJACK!"
TITLE_SIZE = 40
TITLE_FONT = "monospace"
TEXT_COLOUR = "yellow"
MESSAGE_FONT = "sans-serif"
MESSAGE_SIZE = 30
MESSAGE_COLOUR = "aqua"



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
        i = 0
        
        for card in self.cards_in_hand:
            card.draw(canvas, ((pos[0] + 80 * i), pos[1]))
            
            i += 1
 
        
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
    
    global outcome, in_play, cards_in_deck, player_hand, dealer_hand, score
    
    if in_play:
        outcome = "You gave up, Dealer win!"
        score -= 10
        
    else:
        cards_in_deck = Deck()
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
    global outcome, in_play, score
    
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
        score -= 10

       
def stand():
    global outcome, in_play, score
    in_play = False
    while dealer_hand.get_value() < 17 and in_play == False:
        dealer_hand.add_card(cards_in_deck.deal_card())
    
    if dealer_hand.get_value() > 21:
        outcome = "Dealer has busted, Deal again?"
        score += 10
    else:
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome = "Dealer win! Deal again?"
            score -= 10
        else:
            outcome = "Congratz! You win! Deal again?"
            score += 10
            
    #remove this print statements later
    print "Player hand: " + str(player_hand)
    print "Dealer hand: " + str(dealer_hand)
    print "Player value: " , str(player_hand.get_value())
    print "Dealer value: " , str(dealer_hand.get_value())
    print "-------------------------------------"
    print outcome
    
# draw handler    
def draw(canvas):
    #drawing cards in both hands
    player_hand.draw(canvas, (50, 400))
    dealer_hand.draw(canvas, (50, 150))
    
    #title
    title_text_width = frame.get_canvas_textwidth(TITLE, TITLE_SIZE, TITLE_FONT)
    canvas.draw_text(TITLE, [CANVAS_WIDTH/2 - title_text_width/2, 30],
                     TITLE_SIZE, TEXT_COLOUR, TITLE_FONT)
    #message for player
    message_width = frame.get_canvas_textwidth(outcome, MESSAGE_SIZE, MESSAGE_FONT)
    canvas.draw_text(outcome, [CANVAS_WIDTH - (30 + message_width), CANVAS_HEIGHT/2], 
                     MESSAGE_SIZE, MESSAGE_COLOUR, MESSAGE_FONT)
    
    #drawing "hole card" if it's player turn
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          [(50 + CARD_SIZE[0]/2), (150 + CARD_SIZE[1]/2) ], 
                          CARD_BACK_SIZE)
    #drawing score to canvas
    score_message = "Your money: " + str(score)
    score_width = frame.get_canvas_textwidth(score_message,
                                             MESSAGE_SIZE, MESSAGE_FONT)
    canvas.draw_text(score_message, [CANVAS_WIDTH - (30 + score_width), CANVAS_HEIGHT*0.6]
                        ,MESSAGE_SIZE, "black", MESSAGE_FONT)


# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_WIDTH, CANVAS_HEIGHT)
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