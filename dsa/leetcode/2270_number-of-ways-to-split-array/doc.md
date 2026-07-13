# Number of Ways to Split Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2270 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-to-split-array](https://leetcode.com/problems/number-of-ways-to-split-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-to-split-array/).

### Goal
Count split positions that leave both sides nonempty and give the left side a sum greater than or equal to the right side's sum.

### Function Contract
**Inputs**

- `nums`: an integer array of length at least two.

**Return value**

The number of valid split indices.

### Examples
**Example 1**

- Input: `nums = [10, 4, -8, 7]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 3, 1, 0]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 1]`
- Output: `1`

---

## Solution
### Approach
Compute the total sum, then scan through the penultimate element while maintaining the left prefix sum. The right sum is `total - left`; increment the answer whenever `left >= right`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
