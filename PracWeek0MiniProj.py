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
        
        legal_move_index = []
        for i in range(len(self.configuration)):
            if self.is_legal_move(i):
                legal_move_index.append(i)
                return min(legal_move_index)
            
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
        for i in range(1, len(self.configuration)):
            if self.is_legal_move(i):
                moves.append(i)
                self.apply_move(i)
        return moves
    
    
import poc_mancala_testsuite                
poc_mancala_testsuite.run_test(Solitaire_Mancala)
import poc_mancala_gui
poc_mancala_gui.run_gui(Solitaire_Mancala())