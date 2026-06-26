# Maximum Number of Consecutive Values You Can Make

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1798 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximum-number-of-consecutive-values-you-can-make](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/) |

## Problem Description & Examples
### Goal
Given coin values, find how many consecutive integer values starting from `0` can be formed using some subset of the coins.

### Function Contract
**Inputs**

- `coins`: a list of positive coin values.

**Return value**

Return the smallest non-formable value, which is also the count of consecutive values starting at `0`.

### Examples
**Example 1**

- Input: `coins = [1,3]`
- Output: `2`

**Example 2**

- Input: `coins = [1,1,1,4]`
- Output: `8`

**Example 3**

- Input: `coins = [1,4,10,3,1]`
- Output: `20`

---

## Underlying Base Algorithm(s)
Sort the coins and maintain `reachable`, the smallest value not yet formable. Initially only `0` is formable, so `reachable = 1`. If the next coin is greater than `reachable`, there is a gap. Otherwise it extends the formable range up to `reachable + coin - 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage
