# Gas Station

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 134 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/gas-station/) |

## Problem Description
### Goal
Stations are arranged in a circle. At station `i`, a car may add `gas[i]` units of fuel, and driving clockwise to the next station consumes `cost[i]` units. The car begins with an empty tank at whichever station you choose and cannot let its fuel balance become negative during the trip.

Return the zero-based starting index that allows one complete clockwise circuit and arrival back at that station. If no starting point can finish the circuit, return `-1`. The input guarantee makes a feasible answer unique, although fuel left over after individual legs may carry forward and compensate for later expensive segments.

### Function Contract
**Inputs**

- `gas`: fuel available at each station
- `cost`: fuel required for each corresponding outgoing edge

**Return value**

The unique valid starting index when a circuit is possible; otherwise `-1`.

### Examples
**Example 1**

- Input: `gas = [1,2,3,4,5], cost = [3,4,5,1,2]`
- Output: `3`

**Example 2**

- Input: `gas = [2,3,4], cost = [3,4,3]`
- Output: `-1`

**Example 3**

- Input: `gas = [5], cost = [4]`
- Output: `0`
