# Find the Most Competitive Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1673 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-most-competitive-subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-most-competitive-subsequence/).

### Goal
Choose a subsequence of length `k` whose lexicographic order is as small as possible while preserving the original relative order of chosen elements.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the required subsequence length.

**Return value**

Return the most competitive subsequence of length `k`.

### Examples
**Example 1**

- Input: `nums = [3,5,2,6], k = 2`
- Output: `[2,6]`

**Example 2**

- Input: `nums = [2,4,3,3,5,4,9,6], k = 4`
- Output: `[2,3,3,4]`

**Example 3**

- Input: `nums = [9,1,2,5,8,3], k = 3`
- Output: `[1,2,3]`

---

## Solution
### Approach
Use a monotonic stack. While the current number is smaller than the stack top and enough elements remain to still build length `k`, pop the larger top. Push the current value when the stack still needs more elements. This greedily fixes each position to the smallest feasible value.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(k)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
