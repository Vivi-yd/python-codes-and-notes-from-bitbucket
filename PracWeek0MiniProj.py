class Solitaire_Mancala:
    
    """ a class for the game Solitaire Mancala """
    
    def __init__(self):
        
        """ initializing configuration """
        
        self.configuration = [0]
                
    def set_board(self, configuration):
        
        """set the board with the initialized configuration """
        
        self.configuration = list(configuration)
        
    def __str__(self):
        
        """ reverses the configuration and covert to string """
        
        lst = list(self.configuration)
        lst.reverse()
        return str(lst)
        
    def get_num_seeds(self, house_num):
        
        """ return number of seeds in the house of index house_num """
        
        return self.configuration[house_num]
    
    def is_legal_move(self, house_num):
        
        """ return whether move of house with index house_num is legal """
        
        return house_num > 0 and house_num == self.configuration[house_num]
        
        
    def apply_move(self, house_num):
        
        """ apply the move if it's legal """
        
        if self.is_legal_move(house_num):
            
            for i in range(house_num):
                self.configuration[i] += 1
            self.configuration[house_num] = 0   
        
    
    def choose_move(self):
        
        """ return the legal move that is closest to the store """
        
        for i in range(1, len(self.configuration)):
            if self.is_legal_move(i):
                return i
        return 0
    
    def is_game_won(self):
        
        """ declare winning of game if all houses are empty """
        
        for i in range(1, len(self.configuration)):
            if self.get_num_seeds(i) != 0:
                return False
        return True
    
    def plan_moves(self):
        
        """ giving a list which is a series of legal moves of the whole game """
        
        moves = []
        the_move = self.choose_move()
        while the_move != 0:
            self.apply_move(the_move)
            moves.append(the_move)
            the_move = self.choose_move()
        return moves    
    
    
import poc_mancala_testsuite                
poc_mancala_testsuite.run_test(Solitaire_Mancala)
import poc_mancala_gui
poc_mancala_gui.run_gui(Solitaire_Mancala())


==============================================================================


""" Test codes for Solitaire Mancala """

import poc_simpletest

def run_test(class_to_be_tested):
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # create a object from the class to be tested
    game = class_to_be_tested()
    
    #test __str__ method
    
    first_config = [0, 1, 1, 3, 0, 0, 0]
    game.set_board(first_config)
    suite.run_test(str(game), str([0, 0, 0, 3, 1, 1, 0]), "test 1: __str__")
    
    #test get_num_seeds method
    suite.run_test(game.get_num_seeds(2), first_config[2], "test 2: get_num_seeds")
    
    
    #test is_legal_move method
    suite.run_test(game.is_legal_move(0), False, "test 3.1: is_legal move")
    suite.run_test(game.is_legal_move(1), True, "test 3.2: is_legal_move")
    suite.run_test(game.is_legal_move(3), True, "test 3.3: is_legal_move")
    
    
    #test apply_move method
    game.apply_move(1)
    suite.run_test(str(game), str([0, 0, 0, 3, 1, 0, 1]), "test 4: apply_move")
    suite.run_test(first_config, [0, 1, 1, 3, 0, 0, 0], "test 4.1: apply_move; see if there's any change in config")
    #test apply_move to an illegal 
    game.apply_move(2)
    suite.run_test(str(game), str([0, 0, 0, 3, 1, 1, 0]), "test 5: applying illegal move")
    
    
    #test choose_move and applying it
    game.set_board(first_config)
    move = game.choose_move()
    suite.run_test(move, 1, "test 6: testing choose_move")
    game.apply_move(move)
    suite.run_test(str(game), str([0, 0, 0, 3, 1, 0, 1]), "test 6.1: applying move as suggested by choose_move")
    
    second_config = [0, 0, 5, 0, 0, 2, 0]
    game.set_board(second_config)
    move = game.choose_move()
    suite.run_test(move, 0, "test 6.2: testing choose_move when there are no legal move")
    
    
    #test is_game_won
    game.set_board(first_config)
    suite.run_test(game.is_game_won(), False, "test 7.1: test is_game_won when not won")
    third_config = [1, 0, 0, 0, 0, 0, 0]
    game.set_board(third_config)
    suite.run_test(game.is_game_won(), True, "test 7.2: test is_game_won when won")
    
    
    # test plan_moves
    game.set_board(first_config)
    moves = game.plan_moves()
    suite.run_test(moves, [1, 3, 1, 2], "test 8.1: test plan_moves ending with win game")
    for each_move in moves:
        game.apply_move(each_move)
    suite.run_test(str(game), str([0, 0, 0, 0, 0, 0, 4]), "test 8.2: applying move as suggested by plan_moves")    
    
    forth_config = [0, 1, 1, 0, 4, 0, 0]
    game.set_board(forth_config)
    moves = game.plan_moves()
    suite.run_test(moves, [1, 4, 1, 2, 1], "test 8.3: test plan_moves ending with lose game")
    for each_move in moves:
        game.apply_move(each_move)
    suite.run_test(str(game), str([0, 0, 0, 1, 0, 0, 5]), "test 8.4: applying move as suggested by plan_move")
    
    
    # reporting test result
    suite.report_results()