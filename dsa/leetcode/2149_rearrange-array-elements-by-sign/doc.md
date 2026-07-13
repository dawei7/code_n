# Rearrange Array Elements by Sign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2149 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [rearrange-array-elements-by-sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/rearrange-array-elements-by-sign/).

### Goal
Rearrange an equal number of positive and negative integers so signs alternate, starting with a positive value. Preserve the original relative order among positive values and among negative values.

### Function Contract
**Inputs**

- `nums`: a nonzero integer array containing equally many positive and negative values.

**Return value**

The rearranged array with positive values at even indices and negative values at odd indices.

### Examples
**Example 1**

- Input: `nums = [3, 1, -2, -5, 2, -4]`
- Output: `[3, -2, 1, -5, 2, -4]`

**Example 2**

- Input: `nums = [-1, 1]`
- Output: `[1, -1]`

**Example 3**

- Input: `nums = [-3, 4, -2, 5]`
- Output: `[4, -3, 5, -2]`

---

## Solution
### Approach
Allocate the result and maintain the next even slot for positive values and next odd slot for negative values. Scan `nums` once, writing each value to its sign's next slot and advancing that slot by two. The single scan preserves both relative orders.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the returned arrangement

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
