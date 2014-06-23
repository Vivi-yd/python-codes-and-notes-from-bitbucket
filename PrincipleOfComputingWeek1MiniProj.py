"""
Cookie Clicker Simulator by vivi
"""
from math import ceil
import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

def keywithmaxval(dic):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     val = list(dic.values())
     key = list(dic.keys())
     return key[val.index(max(val))]

def keywithminval(dic):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the min value"""  
     val = list(dic.values())
     key =list(dic.keys())
     return key[val.index(min(val))]


# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 1000.0
class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        initializing elements in the game
        """
        self._tot_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        #rate of cookies production, namely cookies per sec.
        self._current_cps = 1.0
        #history to keep track of record.
        self._history = [(0.0, None, 0.0, 0.0)]
        
        
        
    def __str__(self):
        """
        Return human readable state
        """
        return "total cookies so far: " + str(self._tot_cookies) + " current # of cookies: " + str(self.get_cookies()) + " cps: " + str(self.get_cps()) + " at time: " + str(self.get_time())
        
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies); Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS; Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time; Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time_needed = ceil((cookies - self.get_cookies())/self.get_cps())
        if time_needed < 0:
            return 0.0
        return time_needed
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            self._current_time += time
            #calculate cookies produced during time waited.
            cookies_made = time * self._current_cps
            self._tot_cookies += cookies_made
            self._current_cookies += cookies_made
            
            
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        # update states accordingly
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._tot_cookies))
        
        
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
   
    #create a new ClickerState object
    clicker = ClickerState()
    
    #function should loop until the time in the ClickerState object reaches the duration
    while True:
        #get the game states for this instance
        cookies = clicker.get_cookies()
        current_time = clicker.get_time()
        time_left = duration - current_time
        current_cps = clicker.get_cps()
        
        # break loop if current time exceed the simulation duration.
        if current_time > duration:
            break
            
        ## next item to purchase as per strategy
        next_item = strategy(cookies, current_cps, time_left, build_info)
        ## break loop if no further purchase is to be made according to strategy.
        if next_item == None:
            break
        
        # cost and additional cps of next purchase.
        cost_next_item = build_info.get_cost(next_item)
        cps_next_item = build_info.get_cps(next_item)
        # time needed in order to afford next purchase.
        time_needed = clicker.time_until(cost_next_item)
        
        # break loop if time needed for next purchase exceed the time left for simulation.
        if time_needed > time_left:
            break
            
        #wait until that time if not exceed.
        clicker.wait(time_needed)
        #buy the item
        clicker.buy_item(next_item, cost_next_item, cps_next_item)
        #update the build information
        build_info.update_item(next_item)
    
    # wait till the remaining time is over.
    clicker.wait(time_left)
    

    # return game state.
    return clicker


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Always return cheapest available item
    """
    items_dict = {}
    for item in build_info.build_items():
        item_price = build_info.get_cost(item)
        items_dict[item] = item_price
    cheapest_item = keywithminval(items_dict)
    if cookies + cps * time_left >= build_info.get_cost(cheapest_item):
        #print cheapest_item
        return cheapest_item
    else:
        return None

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Always return most expensive available item in the remaining time
    """
    #get a dict of item - cost if item price
    items_dict = {}
    for item in build_info.build_items():
        item_price = build_info.get_cost(item)
        if item_price <= cookies + cps * time_left:
            items_dict[item] = item_price
    #return appropriate key 
    if len(items_dict) == 0:
        return None
    else:
        #print keywithmaxval(items_dict)
        return keywithmaxval(items_dict) 

    

def strategy_best(cookies, cps, time_left, build_info):
    """ best strategy that that I can think of """
    
    # create an item dict to be select for purchasing
    selected_item = {}
    
    # get price/cps of each item in the game
    for item in build_info.build_items():
        item_price = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        fraction = item_cps * time_left/item_price
        selected_item[item] = fraction
            
    if len(selected_item) == 0:
        return None
            
    # make the most expensive purchase in affordable_items 
    else:
        return keywithmaxval(selected_item)
    
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    
#import user34_9rUeW6UkrB_2
#user34_9rUeW6UkrB_2.test_class(ClickerState)
