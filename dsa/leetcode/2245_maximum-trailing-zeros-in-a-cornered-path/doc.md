# Maximum Trailing Zeros in a Cornered Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2245 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-trailing-zeros-in-a-cornered-path](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/).

### Goal
Choose a grid path that moves horizontally and vertically without revisiting cells and makes at most one right-angle turn. Maximize the number of trailing zeros in the product of values along the path.

### Function Contract
**Inputs**

- `grid`: a matrix of positive integers.

**Return value**

The maximum trailing-zero count over all valid cornered paths.

### Examples
**Example 1**

- Input: `grid = [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]`
- Output: `3`

**Example 2**

- Input: `grid = [[4, 3, 2], [7, 6, 1], [8, 8, 8]]`
- Output: `0`

**Example 3**

- Input: `grid = [[10, 20], [25, 4]]`
- Output: `3`

---

## Solution
### Approach
Trailing zeros equal `min(total factors of 2, total factors of 5)`. Factor each cell and build row and column prefix sums for both primes. At every cell as the corner, evaluate the four combinations of one horizontal arm and one vertical arm, subtracting the corner once because both arm sums include it. Maximize the smaller prime-factor total.

### Complexity Analysis
- **Time Complexity**: `O(mn log V)`, including factor counting for maximum cell value `V`
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
