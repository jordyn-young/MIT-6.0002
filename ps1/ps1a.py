###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Jordyn Young
# Collaborators: None
# Time:

import time
from ps1.ps1_partition import get_partitions


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
    names = list(cows.keys())
    best_partition = names
    for partition in get_partitions(names):
        for trip in partition:
            total_weight = 0
            impossible_partition = False
            for cow in trip:
                current_cow_weight = int(cows[cow])
                total_weight += current_cow_weight
            if total_weight > limit:
                impossible_partition = True
                break
        if not impossible_partition and len(partition) < len(best_partition):
            best_partition = partition
    return best_partition


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
    cows = load_cows('ps1/ps1_cow_data.txt')
    start = time.time()
    greedy_cow_transport(cows, limit=10)
    end = time.time()
    print('greedy_cow_transport time:', (end - start), 'seconds')

    start = time.time()
    brute_force_cow_transport(cows, limit=10)
    end = time.time()
    print('brute_force_cow_transport time: ', (end - start), 'seconds')


if __name__ == '__main__':
    cows = load_cows('ps1/ps1_cow_data.txt')
    greedy_cow_transport(cows, limit=10)
    brute_force_cow_transport(cows, limit=10)
    compare_cow_transport_algorithms()
