"""Solution for bb_02: Job Assignment (Hungarian).

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum total cost over all n!
permutations of jobs. Brute-force enumeration (real solver:
Hungarian algorithm, O(n^3)).
Source: https://www.geeksforgeeks.org/job-assignment-problem-set-1/

Inputs passed to solve():
    cost: n x n cost matrix.
    n: number of workers (= number of jobs).

Goal:
    the minimum total assignment cost.

Samples:
Sample 1 input:  cost = [[9, 2, 7], [6, 4, 3], [5, 8, 1]], n = 3
Sample 1 output: 10 (workers 0,1,2 -> jobs 1,2,2 sum 2+3+1 = 6, or 0,1,2: 9+4+1=14, best is 0->1, 1->2, 2->0: 2+3+5=10)


"""

def solve(cost, n):
    # Write your code here.
    return None
