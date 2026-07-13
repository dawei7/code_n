# Get Biggest Three Rhombus Sums in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1878 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [get-biggest-three-rhombus-sums-in-a-grid](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/).

### Goal
Compute border sums of all rhombus shapes in a grid and return the three largest distinct sums, or fewer if fewer than three exist.

### Function Contract
**Inputs**

- `grid`: a 2D integer matrix.

**Return value**

Return up to three distinct rhombus border sums in descending order.

### Examples
**Example 1**

- Input: `grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]`
- Output: `[228,216,211]`

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[20,9,8]`

**Example 3**

- Input: `grid = [[7,7,7]]`
- Output: `[7]`

---

## Solution
### Approach
Every single cell is a rhombus of size zero. For larger rhombi, choose a top cell and side length, ensure all four corners fit, and sum the four diagonal edges. Diagonal prefix sums can compute each edge quickly; a small set or min-heap keeps the largest three distinct values.

### Complexity Analysis
- **Time Complexity**: `O(m * n * min(m, n))`
- **Space Complexity**: `O(m * n)` with diagonal prefixes, or `O(1)` for the top-three set aside from input

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
