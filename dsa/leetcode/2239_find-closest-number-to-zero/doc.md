# Find Closest Number to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2239 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-closest-number-to-zero](https://leetcode.com/problems/find-closest-number-to-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-closest-number-to-zero/).

### Goal
Return the array value closest to zero. When a negative and positive value are equally close, choose the positive one.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array.

**Return value**

The value minimizing absolute magnitude, with the larger value breaking ties.

### Examples
**Example 1**

- Input: `nums = [-4, -2, 1, 4, 8]`
- Output: `1`

**Example 2**

- Input: `nums = [2, -1, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [0, 5, -5]`
- Output: `0`

---

## Solution
### Approach
Scan once while tracking the best value. Replace it when a candidate has smaller absolute value, or when the absolute values tie and the candidate itself is larger.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
