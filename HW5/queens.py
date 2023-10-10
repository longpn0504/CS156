# ----------------------------------------------------------------------
# Name:     queens
# Purpose:  Homework 5
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
N-queens puzzle solver implementation

btack:      basic backtracking search
btrackac3:  backtracking search with AC-3 as a preprocessing step
"""
import csp


# Enter your helper functions here
def domain(n, q1):
    domainDic = {}
    for i in range(1, n + 1):
        if i == 1:
            domainDic[i] = {q1}
        else:
            domainDic[i] = set(range(1, n + 1))
    return domainDic


def neighbor(n):
    neighborDic = {}
    for i in range(1, n + 1):
        neighborDic[i] = set(j for j in range(1, n + 1) if i != j)
    return neighborDic


def constraint(var1, val1, var2, val2):
    if abs(var1 - var2) == abs(val1 - val2):
        return False
    if val1 == val2:
        return False
    return True


def btrack(n, q1):
    """
    Solve the given puzzle with basic backtracking search
    :param n: is the number of queens
    :param q1: the row position associated with the queen in column 1
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    cspObject = csp.Csp(domain(n, q1), neighbor(n), constraint)
    return cspObject.backtracking_search(), cspObject


def btrackac3(n, q1):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param n: is the number of queens
    :param q1: the row position associated with the queen in column 1
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    cspObject = csp.Csp(domain(n, q1), neighbor(n), constraint)
    cspObject.ac3_algorithm()
    return cspObject.backtracking_search(), cspObject
