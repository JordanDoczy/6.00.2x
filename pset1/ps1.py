###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    
    cows_copy = cows.copy() # make a copy to mutate
    transport = [] # start a new transport
    transportWeight = 0 # keep track of transport weight

    # repeat until the transport is full or we run of out suitable cows
    while transportWeight <= limit and len(cows_copy.items()) > 0:
        
        cowToAdd = None # potential cow to add to transport
        cowWeight = 0 # weight of cow to be added to transport
        cows_larger_than_limit = [] # list of cows that exceed limit
        
        # find largest suitable cow
        for cow, weight in cows_copy.items():
            # find largest suitable cow
            if weight > cowWeight and weight <= limit - transportWeight:
                cowWeight = weight
                cowToAdd = cow
            # find cows that exceed the limit
            if weight > limit: 
                cows_larger_than_limit.append(cow)
        
        # remove cows that exceed the limit
        for cow in cows_larger_than_limit:
            cows_copy.pop(cow)

        # if we find a cow:
        # - add it to the transport
        # - increase our transport weight
        # - remove it from the remaining cows
        # else:
        # - no cow suitable cow found, therefore
        # transport is at capacity for given data set
        if cowToAdd:
            transportWeight += cowWeight
            transport.append(cowToAdd)
            cows_copy.pop(cowToAdd)
        else: 
            break

    # recursive call
    # if there are still cows remaining:
    # append the result to the newly created transport
    # else:
    # we return the final transport
    if len(cows_copy.items()) > 0:
        return [transport] + greedy_cow_transport(cows_copy, limit)
    else:
        return [transport]


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(limit,greedy_cow_transport(cows, limit))
#print(cows)

#print(brute_force_cow_transport(cows, limit))


