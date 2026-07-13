# Find the Middle Index in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1991 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-middle-index-in-array](https://leetcode.com/problems/find-the-middle-index-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-middle-index-in-array/).

### Goal
Find the first index where the sum of elements to the left equals the sum of elements to the right.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the leftmost middle index, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [2,3,-1,8,4]`
- Output: `3`

**Example 2**

- Input: `nums = [1,-1,4]`
- Output: `2`

**Example 3**

- Input: `nums = [2,5]`
- Output: `-1`

---

## Solution
### Approach
Compute the total sum, then scan while maintaining the prefix sum before the current index. The right sum is `total - prefix - nums[i]`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
