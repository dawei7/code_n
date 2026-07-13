# Smallest Index With Equal Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2057 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-index-with-equal-value](https://leetcode.com/problems/smallest-index-with-equal-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-index-with-equal-value/).

### Goal
Find the first index whose index modulo `10` equals the value stored there.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the smallest valid index, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [0,1,2]`
- Output: `0`

**Example 2**

- Input: `nums = [4,3,2,1]`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3,4,5,6,7,8,9,0]`
- Output: `-1`

---

## Solution
### Approach
Scan from left to right and return the first index `i` satisfying `i % 10 == nums[i]`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
