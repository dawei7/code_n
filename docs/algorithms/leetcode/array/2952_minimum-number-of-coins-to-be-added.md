# Minimum Number of Coins to be Added

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2952 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-number-of-coins-to-be-added](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/) |

## Problem Description & Examples
### Goal
Given an array of integers representing available coin denominations and a target integer `target`, determine the minimum number of additional coins required to ensure that every integer value from 1 to `target` can be formed by summing a subset of the available coins.

### Function Contract
**Inputs**

- `coins`: A list of integers representing the denominations of the coins currently available.
- `target`: An integer representing the upper bound of the range [1, target] that must be representable.

**Return value**

- An integer representing the minimum count of coins that must be added to the collection.

### Examples
**Example 1**

- Input: `coins = [1, 4, 10], target = 19`
- Output: `2`

**Example 2**

- Input: `coins = [1, 4, 10, 5, 7, 19], target = 19`
- Output: `1`

**Example 3**

- Input: `coins = [1, 1, 1], target = 20`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. We maintain a variable `reachable`, representing the maximum value such that all integers in the range `[1, reachable]` can be formed. Initially, `reachable = 0`. We sort the coins and iterate through them. If the current coin `c` is less than or equal to `reachable + 1`, we can extend our range to `reachable + c`. If `c > reachable + 1`, we have a gap, and we must add a coin of value `reachable + 1` to bridge it, incrementing our count and updating `reachable` accordingly.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` where `N` is the number of coins, primarily due to the sorting step. The subsequent linear scan takes `O(N + log(target))` time.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.
