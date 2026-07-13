# Find the Longest Valid Obstacle Course at Each Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1964 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Binary Indexed Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-longest-valid-obstacle-course-at-each-position](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/).

### Goal
For every position, find the length of the longest non-decreasing subsequence that ends exactly at that obstacle.

### Function Contract
**Inputs**

- `obstacles`: obstacle heights in order.

**Return value**

Return an array of lengths, one per position.

### Examples
**Example 1**

- Input: `obstacles = [1,2,3,2]`
- Output: `[1,2,3,3]`

**Example 2**

- Input: `obstacles = [2,2,1]`
- Output: `[1,2,1]`

**Example 3**

- Input: `obstacles = [3,1,5,6,4,2]`
- Output: `[1,1,2,3,2,2]`

---

## Solution
### Approach
Use the patience-sorting tails array for a longest non-decreasing subsequence. For each height, binary-search the first tail greater than it (`bisect_right`); that position plus one is the answer, and the tail is updated to the current height.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
