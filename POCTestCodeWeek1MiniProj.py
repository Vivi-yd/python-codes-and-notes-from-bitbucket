"""test code for cookie clicker program by vivi and her bf"""
import poc_simpletest

def test_class(ClickerState):
    """
    test clickerstate class in the program
    """
    #create the test suite
    suite = poc_simpletest.TestSuite()
    
    # create game (current initial state)
    state1 = ClickerState() # we initialize the game and then do nothing
    state2 = ClickerState() # ... we will somethings to rest of the games .. work out expected
    state3 = ClickerState() #values and test . like we can call state2.wait(1000.0) for state2
    state4 = ClickerState() #game 
    state5 = ClickerState()
    
    ## test __str__ method
    #for game 1
    string_expected1 = "total cookies so far: 0.0 current # of cookies: 0.0 cps: 1.0 at time: 0.0"
    suite.run_test(str(state1), string_expected1, "test 0.1: __str__")
    
    # test get_cookies method
    suite.run_test(state1.get_cookies(), 0.0, "test 1.1: get_cookies() test")
    
    # test get_cps method
    suite.run_test(state1.get_cps(), 1.0, "test 2.1: get_cps() test")
    
    # test get_time method
    suite.run_test(state1.get_time(), 0.0, "test 3.1: get_time() test")
    
    # test get_ history method
    suite.run_test(state1.get_history(), [(0.0, None, 0.0, 0.0)], "test 4.1: get_history() test")
    
    # test time_until method
    suite.run_test(state1.time_until(5.0), 5.0, "test 5.1: test time_until with whole no. of cookies")
    suite.run_test(state1.time_until(6.7), 7.0, "test 5.2: test time_until with fractional no. of cookies")
    
    # test wait method
    state1.wait(9.0)
    wait_string1 = "total cookies so far: 9.0 current # of cookies: 9.0 cps: 1.0 at time: 9.0"
    suite.run_test(str(state1), wait_string1, "test 6.1: test wait for whole num of seconds")
    
    state1.wait(2.3)
    wait_string2 = "total cookies so far: 11.3 current # of cookies: 11.3 cps: 1.0 at time: 11.3"
    suite.run_test(str(state1), wait_string2, "test 6.2: test wait for consecutive call")
    
    state2.wait(24.9)
    wait_string3 = "total cookies so far: 24.9 current # of cookies: 24.9 cps: 1.0 at time: 24.9"
    suite.run_test(str(state2), wait_string3, "test 6.3: test wait for fractional num of secs")
    
    # test buy_item method
    state3.wait(99.4)
    state3.buy_item("my bf's kisses", 90.0, 10.0)
    buy_string1 = "total cookies so far: 99.4 current # of cookies: 9.4 cps: 11.0 at time: 99.4"
    suite.run_test(str(state3), buy_string1, "test 7.1: test game state after buy_item")
    suite.run_test(state3.get_history(), [(0.0, None, 0.0, 0.0),(99.4, "my bf's kisses", 90.0, 99.4)], "test 7.2: retriving history after buy_item")
                   
    # reporting result
    
    suite.report_results()
    
