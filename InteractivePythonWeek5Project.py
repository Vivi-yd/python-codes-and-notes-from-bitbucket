# implementation of card game - Memory

import simplegui
import random

# initialize numbers on card

num_list = range(8)
card_values = num_list + num_list

#CONSTANTS

CANVAS_HEIGHT = 100
CANVAS_WIDTH = 800
CARD_HEIGHT = CANVAS_HEIGHT
CARD_WIDTH = CANVAS_WIDTH/len(card_values)
FONT_HEIGHT = 40


#global variables

state = 0
turns = 0

first_card_index = 0
second_card_index = 0
first_card = 1
second_card = 1

#a list storing the state of cards

exposed = [False]*16


#shuffle the card

def shuffle_card():
       
    random.shuffle(card_values)
    
print card_values

# helper function to initialize globals
def new_game():
    
    global state, turns, exposed
    shuffle_card()
    turns = 0
    state = 0
    label.set_text("Turns = " + str(turns))
    
    exposed = [False]*16
    
# define event handlers
def mouseclick(pos):
    
    global exposed, state, turns, first_card_index, second_card_index, first_card, second_card
    
    #x coordinate of mouseclick
    pos = list(pos)
    click_x = pos[0]
    
    #get the card number (index) which is being clicked
    card_num = click_x // CARD_WIDTH
    #exposing the card if it is not exposed
    if (not exposed[card_num]):
        exposed[card_num] = True

             
#changing state of games
                
        if state == 0:
            first_card_index = card_num
            first_card = card_values[first_card_index]
            state = 1
        elif state == 1:
            second_card_index = card_num
            second_card = card_values[second_card_index]
            state = 2
            turns += 1
        else:
            #if two previous clicked card are unpaired
            if first_card != second_card:
                #flip the two cards over
                exposed[first_card_index] = False
                exposed[second_card_index] = False
            
            #update the first clicked card
            first_card_index = card_num
            first_card = card_values[first_card_index]            
            state = 1
        
     
    print exposed 
    print click_x
    
    print "state", state
    
    print "turns", turns
    label.set_text("Turns = " + str(turns))
#determine whether cards are paired
    
    
#changing label    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
       
#draw cards
    

    for i in range(len(card_values)):
        
    #drawing face of cards
    
        if exposed[i]:
            
           text_width = frame.get_canvas_textwidth(str(card_values[i]), FONT_HEIGHT, "sans-serif")
        
           x = (CARD_WIDTH * i) + ((CARD_WIDTH - text_width)//2) 
            
           y = ((CARD_HEIGHT - FONT_HEIGHT)/2) + FONT_HEIGHT
        
           canvas.draw_text(str(card_values[i]), (x, y), 
           FONT_HEIGHT, "aqua", "sans-serif")
     
    #drawing back of cards
            
        else:
            
            canvas.draw_polygon(([CARD_WIDTH * i, 0], [CARD_WIDTH*(i+1), 0], 
            [CARD_WIDTH*(i+1), 100], [CARD_WIDTH*i, 100]), 2, "black", "yellow")



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric