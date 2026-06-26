# Frog Jump II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2498 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy |
| Official Link | [frog-jump-ii](https://leetcode.com/problems/frog-jump-ii/) |

## Problem Description & Examples
### Goal
A frog needs to travel from the first stone to the last stone and then return to the first stone. The frog must visit every stone exactly once during the round trip. The goal is to minimize the maximum jump distance (the "cost") encountered during the entire journey.

### Function Contract
**Inputs**

- `stones`: A strictly increasing list of integers representing the positions of stones on a 1D path.

**Return value**

- An integer representing the minimum possible value for the maximum jump distance across the entire round trip.

### Examples
**Example 1**

- Input: `stones = [0, 2, 5, 6, 7]`
- Output: `5`

**Example 2**

- Input: `stones = [0, 3, 9]`
- Output: `9`

---

## Underlying Base Algorithm(s)
The problem can be solved using a **Greedy** approach. By alternating stones between the forward and backward paths, we can ensure that the frog skips every other stone in each direction. The maximum jump distance will be the maximum of either the distance between adjacent stones (if we were forced to jump to the immediate next one) or the distance between stones separated by one index (e.g., `stones[i+2] - stones[i]`).

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of stones, as we iterate through the array once to calculate the gaps.
- **Space Complexity**: `O(1)`, as we only store the maximum jump value and do not require additional data structures proportional to the input size.
