# Car Pooling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1094 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/car-pooling/) |

## Problem Description

### Goal

A car begins with `capacity` empty seats and travels only east, so it cannot turn around and revisit a location to the west. Locations are measured in kilometers east of the car's starting point.

Each entry `trips[i] = [numPassengers_i, from_i, to_i]` describes a group that enters at `from_i` and leaves at `to_i`. Determine whether the car can pick up and drop off every group without the number of passengers on board ever exceeding `capacity`.

### Function Contract

**Inputs**

- `trips`: a list of $n$ triples `[numPassengers, from, to]`, where $1 \leq n \leq 1000$, $1 \leq \texttt{numPassengers} \leq 100$, and $0 \leq \texttt{from} < \texttt{to} \leq 1000$.
- `capacity`: the number of seats, with $1 \leq \texttt{capacity} \leq 10^5$.

**Return value**

Return `True` if every trip can be served without exceeding `capacity`; otherwise return `False`.

### Examples

**Example 1**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 4`
- Output: `False`

At location 3, both groups are aboard and require five seats.

**Example 2**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 5`
- Output: `True`
