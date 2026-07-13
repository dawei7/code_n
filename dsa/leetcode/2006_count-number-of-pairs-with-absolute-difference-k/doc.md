# Count Number of Pairs With Absolute Difference K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2006 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-pairs-with-absolute-difference-k](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/).

### Goal
Count index pairs whose values differ by exactly `k`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: required absolute difference.

**Return value**

Return the number of pairs `i < j` with `abs(nums[i] - nums[j]) == k`.

### Examples
**Example 1**

- Input: `nums = [1,2,2,1], k = 1`
- Output: `4`

**Example 2**

- Input: `nums = [1,3], k = 3`
- Output: `0`

**Example 3**

- Input: `nums = [3,2,1,5,4], k = 2`
- Output: `3`

---

## Solution
### Approach
Scan numbers while counting previously seen values. For each `x`, add counts of `x - k` and `x + k`, then record `x`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
