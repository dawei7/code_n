# Build Array from Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1920 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [build-array-from-permutation](https://leetcode.com/problems/build-array-from-permutation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/build-array-from-permutation/).

### Goal
Given a zero-indexed permutation, build a new array where `answer[i] = nums[nums[i]]`.

### Function Contract
**Inputs**

- `nums`: a zero-indexed permutation of `0..n-1`.

**Return value**

Return the constructed array.

### Examples
**Example 1**

- Input: `nums = [0,2,1,5,3,4]`
- Output: `[0,1,2,4,5,3]`

**Example 2**

- Input: `nums = [5,0,1,2,3,4]`
- Output: `[4,5,0,1,2,3]`

**Example 3**

- Input: `nums = [0]`
- Output: `[0]`

---

## Solution
### Approach
Create a result array and assign `result[i] = nums[nums[i]]` for every index. An in-place encoding is possible because values are in `0..n-1`, but the straightforward output array is clearest.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output array

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
