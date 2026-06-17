"""Solution for dp_22: Egg Dropping.

Return the minimum number of trials needed in the worst
case to find the critical floor. dp[e][f] = min trials for
e eggs and f floors. Drop from floor x -> 1 + worst(
dp[e-1][x-1] (breaks), dp[e][f-x] (survives)).
Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

Inputs passed to solve():
    eggs: number of eggs (1..6 in the setup).
    floors: number of floors (1..10 in the setup).

Goal:
    the minimum worst-case number of trials.

Samples:
Sample 1 input:  eggs = 1, floors = 10
Sample 1 output: 10

Sample 2 input:  eggs = 2, floors = 6
Sample 2 output: 3


"""

def solve(eggs, floors):
    # Write your code here.
    return None
