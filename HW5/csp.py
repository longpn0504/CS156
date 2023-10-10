# ----------------------------------------------------------------------
# Name:    csp
# Purpose: HW 5: implement the Csp class
# ----------------------------------------------------------------------
"""
Class definition for a Constraint Satisfaction Problem.

To create a Csp object, we need to specify the following:
domains: a dictionary representing variables and their domains.
        The dictionary keys are variable names and the values are sets
        representing their domains.
neighbors: a dictionary representing binary constraints.
        The dictionary keys are variable names and the values are sets
        containing all the variables that are connected to the key.
        (Variables are connected if they both appear in a constraint)
constraint: a function that takes as arguments two variables
        and two values: f(var1, val1, var2, val2).
        The function must return True if var1 and var2 satisfy the
        constraint when their respective values are val1 and val2.
"""
import copy
import random

class Csp:
    """
    Represent a Constraint Satisfaction Problem.
    Arguments:
    domains: a dictionary representing variables and their domains.
        The dictionary keys are variable names and the values are sets
        representing their domains.
    neighbors: a dictionary representing binary constraints.
        The dictionary keys are variable names and the values are sets
        containing all the variables that are connected to the key.
        (Variables are connected if they both appear in a constraint)/
    constraint: a function that takes as arguments two variables
        and two values: f(var1, val1, var2, val2).
        The function returns True if var1 and var2 satisfy the
        constraint when their respective values are val1 and val2.

    Attributes:
    domains: a dictionary representing variables and their domains.
        The dictionary keys are variable names and the values are sets
        representing their domains.
    neighbors: a dictionary representing binary constraints.
        The dictionary keys are variable names and the values are sets
        containing all the variables that are connected to the key.
        (Variables are connected if they both appear in a constraint)/
    constraint: a function that takes as arguments two variables
        and two values: f(var1, val1, var2, val2).
        The function returns True if var1 and var2 satisfy the
        constraint when their respective values are val1 and val2.
    """

    def __init__(self, domains, neighbors, constraint):
        self.domains = domains
        self.neighbors = neighbors
        self.constraint = constraint

    def backtracking_search(self):
        """
        Implement the backtracking search algorithm
        :return:  complete consistent assignment or None if failure
        """
        self._nodes = 0  # Keep track of number of nodes
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        """
        Recursive helper function for the backtracking search
        :param assignment: dictionary representing the current
        assignment.
        :return: dictionary representing an assignment
        """
        if len(assignment) == len(self.domains):
            return assignment
        var = self.random_var_selection(assignment)  # select a variable
        self._nodes += 1
        for value in self.domains[var]:
            consistent = self.check_consistent(var, value, assignment)
            if consistent:
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result is not None:
                    return result
                else:
                    del assignment[var]  # backtrack
        return None

    def check_consistent(self, var, value, assignment):
        """
        Check whether the value is consistent with the assignment.
        :param var:  (string) the variable name
        :param value: value from the domain of the variable
        :param assignment: dictionary representing current assignment.
        :return: (boolean) True if assignment is consistent, False
            otherwise
        """
        for neighbor in self.neighbors[var]:
            if neighbor in assignment:
                if not self.constraint(var, value,
                                       neighbor, assignment[neighbor]):
                    return False
        return True

    def random_var_selection(self, assignment):
        """
        Return any unassigned variable in the CSP.
        :param assignment: dictionary representing the current
        assignment.
        :return: A variable in the CSP
        """
        remaining_vars =tuple( set(self.domains) - set(assignment))
        return random.choice(remaining_vars)

    def ac3_algorithm(self):
        """
        Implement the AC-3 algorithm, reducing the variable domains.
        :return: None
        """
        arcs = {(tail, head) for tail in self.domains
                for head in self.neighbors[tail]}
        while arcs:
            (tail, head) = arcs.pop()
            if self.remove_inconsistent_values(tail, head):
                for each_neighbor in self.neighbors[tail]:
                    arcs.add((each_neighbor, tail))

    def remove_inconsistent_values(self, tail, head):
        """
        Enforce the consistency of the arc from tail to head and remove
        all inconsistent values from the domain of the tail.
        :param tail: a variable in the CSP
        :param head: a variable in the CSP
        :return: True if one or more values are removed from the domain
            False otherwise.
        """
        removed = False
        tail_values = copy.copy(self.domains[tail])
        for tail_value in tail_values:
            found = False
            for head_value in self.domains[head]:
                if self.constraint(tail, tail_value, head, head_value):
                    found = True
                    break
            if not found:
                self.domains[tail].remove(tail_value)
                removed = True
        return removed
