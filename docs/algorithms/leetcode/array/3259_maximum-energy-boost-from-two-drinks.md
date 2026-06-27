# Maximum Energy Boost From Two Drinks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3259 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-energy-boost-from-two-drinks](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/) |

## Problem Description & Examples
### Goal
Given two arrays representing energy boosts from two different drinks over a series of hours, determine the maximum total energy you can accumulate. You can consume one drink per hour, but switching drinks requires skipping the current hour (i.e., you cannot consume a drink in the hour immediately following a switch).

### Function Contract
**Inputs**

- `energyA`: A list of integers representing energy gains from drink A at each hour.
- `energyB`: A list of integers representing energy gains from drink B at each hour.

**Return value**

- An integer representing the maximum total energy boost achievable.

### Examples
**Example 1**

- Input: `energyA = [1, 3, 1], energyB = [3, 1, 1]`
- Output: `5`

**Example 2**

- Input: `energyA = [4, 1, 1], energyB = [1, 1, 3]`
- Output: `7`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain two state arrays (or variables) representing the maximum energy accumulated up to hour `i` ending with drink A or drink B. The transition depends on whether we continue the same drink (from `i-1`) or switch (from `i-2`).

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of hours, as we iterate through the arrays once.
- **Space Complexity**: `O(1)` if we optimize the DP state to only track the last two hours, or `O(n)` if using full DP tables.
