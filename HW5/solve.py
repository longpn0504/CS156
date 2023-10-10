# ----------------------------------------------------------------------
# Name:     solve
# Purpose:  homework 5
#
# Author:   Rula Khayrallah
#
# Copyright ©  Rula Khayrallah
# ----------------------------------------------------------------------
"""
Main module to solve n-queens puzzles.

Usage:  usage: solve.py N q1 [--AC3]
N is the number of queens and columns/rows
q1  is the row position associated with the queen in column 1 (Q1).
--AC3 is optional.  When specified, the AC3 algorithm is invoked
        as a  preprocessing step.
Examples:
    solve.py 10 2 --AC3
    solve.py 4 3
"""

import argparse
import time
import random
import queens


def write_solution(assignment):
    """
    Print the puzzle solution.
    :param assignment: a dictionary representing the puzzle solution.
        The dictionary keys are the queens' columns and the values are
        the corresponding assigned rows.
    :return: None
    """
    n = len(assignment)
    for queen in range(1, n+1):
        print(f'Q{queen}: row {assignment[queen]}')


def get_arguments():
    """
    Parse and validate the command line arguments
    :return: tuple containing the arguments: ac3, N and position of Q1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--AC3',
                        help='AC3 Preprocessing?',
                        action='store_true')
    parser.add_argument('N',
                        help='How many queens?',
                        type=int)
    parser.add_argument('q1',
                        help='Where do you want Q1?',
                        type=int)

    arguments = parser.parse_args()

    n = arguments.N
    ac3 = arguments.AC3
    q1 = arguments.q1
    if q1 < 1 or q1 > n:
        parser.error('Invalid row for Q1')
    return ac3, n, q1


def main():
    random.seed(1) # for consistent results
    ac3, n, q1 = get_arguments()
    if ac3:
        approach = "btrackac3"
    else:
        approach = "btrack"
    approach_function = getattr(queens, approach)

    start_time = time.time()
    solution, csp = approach_function(n, q1)
    elapsed_time = time.time() - start_time
    print('Processing time: {:.4f} (sec)'.format(elapsed_time))
    print(f'Nodes Expanded: {csp._nodes:,}')
    if solution is not None:
        write_solution(solution)
    else:
        print("Unable to solve the puzzle.")


if __name__ == '__main__':
    main()
