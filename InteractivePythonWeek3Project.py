# "Stopwatch: The Game"

#import require modules


import simplegui

# define global variables


is_watch_running = False

current_time = 0

num_of_stops = 0

num_of_whole_sec_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
    
def format(t):
    
    global deci_sec
    
    mins = t // 600
    
    secs = (t % 600) / 10
    
    deci_sec = (t % 600) % 10
    
    if len(str(secs)) < 2:
        
        t = str(mins) + ":0" + str(secs) + "." + str(deci_sec)
        
    else:
        
        t = str(mins) + ":" + str(secs) + "." + str(deci_sec)
        
    return t
    


    
# define event handlers for buttons; "Start", "Stop", "Reset"

# for start watch

def start_watch_button():
    
    global is_watch_running
    
    timer.start()
    
    is_watch_running = True
    

# for stop watch

def stop_watch_button():
    
    global is_watch_running, num_of_stops, num_of_whole_sec_stops
    
    str_time = str(current_time)
    
    if is_watch_running == True:
        
        is_watch_running = False
        
        if is_watch_running == False and str_time[len(str_time)- 1] == str(0):
            
            num_of_stops += 1
            num_of_whole_sec_stops += 1
            
            
    
        elif is_watch_running == False:
        
            num_of_stops += 1
            
              
            
    timer.stop()
    
    
    

   

# for resetting watch

def reset_button():
    
    global current_time, is_watch_running, num_of_stops, num_of_whole_sec_stops
    
    timer.stop()
    
    current_time = 0
    
    is_watch_running = False
    
    num_of_stops = 0
    
    num_of_whole_sec_stops = 0

# define event handler for timer with 0.1 sec interval

def timer_handler():
    
    global current_time

    current_time += 1
    

# define draw handler

def draw_time(canvas):
    
    global current_time, num_of_whole_sec_stops, num_of_stops
    
    canvas.draw_text(format(current_time), [70, 120], 50, "White",)
    
    canvas.draw_text(str(num_of_whole_sec_stops) + "/" + str(num_of_stops), [190,25], 30, "Red")

    
# create frame

frame = simplegui.create_frame("The Stop-watch Game", 250, 200)


# register event handlers


frame.set_draw_handler(draw_time)





start_watch = frame.add_button("Start", start_watch_button, 200) 

stop_watch = frame.add_button("Stop", stop_watch_button, 200)  

reset_watch = frame.add_button("Reset", reset_button, 200) 




# create timer

timer = simplegui.create_timer(100, timer_handler)


# start frame

frame.start()
