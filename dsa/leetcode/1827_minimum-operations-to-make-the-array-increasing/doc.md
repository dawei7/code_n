# Minimum Operations to Make the Array Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1827 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-the-array-increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/).

### Goal
Increase array elements by `1` any number of times so the array becomes strictly increasing. Minimize the number of increments.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the minimum number of increment operations.

### Examples
**Example 1**

- Input: `nums = [1,1,1]`
- Output: `3`

**Example 2**

- Input: `nums = [1,5,2,4,1]`
- Output: `14`

**Example 3**

- Input: `nums = [8]`
- Output: `0`

---

## Solution
### Approach
Scan left to right. Track the minimum value the current element must have, one more than the previous adjusted value. If `nums[i]` is too small, add the difference to the answer and treat the adjusted value as the required minimum.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
