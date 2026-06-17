"""Solution for greedy_06: Gas Station.

n gas stations on a circular route. gas[i] is the fuel at station i,
cost[i] is the fuel to reach i+1. Find a starting index from which
the car can complete the loop, or -1 if none exists.
Requirement: O(n) - one pass tracks the running tank; whenever the
tank goes negative, the start must be after the failing station.
Source: https://www.geeksforgeeks.org/gas-station/

Inputs passed to solve():
    gas: list of n gas amounts at each station.
    cost: list of n fuel costs to the next station.
    n: number of stations.

Goal:
    the index of a valid starting station, or -1 if no valid start exists.

Samples:
Sample 1 input:  gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2], n = 5
Sample 1 output: 3

Sample 2 input:  gas = [2, 3, 4], cost = [3, 4, 3], n = 3
Sample 2 output: -1

Sample 3 input:  gas = [5, 1, 2, 3, 4], cost = [4, 4, 4, 4, 4], n = 5
Sample 3 output: 4

"""

def solve(gas, cost, n):
    # Write your code here.
    return None
