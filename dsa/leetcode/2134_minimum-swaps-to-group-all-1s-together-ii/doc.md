# Minimum Swaps to Group All 1's Together II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2134 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-swaps-to-group-all-1s-together-ii](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/).

### Goal
Find the minimum number of swaps needed to place all `1` values in one contiguous block when the binary array is circular. A swap may exchange values at any two positions.

### Function Contract
**Inputs**

- `nums`: a circular binary array.

**Return value**

The minimum number of swaps required.

### Examples
**Example 1**

- Input: `nums = [0, 1, 0, 1, 1, 0, 0]`
- Output: `1`

**Example 2**

- Input: `nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 1, 0, 0, 1]`
- Output: `0`

---

## Solution
### Approach
Let `k` be the total number of ones. Any final block has length `k`, and the number of swaps it needs equals the zeros currently inside that block. Use a fixed-size sliding window across the circular array, represented by modular indexing or a doubled scan, and minimize the zero count among all `n` windows.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
