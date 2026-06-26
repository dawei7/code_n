# Maximum Alternating Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1911 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-alternating-subsequence-sum](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) |

## Problem Description & Examples
### Goal
Choose a subsequence and assign alternating signs starting with plus. Maximize the resulting sum.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the maximum alternating subsequence sum.

### Examples
**Example 1**

- Input: `nums = [4,2,5,3]`
- Output: `7`

**Example 2**

- Input: `nums = [5,6,7,8]`
- Output: `8`

**Example 3**

- Input: `nums = [6,2,1,2,4,5]`
- Output: `10`

---

## Underlying Base Algorithm(s)
Use two DP states while scanning: `even` is the best sum after choosing an even number of elements, and `odd` is the best sum after choosing an odd number of elements. Taking a number from `even` adds it; taking from `odd` subtracts it. Update both states with either taking or skipping the current value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
