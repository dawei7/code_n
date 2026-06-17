"""Solution for greedy_12: Max Trains for Stoppage.

A single platform can hold one train at a time. Given arrival and
departure times for n trains, find the maximum number that can be
served without overlap. Greedy: sort by departure, accept a train
iff its arrival is >= the last accepted departure.
Requirement: O(n log n).
Source: https://www.geeksforgeeks.org/maximum-trains-stoppage-can-use/

Inputs passed to solve():
    arrivals: list of n arrival times.
    departures: list of n departure times (parallel to arrivals).
    n: number of trains.

Goal:
    the maximum number of trains that can be served without conflict.

Samples:
Sample 1 input:  arrivals = [100, 120, 150, 200], departures = [110, 130, 210, 220], n = 4
Sample 1 output: 3

Sample 2 input:  arrivals = [900, 1000, 1100], departures = [1000, 1100, 1200], n = 3
Sample 2 output: 3


"""

def solve(arrivals, departures, n):
    # Write your code here.
    return None
