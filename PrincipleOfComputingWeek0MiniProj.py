"""
Clone of 2048 game.
"""

import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
 
#Helper functions for merge():
    
def zero_to_right(line):
    
    """ Helper function for merge() that put all non-zero term
    to the left with no space. i.e. zero's to the right"""
    
    length = len(line)
    result = [0] * length
    idx = 0
    for num in line:
        if num != 0:
            result[idx] = num
            idx += 1
    #print result        
    return result
            
### Test    
zero_to_right([0, 4, 4, 0])
zero_to_right([0, 0, 2, 0])
zero_to_right([2, 2, 4, 0])
zero_to_right([0, 4, 2, 2])


def next_occ(seq, idx):
    """find the index of next value that is the same and to the right of current index """
    
    if seq[idx + 1:].count(seq[idx]) > 0:
         new_idx = seq[idx + 1:].index(seq[idx])
         return new_idx + idx + 1
        
    else:
        return -9999 #safer :P

    
    
###Test         
print next_occ([4, 0, 4, 0], 1)
print next_occ([0, 2, 2, 0], 0)
print next_occ([2, 2, 2, 2], 0)
print next_occ([8, 0, 3, 2, 4, 0, 3, 0, 0], 2)


def check_gap(seq, idx1, idx2):
    """check if there are any non-zero entries in between idx1 and idx2"""
    
    
    for i in range(idx1 + 1, idx2):
        if seq[i] != 0:
            return True
    
    return False
    
### Test
print check_gap([4, 0, 4, 0], 0, 2)
print check_gap([0, 2, 2, 0], 0, 3)
print check_gap([2, 2, 2, 2], 0, 3)
print check_gap([8, 0, 3, 2, 4, 0, 3, 0, 0], 2, 6)
print check_gap([0, 0, 2, 0, 0, 0], 2, 5)


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    
    result_list = [0] * len(line)
    #keep track of indexes which are not to be merged
    merged = []

    for i in range(len(line)):
        second_occurence = next_occ(line, i)
        first_bool = not(check_gap(line, i, second_occurence))
        second_bool =  not(i in merged)
        #element will merge if it occurs again there are no non-zeros in between or
        #it was not created by merge itself
        if second_occurence != -9999 and first_bool and second_bool:
            print second_occurence
            result_list[second_occurence] = 2 * line[i]
            merged.append(second_occurence)
        elif second_bool:
            result_list[i] = line[i]

        
    return zero_to_right(result_list)
   

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        pass
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        pass
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        pass

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return 0
 


import user34_K9swOlUgbQ_24

user34_K9swOlUgbQ_24.zero_to_right_test(zero_to_right)

user34_K9swOlUgbQ_24.next_occ_test(next_occ)

user34_K9swOlUgbQ_24.check_gap_test(check_gap)

user34_K9swOlUgbQ_24.merge_test(merge)
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))