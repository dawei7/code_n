# Search a 2D Matrix II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 240 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Problem Description
### Goal
Given a rectangular integer matrix, every row is sorted from left to right in ascending order and every column is sorted from top to bottom in ascending order. Determine whether any cell contains the integer `target`.

Return `True` when at least one occurrence exists and `False` otherwise. Duplicate matrix values are allowed, and only one match is needed. Use both sorting directions to avoid an exhaustive scan under the required complexity. The target may lie outside the matrix's total value range, and an empty matrix representation contains no matching cell.

### Function Contract
**Inputs**

- `matrix`: a rectangular integer matrix sorted left-to-right and top-to-bottom
- `target`: the integer to locate

**Return value**

`True` if any matrix cell equals `target`; otherwise `False`.

### Examples
**Example 1**

- Input: `matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5`
- Output: `True`

**Example 2**

- Input: `matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 10`
- Output: `False`

**Example 3**

- Input: `matrix = [[-5]], target = -5`
- Output: `True`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Start where one comparison eliminates a row or column**

Begin at the top-right cell. A larger value proves the entire current column is too large, so move left. A smaller value proves the entire current row is too small, so move down.

Before each comparison, every still-possible target cell lies in the submatrix from the current row downward and from column zero through the current column.

Sorted columns justify discarding a column when its top remaining value is too large; sorted rows justify discarding a row when its rightmost remaining value is too small. These moves never discard a possible match, and finding equality returns true. Leaving the matrix means all rows or columns have been safely eliminated.

At the top-right boundary of the remaining submatrix, a value greater than the target rules out its entire column because every lower value is at least as large. A value below the target rules out its entire row because every value to the left is no larger. Equality succeeds immediately; leaving the matrix means these safe eliminations exhausted all candidates.

#### Complexity detail

Each step moves left or down, with at most `n` left moves and `m` down moves, for $O(m+n)$ time and constant space.

#### Alternatives and edge cases

- **Search every cell:** costs $O(mn)$.
- **Binary-search every row:** costs $O(m \log n)$.
- Empty matrices return false; one row, one column, duplicates, and negative values preserve the same invariant.

</details>
