# Partition Array Into Two Arrays to Minimize Sum Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2035 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Dynamic Programming, Bit Manipulation, Sorting, Ordered Set, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [partition-array-into-two-arrays-to-minimize-sum-difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/).

### Goal
Split `2n` numbers into two groups of `n` numbers so the absolute difference of their sums is as small as possible.

### Function Contract
**Inputs**

- `nums`: an array with even length.

**Return value**

Return the minimum possible absolute sum difference.

### Examples
**Example 1**

- Input: `nums = [3,9,7,3]`
- Output: `2`

**Example 2**

- Input: `nums = [-36,36]`
- Output: `72`

**Example 3**

- Input: `nums = [2,-1,0,4,-2,-9]`
- Output: `0`

---

## Solution
### Approach
Use meet-in-the-middle. Generate subset sums for each half grouped by how many elements are chosen. For each left choice count and sum, binary-search the compatible right sums to get as close as possible to half of the total.

### Complexity Analysis
- **Time Complexity**: `O(n * 2^n)` for half-size `n`, plus sorting grouped sums.
- **Space Complexity**: `O(2^n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
