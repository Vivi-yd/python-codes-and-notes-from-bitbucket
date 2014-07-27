""" Word Wrangler v1.2 by vivi D"""


import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    # create an answer list that will store all elements with no duplicates.
    no_dup = []
    
    # compare each elements in the input list up to but not include the
    # last element with the next elements in the list
    # only append to the answer list if not identical
    if len(list1) < 2:
        return list1
    else:
        for idx in range(len(list1)- 1):
            if list1[idx] != list1[idx + 1]:
                no_dup.append(list1[idx])
    
    # append the last element to the answer list        
    no_dup.append(list1[-1])
    
    return no_dup


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.
    """
    # create an empty list for storing intersections of the 2 inputs
    intersn = []
    
    # incrementing index for list1 and list2
    incr_idx1 = 0
    incr_idx2 = 0
    
    # while non of the indices surpass the length of both lists
    while incr_idx1  < len(list1) and incr_idx2 < len(list2):
        # compare the values from both lists at current indices
        # increment the one with smaller value
        if list1[incr_idx1] < list2[incr_idx2]:
            incr_idx1 += 1
        elif list1[incr_idx1] > list2[incr_idx2]:
            incr_idx2 += 1
        # append the value if equal and increment indices
        else:
            intersn.append(list1[incr_idx1])
            incr_idx1 += 1
            incr_idx2 += 1
            
    return intersn        
    

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    
    merged = []
    
    #indices for iterating over lst1 and lst2
    idx = 0
    jdx = 0
    while idx < len(list1) and jdx < len(list2):
        if list1[idx] < list2[jdx]:
            #append lst1[idx] to merged and increment index
            merged.append(list1[idx])
            idx += 1
        else:
            merged.append(list2[jdx])
            jdx += 1
    
    # extend the list with the remaining uniterated elements
    merged.extend(list1[idx:])
    merged.extend(list2[jdx:])
    
    return merged

def merge_sort(list1):
    """
    input: list1 - an unsorted list
    output: sorted - a new sorted list that contains all the elements from list1
    in ascending order
    """
    leng = len(list1)
    # base case
    if leng < 2:
        return list1
    
    # recursive steps that repeat until the base case is achived
    else:
        # split list in half
        split1 = list1[:(leng/2)]
        split2 = list1[(leng/2):]
        
        # call merge_sort to each
        sorted1 = merge_sort(split1)
        sorted2 = merge_sort(split2)
        
    # merge the 2 sorted halves and return  
    return merge(sorted1, sorted2)



# Function to generate all strings for the word wrangler game

def insert(item, string):
    """
    input: item - a string to be inserted
           string - a string at which item is be inserted into
    
    output: all_strings - a list of all possible strings can be generated
            by inserting item into all possible position of "string"
    """
    all_strings = []
    
    
    for idx in range(len(string)+1):
        new_str = string[:idx] + item + string[idx:]
        all_strings.append(new_str)
        
    
    return all_strings    


def gen_all_strings(word):
    """
    input: word - a string
    output: all_strings - a list of strings that the letters in the input
    "word" can compose in any order.
    
    * letters are treated as distinct characters even if they are the same letter
    """
    
    # base case, if word has zero length return it directly
    if len(word) < 1:
        return [""]

    # recursive step calling on "rest", all outcomes are stored in rest_string
    else:
        first = word[0]
        rest = word[1:]
    
        
        rest_string = gen_all_strings(rest)
        
        
        # [:] is needed to prevent mutation of rest_string
        # since all_string is changing because of the for loop below
        all_strings = rest_string[:]

        # For each string in rest_strings, generate new strings by inserting 
        # the initial character, "first", in all possible positions within the string.
        for string in rest_string:
            new_strings = insert(first, string)
            all_strings.extend(new_strings)
        
    return all_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(WORDFILE)
    dic = urllib2.urlopen(url)
    
    
    return [word.strip() for word in dic.readlines()]
    

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)


run()



# test 

#import user36_vhj847Mu48_17 as test_code
#
#test_code.duplicate_test(remove_duplicates)
#test_code.intersect_test(intersect)
#test_code.merge_test(merge)
#test_code.merge_sort_test(merge_sort)
#test_code.gen_all_str_test(gen_all_strings)
#test_code.insert_test(insert)

