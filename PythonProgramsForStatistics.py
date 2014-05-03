##THIS PROGRAM ARE WRITTEN BASED ON PYTHON 2.7
#programs to compute statistics related operation

#(this program CANNOT be run partially, as this may cause error in calling functions)
#=================================================

#all function calls below take a list as its argument unless stated otherwise
##example format of list: [1,2,3,4]

import math

import scipy.stats ##added by ashu774
###to compute "Mean" of a data set
  

def mean(data_list):

    total = 0

    for value in data_list:
        total += value

    return total/float(len(data_list))




###to find the "Median" of a data set

def median(data_list):

    #sort the list in order from smallest to largest
    
    ordered_list = sorted(data_list)

    #median is the average of the two middle value of the ordered list if
    #list has an even number of values

    if len(data_list) % 2 == 0:
        median = (ordered_list[len(data_list)/2 - 1]
                  + ordered_list[len(data_list)/2])/2.0

    #otherwise, if list has odd number of values, median is the middle value

    else:
        median = ordered_list[len(data_list)//2]

    return median





###to find the "Mode" of a data set

def mode(data_list):

    data_list = sorted(data_list)

    #occurances of different elements in list

    occurance_counts = []

    i = 0

    #location where the program is evaluating after each run of the "for loop"

    index = 0

    #counting occurances of each element

    count = 0

    for value in data_list:

        #comparing the element in index "i" to the next element
        #and check whether they are the same
        
        if data_list[i] == data_list[i + 1]:

            count += 1

            i += 1

        else:
            return count

        #assigning the number of occurances back to the corresponding element

        count = data_list[index]

        index += 2

    #grouping up all the result from occurances counting to the orgininal empty list

    occurance_counts = occurance_counts.append(count)

    #return the corresponding element from
    #the list that has the largest number of occurances
    
    return max(occurance_counts)
    

-    
-### break it in two components
-#    1. define a helper function which counts how many times an element occur in a list
-#    2. define a main function .. which chooses which element has the highest count 




###to compute the "Population Variance(Sigma squared)" of a data set
  

def pop_var(data_list):

    total = 0

    for value in data_list:
        total += (value - mean(data_list))**2.0


    return total/len(data_list)



###to compute the "Population Standard Deviation(Sigma)" of a data set

def pop_sd(data_list):
    
    return math.sqrt(pop_var(data_list))



###to compute the "Sample Variance(s^2)" of a data set

def sam_var(data_list):

    total = 0

    for value in data_list:
        total += (value - mean(data_list))**2.0

    return total/float((len(data_list) - 1))



###to compute the "Sample Standard Deviation(s)" of a data set

def sam_sd(data_list):

    return math.sqrt(sam_var(data_list))
    
##added by ashu774
import numpy as np
import scipy.stats
from math import sqrt

def mean(x):
    """
    x: a list

    returns mean of the values in the list.
    """
    assert type(x) is list, \
    "x must be a list"
    return np.mean(x)

def median(x):
    """
    x: a list

    returns median of the values in the list.
    """
    assert type(x) is list, \
    "x must be a list"
    return np.median(x)
            
def mode(x):
    """
    x: a list

    returns mode of the values in the list.
    """
    assert type(x) is list, \
    "x must be a list"
    mode = None
    maxCount = 0
    for value in x:
        count = x.count(value)
        if count > maxCount:
            maxCount = count
            mode = value            
            
    return mode

def variance(x):
    """
    x: a list

    returns population variance for values in the list.
    """
    squaredDeviations = 0
    average = mean(x)
    for value in x:
        squaredDeviations += (value-average)**2

    return 1.0 * squaredDeviations/len(x)                

def sd(x):
    """
    x: a list

    returns population standard deviation for values in the list.
    """
    return sqrt(variance(x))
    
def percentileList(x, t):
    """
    x: a list
    t: value for which percentile score is to be calculated
    
    returns the 'weak' percentile score of the value in the list
    """
    return scipy.stats(x, t, kind = 'weak')

    
def percentileNormal(x, mean, sd):
    """
    mean: mean of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns percentile score of x for the given normal distribution
    """
    #define the normal distribution with the given mean and sd
    normalDistribution = scipy.stats.norm(mean, sd)
    #return the percentile (proportion of values above which x lies)
    #cdf here stands for the cumulative distribution function
    return normalDistribution.cdf(x)
            
def zscore(x,mean, sd):
    """
    mean: average of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns z score of the value given mean and sd of the normal distribution
    """
    return float(x - mean)/sd

def trueScoreNormal(z,mean, sd):
    """
    z: z score of the value
    mean: average of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns x, the true value given mean,sd and z-score in a normal distribution
    """
    return float(mean + sd * z)


def proportionAbove(x, mean, sd):
    """
    mean: mean of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns proportion of scores above x in the given normal distribution
    """
    return 1- percentileNormal(x, mean, sd)

def proportionBetween(x, y, mean, sd):
    """
    mean: mean of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns proportion of scores between x and y in the given normal distribution
   
    """ 
    inBetween = percentileNormal(x, mean, sd) - percentileNormal(y, mean, sd) 
    if x > y:
        return  inBetween
    else:
        return -1.0 * inBetween

def desiredScore(p, mean, sd):
    """
    mean: mean of the normal distribution
    sd: standard deviation of the normal distribution
    
    returns the score correspoding to the given percentile
    
    """
    high = mean + 5.0 * sd
    low = mean - 5.0  * sd
    guess = (high + low)/2.0
    while abs(percentileNormal(guess, mean, sd) - p) > 0.001:
        if percentileNormal(guess, mean, sd) > p:
            high = guess
        else:
            low = guess
        #update guess
        guess = (high + low)/2.0

    return guess                                        
