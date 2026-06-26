# Max Number of K-Sum Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1679 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Official Link | [max-number-of-k-sum-pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) |

## Problem Description & Examples
### Goal
Remove as many disjoint pairs as possible from an array where each removed pair must sum to `k`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the target pair sum.

**Return value**

Return the maximum number of valid pair removals.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4], k = 5`
- Output: `2`

**Example 2**

- Input: `nums = [3,1,3,4,3], k = 6`
- Output: `1`

**Example 3**

- Input: `nums = [2,2,2,3,1,1,4], k = 4`
- Output: `2`

---

## Underlying Base Algorithm(s)
Count frequencies as the array is scanned. For each value, first try to consume a previously seen complement `k - value`; if one exists, form a pair. Otherwise store the current value for a future complement.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
