## Problem Description & Examples
### Goal
Given an integer array `nums`, return `True` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `False` otherwise.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

bool - True if partition exists

### Examples
**Example 1**

- Input: `nums = [1, 5, 11, 5]`
- Output: `True`

**Example 2**

- Input: `nums = [13, 14]`
- Output: `False`

**Example 3**

- Input: `nums = [5, 19]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
