# Candy

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_220` |
| Frontend ID | 135 |
| Difficulty | Hard |
| Topics | Array, Greedy |
| Official Link | [candy](https://leetcode.com/problems/candy/) |

## Problem Description & Examples
### Goal
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum candies you must give.

### Function Contract
**Inputs**

- `ratings`: List[int]

**Return value**

int - minimum candies to distribute

### Examples
**Example 1**

- Input: `ratings = [1, 0, 2]`
- Output: `5`

**Example 2**

- Input: `ratings = [6, 0]`
- Output: `3`

**Example 3**

- Input: `ratings = [9]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
