# Maximum Difference Between Increasing Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2016 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-difference-between-increasing-elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-difference-between-increasing-elements/).

### Goal
Find the largest positive difference `nums[j] - nums[i]` with `i < j`.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the maximum positive difference, or `-1` if no increasing pair exists.

### Examples
**Example 1**

- Input: `nums = [7,1,5,4]`
- Output: `4`

**Example 2**

- Input: `nums = [9,4,3,2]`
- Output: `-1`

**Example 3**

- Input: `nums = [1,5,2,10]`
- Output: `9`

---

## Solution
### Approach
Scan left to right while tracking the smallest value seen so far. Each current value can form a candidate difference against that minimum, then the minimum is updated.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
