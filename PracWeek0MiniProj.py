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
    suite.run_test(game.get_num_seeds(2), first_config(2), "test 2: get_num_seeds")
    
    
    #test is_legal_move method
    suite.run_test(game.is_legal_move(0), False, "test 3.1: is_legal move")
    suite.run_test(game.is_legal_move(1), True, "test 3.2: is_legal_move")
    suite.run_test(game.is_legal_move(3), True, "test 3.3: is_legal_move")
    
    
    #test apply_move method
    game.apply_move(1)