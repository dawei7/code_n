# Maximum Element After Decreasing and Rearranging

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1846 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-element-after-decreasing-and-rearranging](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/).

### Goal
Rearrange the array and decrease elements as needed so the first value is `1` and adjacent values differ by at most `1`. Maximize the largest final element.

### Function Contract
**Inputs**

- `arr`: a list of positive integers.

**Return value**

Return the maximum possible value of the largest element after valid changes.

### Examples
**Example 1**

- Input: `arr = [2,2,1,2,1]`
- Output: `2`

**Example 2**

- Input: `arr = [100,1,1000]`
- Output: `3`

**Example 3**

- Input: `arr = [1,2,3,4,5]`
- Output: `5`

---

## Solution
### Approach
Sort the array. Greedily build the smallest valid sequence that lets the maximum grow as much as possible: start the first adjusted value at `1`, and each next adjusted value can be at most previous plus one and at most its original sorted value.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
