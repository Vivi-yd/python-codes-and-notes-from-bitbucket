"""
Monte Carlo Tic-Tac-Toe Player by vivi
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.

#### helper functions ######

    
def keywithmaxval(dic):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     val = list(dic.values())
     key = list(dic.keys())
     return key[val.index(max(val))]
    
    
##### Core functions #######

def mc_trial(board, player):
    """
    play a game starting with the given player by making random moves, 
    alternating between players. Return when the game is over. 
    The modified board will contain the state of the game, 
    so the function does not return anything.
    """
    opponent = provided.switch_player(player)
    # run the loop until game ends
    
    while True:
        # find an empty square (tuple) for player
        empty = random.choice(board.get_empty_squares())
        # place player on the sqaure
        board.move(empty[0], empty[1], player)
        # break if game had ended
        if board.check_win():
            break
        # find another empty sqaure for opponent
        nxt_empty = random.choice(board.get_empty_squares())
        # place opponent on that sqaure
        board.move(nxt_empty[0], nxt_empty[1], opponent)
        if board.check_win():
            break
    


def mc_update_scores(scores, board, player):
    """
    The function should score the completed board and update the scores grid. 
    As the function updates the scores grid directly, it does not return anything
    """

    # get board dimension
    board_dim = board.get_dim()
    opponent = provided.switch_player(player)
    # loop over every tile in the board
    for row in range(board_dim):
        for col in range(board_dim):
            

            # if player win the game, check status of each tile then score
            # in favour where player played
            if board.check_win() == player:
                tile_status = board.square(row, col)
                if tile_status == player:
                    scores[row][col] += MCMATCH
                elif tile_status == opponent:
                    scores[row][col] -= MCOTHER
            
            # if opponent win the game, again check status and score each tile
            elif board.check_win() == opponent:
                tile_status = board.square(row, col)
                if tile_status == player:
                    scores[row][col] -= MCMATCH
                elif tile_status == opponent:
                    scores[row][col] += MCOTHER
                

def get_best_move(board, scores):
    """
    Find all of the empty squares with the maximum score and randomly return one of them 
    as a (row, column) tuple. 
    Error if call with a board that has no empty squares (no more move)
    """
    # create a dict to store scores with their corresponding empty tile
    score_dict = {}
    
    # run a loop to append the list with score
    for tile in board.get_empty_squares():
        score_dict[tile] = scores[tile[0]][tile[1]]
        
    # return the tile with the maximum score, randomly choose one if there are multiple
   
    return keywithmaxval(score_dict)


def mc_move(board, player, trials):
    """
    Use the Monte Carlo simulation to return a move for the machine player 
    in the form of a (row, column) tuple.
    """
    # create a clone of original board
    clone_board = board.clone()
    # get dimension of board
    dim = clone_board.get_dim()
    # create a score list with dimension identical to board
    scores_list = [[0]*dim]*dim
    # keep track of game played
    game_played = 0
    # play trials game of the clone board and give each square on the
    # board their scores
    while game_played <= trials:
        mc_trial(clone_board, player)
        mc_update_scores(scores_list, clone_board, player)
        game_played += 1
        #cloning board after each loop
        clone_board = board.clone()
    # return the square with best score with respect to the original board

    return get_best_move(board, scores_list)        




# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
#provided.play_game(mc_move, NTRIALS, False) 
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)