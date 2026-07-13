# Closest Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1755 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Bit Manipulation, Sorting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [closest-subsequence-sum](https://leetcode.com/problems/closest-subsequence-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/closest-subsequence-sum/).

### Goal
Choose any subsequence of `nums` and compare its sum with `goal`. Minimize the absolute difference between the subsequence sum and `goal`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `goal`: the target sum.

**Return value**

Return the smallest possible absolute difference.

### Examples
**Example 1**

- Input: `nums = [5,-7,3,5], goal = 6`
- Output: `0`

**Example 2**

- Input: `nums = [7,-9,15,-2], goal = -5`
- Output: `1`

**Example 3**

- Input: `nums = [1,2,3], goal = -7`
- Output: `7`

---

## Solution
### Approach
Use meet-in-the-middle. Split `nums` into two halves, enumerate all subset sums of each half, sort one list, and for every sum from the other half binary search for the closest complement to `goal`.

### Complexity Analysis
- **Time Complexity**: `O(2^(n/2) log 2^(n/2))`
- **Space Complexity**: `O(2^(n/2))`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
