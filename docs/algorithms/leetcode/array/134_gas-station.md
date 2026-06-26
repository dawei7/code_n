# Gas Station

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_214` |
| Frontend ID | 134 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [gas-station](https://leetcode.com/problems/gas-station/) |

## Problem Description & Examples
### Goal
There are `n` gas stations along a circular route, where the amount of gas at the `i`-th station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`-th station to its next `(i + 1)`-th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

### Function Contract
**Inputs**

- `gas`: List[int]
- `cost`: List[int]

**Return value**

int - starting gas station index or -1

### Examples
**Example 1**

- Input: `gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]`
- Output: `3`

**Example 2**

- Input: `gas = [7, 1, 5], cost = [9, 8, 7]`
- Output: `-1`

**Example 3**

- Input: `gas = [10, 2], cost = [5, 2]`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
