# Frequency of the Most Frequent Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1838 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Official Link | [frequency-of-the-most-frequent-element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) |

## Problem Description & Examples
### Goal
You may increase elements by `1` at most `k` total times. Maximize the frequency of any value after those increments.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.
- `k`: the total increment budget.

**Return value**

Return the highest achievable frequency.

### Examples
**Example 1**

- Input: `nums = [1,2,4], k = 5`
- Output: `3`

**Example 2**

- Input: `nums = [1,4,8,13], k = 5`
- Output: `2`

**Example 3**

- Input: `nums = [3,9,6], k = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
Sort `nums` and use a sliding window ending at each target value. The cost to raise every value in the window to `nums[right]` is `nums[right] * window_size - window_sum`. Shrink the left side while this cost exceeds `k`, and track the largest window size.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage
