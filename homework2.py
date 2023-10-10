# ----------------------------------------------------------------------
# Name:        homework2
# Purpose:     Practice writing Python functions
#
# Author:     Rula Khayrallah
# ----------------------------------------------------------------------
"""
Implement functions to track Sammy's consumption of carrots.

Sammy is an eco-friendly intelligent agent powered by carrots.
His task is to collect medals at various positions in a grid.
Sammy can only move North, South, West or East.
The carrot consumption per step for each direction is given by a
dictionary that is passed to some of the functions.
The functions must work with any dictionary specifying the carrot
consumption.
"""

# Use these constants in your functions
NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

def steps_to_medal(sammy, medal):
    """
    Compute the number of steps that  Sammy needs to take to reach the
    given medal assuming he does not take any unnecessary detours.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medal (tuple) representing the position of a given medal
    :return: (integer) the number of steps taken assuming Sammy
             does not take any unnecessary detours.
    """
    # Enter your code here and remove the pass statement below
    (sammyX, sammyY) = sammy
    (medalX, medalY) = medal
    steps = abs(sammyX - medalX) + abs(sammyY - medalY)
    return steps

def carrots_to_medal(sammy, medal, cost):
    """
    Compute the number of carrots that  Sammy consumes to reach the
    given medal.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medal (tuple) representing the position of a given medal
    :param cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots consumed assuming Sammy
             does not take any unnecessary detours.
    """
    # Enter your code here and remove the pass statement below
    (sammyX, sammyY) = sammy
    (medalX, medalY) = medal
    total = 0
    if (sammyX - medalX) > 0:
        total += cost[WEST] * (sammyX - medalX)
    elif (sammyX - medalX) < 0:
        total += cost[EAST] * abs(sammyX - medalX)

    if (sammyY - medalY) > 0:
        total += cost[NORTH] * (sammyY - medalY)
    elif (sammyY - medalY) < 0:
        total += cost[SOUTH] * abs(sammyY - medalY)

    return total

def max_carrots(sammy, medals, cost):
    """
    Compute the number of carrots that Sammy consumes to get to the
    costliest medal in the set.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots.
    """
    # Enter your code here and remove the pass statement below
    if not medals:
        return None

    return max(carrots_to_medal(sammy,medal,cost) for medal in medals)

def min_carrots_medal(sammy, medals, cost):
    """
    Find the medal that Sammy consumes the fewest carrots to reach.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (tuple) the position of the medal
    """
    # Enter your code here and remove the pass statement below
    if not medals:
        return None

    return min((medal for medal in medals), key=lambda m: carrots_to_medal(sammy,m,cost))



def main():
    # The main function is used to test the 4 functions.
    sammy1 = (10, 3)
    sammy2 = (2, 2)
    carrots1 = {WEST: 10, EAST: 100, SOUTH: 3, NORTH: 5}
    carrots2 = {NORTH: 5, EAST: 3, WEST: 7, SOUTH: 2}
    print('----------Testing the steps_to_medal function----------')
    print(steps_to_medal(sammy1, (3, 1)))  # 9
    print(steps_to_medal(sammy1, (0, 8))) # 15
    print(steps_to_medal(sammy1, (10, 6))) # 3
    print(steps_to_medal(sammy1, (14, 3))) # 4
    print(steps_to_medal(sammy1, (13, 7)))  # 7
    print(steps_to_medal(sammy1, (10, 3)))  # 0
    print('----------')
    print(steps_to_medal(sammy2, (3, 1)))  # 2
    print(steps_to_medal(sammy2, (0, 8)))  # 8
    print(steps_to_medal(sammy2, (10, 6)))  # 12
    print(steps_to_medal(sammy2, (14, 3)))  # 13
    print(steps_to_medal(sammy2, (13, 7)))  # 16
    print(steps_to_medal(sammy2, (10, 3)))  # 9
    print('----------Testing the carrots_to_medal function----------')
    print(carrots_to_medal(sammy1, (3, 1), carrots1))  # 80
    print(carrots_to_medal(sammy1, (0, 8), carrots1))  # 115
    print(carrots_to_medal(sammy1, (10, 6), carrots1)) # 9
    print(carrots_to_medal(sammy1, (14, 3), carrots1)) # 400
    print(carrots_to_medal(sammy1, (13, 7), carrots1)) # 312
    print(carrots_to_medal(sammy1, (10, 3), carrots1)) # 0
    print('----------')
    print(carrots_to_medal(sammy2, (3, 1), carrots2))   # 8
    print(carrots_to_medal(sammy2, (0, 8), carrots2))   # 26
    print(carrots_to_medal(sammy2, (10, 6), carrots2))  # 32
    print(carrots_to_medal(sammy2, (14, 3), carrots2))  # 38
    print(carrots_to_medal(sammy2, (13, 7), carrots2))  # 43
    print(carrots_to_medal(sammy2, (10, 3), carrots2))  # 26
    print('----------Testing the max_carrots function----------')
    medals1 = {(3, 1), (0, 8), (13, 7), (2, 4), (10, 6), (14, 3), (3, 2)}
    medals2 = {(10, 3)}
    nomedals = set()
    print(max_carrots(sammy1, medals1, carrots1)) # 400
    result = max_carrots(sammy1, nomedals, carrots1)
    print (result is None) # True
    print(max_carrots(sammy1, medals2, carrots1))  # 0
    print(max_carrots(sammy2, medals1, carrots2))  # 43
    result = max_carrots(sammy2, nomedals, carrots2)
    print(result is None)  # True
    print(max_carrots(sammy2, medals2, carrots2))  # 26
    print('-------Testing the min_carrots_medal function-------')
    print(min_carrots_medal(sammy1, medals1, carrots1)) # (10, 6)
    print(min_carrots_medal(sammy2, medals1, carrots1))  # (2, 4)
    result = min_carrots_medal(sammy1, nomedals, carrots1)
    print(result is None)  # True
    print(min_carrots_medal(sammy2, medals2, carrots1)) # (10, 3)

if __name__ == '__main__':
    main()
