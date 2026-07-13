# Maximal Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 221 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-square/) |

## Problem Description
### Goal
Given a nonempty rectangular matrix whose entries are the characters `"0"` and `"1"`, find an axis-aligned square submatrix in which every cell is `"1"`. The square must occupy consecutive rows and columns and have equal height and width.

Return the area of the largest such square, not its side length or coordinates. A single `"1"` forms an area-one square, while an all-zero matrix returns `0`. When several largest squares exist, their shared area is sufficient. Rectangular all-one regions whose shorter dimension limits the square contribute only the area of their largest square portion.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular matrix of `"0"` and `"1"`

**Return value**

The largest all-one square's area.

### Examples
**Example 1**

- A matrix containing a two-by-two all-one region
- Output: `4`

**Example 2**

- Input: `[["0","1"],["1","0"]]`
- Output: `1`

**Example 3**

- Input: `[["0"]]`
- Output: `0`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Describe a square by its bottom-right corner. Let the state at `(row, column)` be the side length of the largest all-one square ending there. A zero cell cannot end such a square, so its state is zero. For a one cell, extending to side length `q` requires side length at least $q - 1$ immediately above, immediately left, and diagonally above-left. The limiting neighbor determines the extension:

`state = 1 + min(above, left, diagonal)`.

The diagonal term is essential. Above and left may each support long strips while the interior corner contains a zero; without the diagonal constraint, those strips would be mistaken for a filled square.

For a one-cell whose three neighboring states are `2`, `3`, and `2`, the largest ending square has side `3`. The two size-two squares plus the current row and column certify the complete three-by-three region, while the minimum prevents claiming a fourth layer unsupported by every direction.

**Compressing the table to one row**

Process the matrix row by row and keep `dp[column]`. Before updating a position, that entry is the state from above; `dp[column - 1]` is already the current row's left state. Preserve the old previous-column value in a separate `diagonal` variable before it is overwritten. A leading zero sentinel removes first-row and first-column branches.

After each update, the stored value is exactly the largest square ending at that cell: any larger square would require all three neighboring states to be larger, while the minimum-sized neighbor squares together with the current one-cell construct the claimed square. Track the maximum side encountered and square it only at the end because the requested result is area.

#### Complexity detail

Every one of the $m \cdot n$ cells is processed once, giving $O(mn)$ time. A DP row of $n + 1$ integers plus constant state uses $O(n)$ space; choosing the shorter matrix dimension for compression can reduce this to $O(\min(m,n))$ when traversal is adapted.

#### Alternatives and edge cases

- A full two-dimensional DP table is easier to inspect but uses $O(mn)$ space.
- Expanding a candidate square from every cell can repeatedly inspect the same area and become cubic or worse.
- Histogram/stack logic for maximal rectangles solves a different shape constraint and is unnecessary here.
- An all-zero matrix returns zero; one isolated `"1"` yields area one.
- A full square of side `q` yields $q^{2}$, not side length `q`.

</details>
