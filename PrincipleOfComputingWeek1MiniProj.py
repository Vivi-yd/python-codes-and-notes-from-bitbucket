"""
Cookie Clicker Simulator by vivi
"""
from math import ceil
import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

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
    #create a ClickerState() object
    state = ClickerState()
    while True:
        
        #bringing game states into this function
        
        cookies = state.get_cookies()
        cps = state.get_cps()
        time_left = duration - state.get_time()
    
        # break loop if current time exceed the simulation duration.
        if state.get_time() > duration:
            break
            
        # next item to purchase as per strategy
        nxt_item = strategy(cookies, cps, duration, build_info)
        
        # check if there is anything to buy next according to strategy chosen
        # if none break.
        if nxt_item == None:
            break
        # cost of that next item to purchase
        nxt_item_cost = build_info.get_cost(nxt_item)
        nxt_item_cps_add = build_info.get_cps(nxt_item)
        
        # time needed until next purchase is affordable
        wait_time = state.time_until(nxt_item_cost)
        
        # check time needed to be able to make next purchase as per strategy
        # if time needed exceeds duration, stop checking for purchase
        if wait_time > time_left:
            break
                
        # wait till that time if not exceeded (info auto update)
        
        state.wait(wait_time)
        # buy item when affordable (info auto update) 
        state.buy_item(nxt_item, nxt_item_cost, nxt_item_cps_add)
        #upate the buildInfo
        build_info.update_item(nxt_item)
            
    state.wait(time_left)
    
    return state

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
    return None

def strategy_expensive(cookies, cps, time_left, build_info):
    return None

def strategy_best(cookies, cps, time_left, build_info):
    return None
        
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
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    
import user34_9rUeW6UkrB_2
user34_9rUeW6UkrB_2.test_class(ClickerState)