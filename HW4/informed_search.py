# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s):
# ----------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation

Your task for homework 4 is to implement:
1.  astar
2.  single_heuristic
3.  better_heuristic
4.  gen_heuristic
"""
import math

import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    closed = set()
    fringe = data_structures.PriorityQueue()
    current = problem.start_state()
    root = data_structures.Node(current, None, None, 0)
    fringe.push(root, 0)
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()
        if node.state not in closed:
            closed.add(node.state)
            for node_state, action, action_cost in problem.expand(node.state):
                child_node = data_structures.Node(node_state, node, action, node.cumulative_cost + action_cost)
                priority = child_node.cumulative_cost + heuristic(node_state, problem)
                fringe.push(child_node, priority)
    return None


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def manhattan_distance(sammy, medal):
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
    disX = abs(sammyX - medalX)
    disY = abs(sammyY - medalY)
    return disX + disY


def single_heuristic(state, problem):
    """
    Running A* using the Manhattan distance heuristic
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: the Manhattan distance from sammy to medal
    """
    if not problem.is_goal(state):
        return manhattan_distance(state[0], state[1][0])
    return 0


def total_carrot(sammy, medal):
    """
        Compute the number of carrots that  Sammy consumes to reach the
        given medal.
        :param sammy (tuple) representing the position of Sammy in the grid
        :param medal (tuple) representing the position of a given medal
        per step for each direction
        :return: (integer) the number of carrots consumed assuming Sammy
                 does not take any unnecessary detours.
        """
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    cost = {EAST: 15, WEST: 1, SOUTH: 2, NORTH: 14}
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


def better_heuristic(state, problem):
    """
    Running A* using the total carrots consumed heuristic
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: the total number of carrots consumer to get to the medal
    """
    if not problem.is_goal(state):
        return total_carrot(state[0], state[1][0])
    return 0


def max_carrots_medal(sammy, medals):
    """
    Find the medal that Sammy consumes the most carrots to reach.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medalal
    per step for each direction
    :return: (tuple) the position of the medal with the max carrots consumed
    """
    # Enter your code here and remove the pass statement below
    if not medals:
        return None

    return max((medal for medal in medals), key=lambda m: total_carrot(sammy, m))


def gen_heuristic(state, problem):
    """
    running A* using the total carrots consumed to reach the most carrot consumed medal
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: the total of carrots consumed to get to the most carrot consumed medal
    """
    if not problem.is_goal(state):
        target = max_carrots_medal(state[0], state[1])
        return total_carrot(state[0], target)
    return 0
