# Largest Magic Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1895 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-magic-square](https://leetcode.com/problems/largest-magic-square/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-magic-square/).

### Goal
Find the largest square subgrid where every row sum, every column sum, and both diagonal sums are equal.

### Function Contract
**Inputs**

- `grid`: a 2D integer matrix.

**Return value**

Return the side length of the largest magic square.

### Examples
**Example 1**

- Input: `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`
- Output: `3`

**Example 2**

- Input: `grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1]]`
- Output: `1`

---

## Solution
### Approach
Precompute row prefix sums, column prefix sums, and both diagonal prefix sums. Try square sizes from largest to smallest; for each top-left corner, compute the target diagonal sum and test all rows, columns, and the other diagonal in constant time per line. The first valid size found is the answer.

### Complexity Analysis
- **Time Complexity**: `O(min(m, n)^3 * max(m, n))` in direct checking with prefixes
- **Space Complexity**: `O(m * n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
