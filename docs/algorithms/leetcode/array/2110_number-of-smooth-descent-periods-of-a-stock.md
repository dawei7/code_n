# Number of Smooth Descent Periods of a Stock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2110 |
| Difficulty | Medium |
| Topics | Array, Math, Two Pointers, Dynamic Programming, Sliding Window |
| Official Link | [number-of-smooth-descent-periods-of-a-stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) |

## Problem Description & Examples
### Goal
Count contiguous periods where each price after the first is exactly one less than the previous price. Single-day periods also count.

### Function Contract
**Inputs**

- `prices`: stock prices by day.

**Return value**

Return the total number of smooth descent periods.

### Examples
**Example 1**

- Input: `prices = [3,2,1,4]`
- Output: `7`

**Example 2**

- Input: `prices = [8,6,7,7]`
- Output: `4`

**Example 3**

- Input: `prices = [1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Track the length of the smooth descent run ending at each position. Extend it when `prices[i - 1] - prices[i] == 1`; otherwise reset to one. Add each ending-run length to the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
