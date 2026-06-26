"""
Description
-----------
Given n activities with start and finish times, pick the maximum
number of non-overlapping activities.
Greedy: sort by finish time, then pick each activity whose start is
at or after the finish of the last picked.
Requirement: O(n log n).
Source: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

Examples
--------
Example 1:
Input:  start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9], n = 6
Output: 4

Example 2:
Input:  start = [1, 2, 3], finish = [2, 3, 4], n = 3
Output: 3

Example 3:
Input:  start = [0, 5, 8], finish = [4, 6, 9], n = 3
Output: 2
"""

def solve(start, finish, n):
    # Write your code here.
    return None
