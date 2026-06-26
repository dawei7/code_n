"""Optimal solution for greedy_12: Max Trains for Stoppage.

A single platform can hold one train at a time. Given arrival
and departure times for n trains, find the maximum number that
can be served without overlap. Greedy: sort by departure, accept
a train iff its arrival is after the last accepted departure.
O(n log n) for the sort.
"""


def solve(arrivals, departures, n):
    if n == 0:
        return 0
    order = sorted(range(n), key=lambda i: (departures[i], arrivals[i]))
    count = 0
    last_departure = -1
    for i in order:
        if arrivals[i] >= last_departure:
            count += 1
            last_departure = departures[i]
    return count
