# Maximum Number of Coins You Can Get

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1561 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting, Game Theory |
| Official Link | [maximum-number-of-coins-you-can-get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) |

## Problem Description & Examples
### Goal
Split piles into groups of three where Alice takes the largest pile, you take
the second-largest pile, and Bob takes the smallest pile. Maximize your total
coins.

### Function Contract
**Inputs**

- `piles`: an array of pile sizes, with length divisible by three.

**Return value**

The maximum number of coins you can collect.

### Examples
**Example 1**

- Input: `piles = [2, 4, 1, 2, 7, 8]`
- Output: `9`

**Example 2**

- Input: `piles = [2, 4, 5]`
- Output: `4`

**Example 3**

- Input: `piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]`
- Output: `18`

---

## Underlying Base Algorithm(s)
Sort the piles. Bob can be assigned the smallest third of piles, while Alice and
you split the remaining larger piles in pairs. Starting from the second-largest
remaining pile, take every other pile exactly `n / 3` times.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.
