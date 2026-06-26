# Max Consecutive Ones III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1004 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [max-consecutive-ones-iii](https://leetcode.com/problems/max-consecutive-ones-iii/) |

## Problem Description & Examples
### Goal
Given a binary array and an allowance `k`, return the longest contiguous segment that can be made all `1`s by changing at most `k` zeroes.

### Function Contract
**Inputs**

- `nums`: List[int] containing only 0 and 1
- `k`: int maximum zeroes allowed in the window

**Return value**

int - maximum valid window length

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- Output: `6`

**Example 2**

- Input: `nums = [0, 0, 1, 1, 0, 1], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 1, 1], k = 0`
- Output: `3`

---

## Underlying Base Algorithm(s)
Sliding window with a zero counter.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
