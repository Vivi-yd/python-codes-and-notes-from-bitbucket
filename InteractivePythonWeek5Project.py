# implementation of card game - Memory

import simplegui
import random

# initialize numbers on card

num_list = range(8)
card_nums = num_list + num_list

#CONSTANTS

CANVAS_HEIGHT = 100
CANVAS_WIDTH = 800
CARD_HEIGHT = CANVAS_HEIGHT
CARD_WIDTH = CANVAS_WIDTH/len(card_nums)
FONT_HEIGHT = 40


#global variables

state = 0
turns = 0

exposed = [False]*16


#shuffle the card

def shuffle_card():
    
    
    
    random.shuffle(card_nums)
    
print card_nums

# helper function to initialize globals
def new_game():
    
    global state, Turns
    shuffle_card()
    turns = 0
    state = 0
    
    
      

     
# define event handlers
def mouseclick(pos):
    
    global exposed, state, turns
    
    
    pos = list(pos)
    click_x = pos[0]
    
    
        
    for i in range(len(card_nums)):
        if click_x < CARD_WIDTH * i and CARD_WIDTH * (i-1) < click_x:
                exposed[i-2] = True
        
    if state == 0:
        state = 1
        
        
    elif state == 1:
        state = 2
        turns += 1
        
        
    else:
        state = 1
        
    
    print exposed 
    print click_x
    
    print "state", state
    
    print "turns", turns

    return turns       
    return exposed
    
    

                
            
   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
       
#draw cards
    

    for i in range(len(card_nums)):
        

        if exposed[i-1]:
            
           text_width = frame.get_canvas_textwidth(str(card_nums[i]), FONT_HEIGHT, "sans-serif")
        
           x = (CARD_WIDTH * i) + ((CARD_WIDTH - text_width)//2) 
            
           y = ((CARD_HEIGHT - FONT_HEIGHT)/2) + FONT_HEIGHT
        
           canvas.draw_text(str(card_nums[i]), (x, y), 
           FONT_HEIGHT, "aqua", "sans-serif")
            
        else:
            
            canvas.draw_polygon(([CARD_WIDTH * i, 0], [CARD_WIDTH*(i+1), 0], 
            [CARD_WIDTH*(i+1), 100], [CARD_WIDTH*i, 100]), 2, "black", "yellow")
            
     
   
#determine whether cards are paired


#counter


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.set_text("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric