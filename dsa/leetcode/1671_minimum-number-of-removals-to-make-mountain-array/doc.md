# Minimum Number of Removals to Make Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1671 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-removals-to-make-mountain-array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/).

### Goal
Remove as few elements as possible so that the remaining sequence is a mountain array: strictly increasing to one peak and then strictly decreasing, with both sides non-empty.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the minimum number of removals needed to leave a valid mountain array.

### Examples
**Example 1**

- Input: `nums = [1,3,1]`
- Output: `0`

**Example 2**

- Input: `nums = [2,1,1,5,6,2,3,1]`
- Output: `3`

**Example 3**

- Input: `nums = [4,3,2,1,1,2,3,1]`
- Output: `4`

---

## Solution
### Approach
Compute the length of the longest strictly increasing subsequence ending at each index and the longest strictly decreasing subsequence starting at each index. Any index with both lengths greater than one can be the peak. The best mountain length is `left[i] + right[i] - 1`, so removals are `n - best`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` with patience sorting lengths
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
