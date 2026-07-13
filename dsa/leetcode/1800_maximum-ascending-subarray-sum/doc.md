# Maximum Ascending Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1800 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-ascending-subarray-sum](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-ascending-subarray-sum/).

### Goal
Find the maximum sum among contiguous subarrays whose values are strictly increasing from left to right.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the largest sum of any strictly ascending subarray.

### Examples
**Example 1**

- Input: `nums = [10,20,30,5,10,50]`
- Output: `65`

**Example 2**

- Input: `nums = [10,20,30,40,50]`
- Output: `150`

**Example 3**

- Input: `nums = [12,17,15,13,10,11,12]`
- Output: `33`

---

## Solution
### Approach
Scan once while maintaining the sum of the current strictly increasing run. If `nums[i] > nums[i - 1]`, extend the run; otherwise start a new run at `nums[i]`. Track the maximum run sum.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
