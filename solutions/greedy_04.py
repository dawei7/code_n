"""Solution for greedy_04: Job Sequencing.

Each job has a deadline and a profit, and takes one unit of time.
Schedule jobs to maximise total profit; a job must finish by its
deadline.
Greedy: sort by profit descending; place each job in the latest free
slot <= its deadline.
Requirement: O(n^2) with a boolean slot array, or O(n log n) with a DSU.
Source: https://www.geeksforgeeks.org/job-sequencing-problem/

Inputs passed to solve():
    deadline: list of n deadlines (1-indexed).
    profit: list of n profits (parallel to deadline).
    n: number of jobs.

Goal:
    the maximum total profit from a feasible schedule.

Samples:
Sample 1 input:  deadline = [2, 1, 2, 1, 3], profit = [100, 19, 27, 25, 15], n = 5
Sample 1 output: 142

Sample 2 input:  deadline = [3, 3, 3], profit = [50, 60, 70], n = 3
Sample 2 output: 120

Sample 3 input:  deadline = [1, 1, 1], profit = [10, 20, 30], n = 3
Sample 3 output: 30

"""

def solve(deadline, profit, n):
    # Write your code here.
    return None
