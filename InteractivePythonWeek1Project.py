# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

### comments by ashutosh -: Better than my code :D . However, the better way to deal with invalid input is to use
### assertion. You can see below. You can use list or tuple to write assertion statement in one line

# helper functions

def name_to_number(name):
    #assert name in ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    
    #in case of an invalid input the program will crash raising an assertion error !!!
    #it is considered more stylish :) and is better in terms of writing an robust code 
    
    if name == "rock":
        number = 0
        
    elif name == "Spock":
        number = 1
        
    elif name == "paper":
        number = 2
        
    elif name == "lizard":
        number = 3
        
    elif name == "scissors":
        number = 4
        
#in the case if the fanction receive an invalid name
#as it's argument.

    else:
        number = "invalid name"
    
    return number

################################################################################3

# Convert number 0~4 to name corresponding to above
# list of assignments.



def number_to_name(number):
    
    if number == 0:
        name = "rock"
        
    elif number == 1:
        name = "Spock"
    
    elif number == 2:
        name = "paper"
    
    elif number == 3:
        name = "lizard"
    
    elif number == 4:
        name = "scissors"
        
#in the case when the fanction receive an arguement other
#than the range of 0 to 4.
   
    else:
        name = "invalid input for number"
        
    return name
        
######################################################################################
    

def rpsls(player_choice):
    
    # print a blank line to separate consecutive games
    
    print ''
    
    # print out the message for the player's choice
    
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    
    import random
    
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    
    result = (player_number - comp_number) % 5.0

    # use if/elif/else to determine winner, print winner message
    
    if result == 1 or result == 2:
        message = "Player Win!"
        
    elif result == 3 or result == 4:
        message = "Computer Win!"
    
    elif result == 0:
        message = "Player and Computer Tie."
        
    print message


# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")