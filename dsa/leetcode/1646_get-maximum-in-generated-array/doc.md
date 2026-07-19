# Get Maximum in Generated Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1646 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-maximum-in-generated-array/) |

## Problem Description
### Goal
Given an integer `n`, generate a 0-indexed array `nums` of length `n + 1`. Set `nums[0] = 0`, and set `nums[1] = 1` when that index exists.

For every valid generated index, an even index `2 * i` receives `nums[i]`, while an odd index `2 * i + 1` receives `nums[i] + nums[i + 1]`. Return the maximum value anywhere in the completed array.

### Function Contract
**Inputs**

- `n`: the final generated index, where $0 \le n \le 100$.

**Return value**

Return the maximum among `nums[0]` through `nums[n]` after applying the recurrence to every valid index.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `3`

The generated array is `[0,1,1,2,1,3,2,3]`.

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 3`
- Output: `2`
