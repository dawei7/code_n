# Minimum Operations to Reduce X to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1658 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-reduce-x-to-zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/).

### Goal
Remove values from either end of the array until the removed sum equals `x`.
Minimize the number of removals.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `x`: the target removed sum.

**Return value**

The minimum number of end removals, or `-1` if impossible.

### Examples
**Example 1**

- Input: `nums = [1, 1, 4, 2, 3], x = 5`
- Output: `2`

**Example 2**

- Input: `nums = [5, 6, 7, 8, 9], x = 4`
- Output: `-1`

**Example 3**

- Input: `nums = [3, 2, 20, 1, 1, 3], x = 10`
- Output: `5`

---

## Solution
### Approach
Instead of choosing removed ends directly, keep the longest middle subarray with
sum `sum(nums) - x`. With positive values, find that longest subarray using a
sliding window; the answer is total length minus the kept length.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
