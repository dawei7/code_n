# Minimum Operations to Make a Uni-Value Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2033 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-a-uni-value-grid](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/).

### Goal
Each operation adds or subtracts `x` from one cell. Make all grid values equal using the fewest operations.

### Function Contract
**Inputs**

- `grid`: an integer matrix.
- `x`: operation step size.

**Return value**

Return the minimum operation count, or `-1` if no common value is reachable.

### Examples
**Example 1**

- Input: `grid = [[2,4],[6,8]], x = 2`
- Output: `4`

**Example 2**

- Input: `grid = [[1,5],[2,3]], x = 1`
- Output: `5`

**Example 3**

- Input: `grid = [[1,2],[3,4]], x = 2`
- Output: `-1`

---

## Solution
### Approach
All values must share the same remainder modulo `x`. If so, flatten and sort the values; the median minimizes total absolute distance. Sum `abs(value - median) / x`.

### Complexity Analysis
- **Time Complexity**: `O(mn log(mn))`
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
