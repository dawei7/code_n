"""Solution for greedy_01: Activity Selection.

Given n activities with start and finish times, pick the maximum
number of non-overlapping activities.
Greedy: sort by finish time, then pick each activity whose start is
at or after the finish of the last picked.
Requirement: O(n log n).
Source: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

Inputs passed to solve():
    start: list of n activity start times.
    finish: list of n activity finish times (parallel to start).
    n: number of activities.

Goal:
    the maximum number of non-overlapping activities that can be selected.

Samples:
Sample 1 input:  start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9], n = 6
Sample 1 output: 4

Sample 2 input:  start = [1, 2, 3], finish = [2, 3, 4], n = 3
Sample 2 output: 3

Sample 3 input:  start = [0, 5, 8], finish = [4, 6, 9], n = 3
Sample 3 output: 2

"""

def solve(start, finish, n):
    # Write your code here.
    return None
