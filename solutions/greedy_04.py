"""
Description
-----------
Each job has a deadline and a profit, and takes one unit of time.
Schedule jobs to maximise total profit; a job must finish by its
deadline.
Greedy: sort by profit descending; place each job in the latest free
slot <= its deadline.
Requirement: O(n^2) with a boolean slot array, or O(n log n) with a DSU.
Source: https://www.geeksforgeeks.org/job-sequencing-problem/

Examples
--------
Example 1:
Input:  deadline = [2, 1, 2, 1, 3], profit = [100, 19, 27, 25, 15], n = 5
Output: 142

Example 2:
Input:  deadline = [3, 3, 3], profit = [50, 60, 70], n = 3
Output: 120

Example 3:
Input:  deadline = [1, 1, 1], profit = [10, 20, 30], n = 3
Output: 30
"""

def solve(deadline, profit, n):
    # Write your code here.
    return None
