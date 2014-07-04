"""
Planner for Yahtzee by vivi
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    # Hand is a tuple of dice values rolled.
    # count repetition of each value in dice. Compute score by multiplying the
    # recurring times to the value.
    # append to the computed score to a storing list.
    # find maximum in that list
    
    # a score list that stores the score corresponding to each value of die rolled.
    score_lst = [val * hand.count(val) for val in hand]
    
    return max(score_lst)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    # define score from dice being rolled for all possible outcomes
    tot_score = 0
    # all outcomes that the die can generate
    outcomes = set([val for val in range(1, num_die_sides + 1)])
    # find all sequences that can be generated from rolling num_free_dice
    roll_seqs = gen_all_sequences(outcomes, num_free_dice)
    # length of sequences
    seq_len = len(roll_seqs)
    
    # interate
    for seq in roll_seqs:
        combined_hand = held_dice + seq
        single_score = score(combined_hand)
        tot_score += single_score
    
    # fianlly compute expected value according w.r.t the probability of each outcome.
    expected_val = 1.0 * tot_score/seq_len  
    
    
    return expected_val


def lst_to_tup(lst_of_lst):
    """ 
    coverting list of list to set of tups
    """
    result_tup = set([])
    for lst in lst_of_lst:
        result_tup.add(tuple(lst))
        
    return result_tup    
        


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    # initiate a list for all possible holds 
    all_choices_lst = []
    # define a set that represent choose/not choose (like on/off switch)
    choice = [1, 0]
    
    # generates all possible ways (will be called vectors like matrices)
    # of choosing or not choosing in a list of 3
    vectors = gen_all_sequences(choice, len(hand))
    
    
    # for each vector in vectors
    for vec in vectors:
        # interate over the each value in vector
        temp_list = []

        for idx in range(len(vec)):
 
            # if the value is 1, add the corresponding value of the index in
            # hand into the temparory set
            if vec[idx] == 1:
                temp_list.append(hand[idx])
        # then add the temp_set into the list of all possible holds        
        all_choices_lst.append(temp_list)    
    
    
    return lst_to_tup(all_choices_lst)




def keywithmaxval(dic):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     val = list(dic.values())
     key = list(dic.keys())
     return key[val.index(max(val))]




def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    # generate all possible hold from given hand
    all_hold = gen_all_holds(hand)
    # a dic to hold value associated with corresponding hold as keys.
    all_hold_val = {}
    
    for held in all_hold:
        held_val = expected_value(held, num_die_sides, len(hand) - len(held))
        all_hold_val[held] = held_val
        
    best_hold = keywithmaxval(all_hold_val)    
    
    
    return (all_hold_val[best_hold], best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

## my test: score()
#import user35_3jVHRE048V_5
#user35_3jVHRE048V_5.score_test(score)

## test: expected_value()
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                           
    
    


