###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Jordyn Young
# Collaborators: None
# Time:

import time
sys.path.extend(['/Users/jordynyoung/Documents/Programming/Python/MIT 6.0002/MIT-6.0002/ps1'])
from ps1_partition import get_partitions

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    cows = {}
    with open(filename) as f:
        read_data = f.read().splitlines()
            for entry in read_data:
                temp = entry.split(',')
                cows[temp[0]] = temp[1]
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy = list(map(list, (sorted(cows.items(), key = lambda x: x[1], reverse=True))))
    all_trips = []
    while len(cowsCopy) > 0:
        totalWeight = 0
        current_trip = []
        for i in cowsCopy:
            name = i[0]
            weight = int(i[1])
            if totalWeight + weight <= limit:
                current_trip.append(name)
                totalWeight += weight
                cowsCopy.remove(i)
        all_trips.append(current_trip)
    return all_trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    cowsCopy = dict(cows)
    result = {}

    for partitions in get_partitions(cowsCopy.keys()):
        for trip in partitions:
            totalWeight = 0
            score = []
            for i in trip:
                totalWeight += int(cowsCopy[i])
                if totalWeight <= limit:
                    score.append(1)
                else:
                    score.append(0)
        number_trips = sum(score)
        if 0 not in score:
            result[partitions] = number_trips

    print(min(result.values()))
    
    # TODO: Your code here
    pass
        
# Problem 4
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
