# Count Subarrays With Score Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2302 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-subarrays-with-score-less-than-k](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/).

### Goal
Count nonempty contiguous subarrays whose score, defined as their sum multiplied by their length, is strictly less than `k`.

### Function Contract
**Inputs**

- `nums`: a positive integer array.
- `k`: the exclusive score limit.

**Return value**

The number of qualifying subarrays.

### Examples
**Example 1**

- Input: `nums = [2, 1, 4, 3, 5]`, `k = 10`
- Output: `6`

**Example 2**

- Input: `nums = [1, 1, 1]`, `k = 5`
- Output: `5`

**Example 3**

- Input: `nums = [1, 2]`, `k = 1`
- Output: `0`

---

## Solution
### Approach
Use a sliding window because all values are positive. Extend the right edge and add its value. While `window_sum * window_length >= k`, move the left edge forward. Every suffix of the remaining window ending at the current right edge is valid, contributing its length to the answer.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
