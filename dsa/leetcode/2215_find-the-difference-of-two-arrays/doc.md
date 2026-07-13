# Find the Difference of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2215 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-difference-of-two-arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-difference-of-two-arrays/).

### Goal
Return the distinct values appearing only in the first array and the distinct values appearing only in the second array.

### Function Contract
**Inputs**

- `nums1`: the first integer array.
- `nums2`: the second integer array.

**Return value**

`[only_in_nums1, only_in_nums2]`; values within either list may be in any order.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 3]`, `nums2 = [2, 4, 6]`
- Output: `[[1, 3], [4, 6]]`

**Example 2**

- Input: `nums1 = [1, 2, 3, 3]`, `nums2 = [1, 1, 2, 2]`
- Output: `[[3], []]`

**Example 3**

- Input: `nums1 = [5, 5]`, `nums2 = [5]`
- Output: `[[], []]`

---

## Solution
### Approach
Convert each array to a set. Compute the two directional set differences, `set1 - set2` and `set2 - set1`, and return them as lists.

### Complexity Analysis
- **Time Complexity**: `O(n + m)` expected
- **Space Complexity**: `O(n + m)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
