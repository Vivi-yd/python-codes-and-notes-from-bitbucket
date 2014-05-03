# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

#default position of paddles and score at initial state

paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel# these are vectors stored as lists
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    #generates random initial velocity for the ball
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240)//40
        ball_vel[1] = random.randrange(-180, -60)//40
        
    else:
        ball_vel[0] = random.randrange(-240, -120)//40
        ball_vel[1] = random.randrange(-180, -60)//40


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    #launch ball
    
    spawn_ball(random.choice([RIGHT, LEFT]))
    
    score1 = 0
    score2 = 0
        

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
   
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    
    
    # update ball
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #makes ball bounce off bottom wall and top wall.
    
    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]
    
    #check if the ball touches the left or right gutters, if yes, relaunch
    #the ball on the opposite gutter of where it had touches
    
    if ball_pos[0] >= ((WIDTH - 1) - PAD_WIDTH)- BALL_RADIUS:
        
        if abs(paddle2_pos- ball_pos[1]) > HALF_PAD_HEIGHT + BALL_RADIUS:
           score1 += 1
        
           spawn_ball(LEFT)
            
        else:
            
            ball_vel[0] = (-1.1)* ball_vel[0]
        
        
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        
        if abs(paddle1_pos- ball_pos[1]) > HALF_PAD_HEIGHT + BALL_RADIUS:
            
           score2 += 1
        
           spawn_ball(RIGHT)
        
        else:
            
            ball_vel[0] = (-1.1)* ball_vel[0]
            
            
            
        
        
        
        
    
        
    
    
    # draw ball
    
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 1, "08E82D", "08E82D")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT and (paddle1_pos + paddle1_vel) <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
        
        
    if (paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT and (paddle2_pos + paddle2_vel) <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT), 
                    (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), 
                     (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT)], 1, "08E82D", "08E82D")
    
    canvas.draw_polygon([(WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 
                    (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 
                    (WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT)], 1, "08E82D", "08E82D")
    
    # draw scores
    
    # width of score2
    
    score2_width = frame.get_canvas_textwidth(str(score2), 50)
    
    
    canvas.draw_text(str(score1), [WIDTH/5, HEIGHT/6], 50, "white", "sans-serif")
    canvas.draw_text(str(score2), [WIDTH*4/5 - score2_width , HEIGHT/6], 50, "white", "sans-serif")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 10
       
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 10
        
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 10
    
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 10
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle1_vel = 0
    
    paddle2_vel = 0
    



    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#create reset button

frame.add_button("Restart", new_game, 200)

# start frame
new_game()
frame.start()
