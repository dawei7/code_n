# Campus Bikes II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1066 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [campus-bikes-ii](https://leetcode.com/problems/campus-bikes-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/campus-bikes-ii/).

### Goal
Assign a distinct bike to each worker so that the total Manhattan distance between workers and their assigned bikes is minimized.

### Function Contract
**Inputs**

- `workers`: List of worker coordinates `[x, y]`.
- `bikes`: List of bike coordinates `[x, y]`.

**Return value**

Minimum possible total Manhattan distance.

### Examples
**Example 1**

- Input: `workers = [[0, 0], [2, 1]], bikes = [[1, 2], [3, 3]]`
- Output: `6`

**Example 2**

- Input: `workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]]`
- Output: `4`

**Example 3**

- Input: `workers = [[0, 0]], bikes = [[5, 5]]`
- Output: `10`

---

## Solution
### Approach
Use dynamic programming over a bitmask of assigned bikes. Let `dp(i, mask)` be the minimum additional distance after assigning bikes to workers `0..i-1`, where `mask` marks bikes already used. Try assigning every unused bike to worker `i` and recurse.

Memoization prevents recomputing the same `(i, mask)` state. Since `i` is determined by the number of bits in `mask`, the mask alone can also identify the state.

### Complexity Analysis
- **Time Complexity**: `O(w * 2^b * b)` in a direct formulation, where `w` is workers and `b` is bikes.
- **Space Complexity**: `O(2^b)` for memoized states.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
