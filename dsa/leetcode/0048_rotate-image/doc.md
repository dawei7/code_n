# Rotate Image

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 48 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-image/) |

## Problem Description
### Goal
You are given a nonempty square $n \times n$ matrix representing an image. Rotate the image by exactly 90 degrees clockwise: an entry at row `r`, column `c` moves to row `c`, column $n - 1 - r$.

The native operation must modify the supplied matrix in place rather than allocating another $n \times n$ grid, and it returns no value. In cOde(n), `solve` returns that same mutated object so the resulting cell arrangement can be inspected. A $1 x 1$ image is unchanged.

### Function Contract
**Inputs**

- `matrix`: a nonempty square `List[List[int]]`

**Return value**

The rotated matrix. The app adapter returns the input object after mutating it; LeetCode's `rotate` method returns nothing.

### Examples
**Example 1**

- Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

**Example 2**

- Input: `matrix = [[1, 2], [3, 4]]`
- Output: `[[3, 1], [4, 2]]`

**Example 3**

- Input: `matrix = [[-1]]`
- Output: `[[-1]]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Decompose clockwise rotation into transpose plus row reversal**

A clockwise rotation can be expressed as two in-place transformations: transpose across the main diagonal, then reverse every row. Transposition sends the original cell `(row, column)` to `(column, row)`; reversing its new row sends it to `(column, n - 1 - row)`, exactly the clockwise destination.

**Visit each cross-diagonal pair exactly once**

Visit only cells strictly above the main diagonal, where `column > row`. When processing `(row, column)`, swap it with `(column, row)`. Visiting both triangular halves would swap every pair twice and undo the transpose. Diagonal cells map to themselves and require no operation.

**Trace both transformations**

Transposing `[[1,2,3],[4,5,6],[7,8,9]]` gives `[[1,4,7],[2,5,8],[3,6,9]]`. Reversing each row gives `[[7,4,1],[8,5,2],[9,6,3]]`.

**Correctness argument from coordinates**

For every original coordinate `(r, c)`, the transpose places its value at `(c, r)`. Row reversal then places it at $(c, n - 1 - r)$, the coordinate definition of a 90-degree clockwise rotation. Every coordinate is mapped once, so no value is lost or duplicated.

#### Complexity detail

The transpose visits $n(n - 1) / 2$ pairs and row reversal visits all $n^{2}$ cells, for $O(n^2)$ time. Swaps use constant temporary storage, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Build a second matrix:** is simple and has optimal $O(n^2)$ time, but violates the platform's $O(1)$ in-place requirement.
- **Rotate four cells per layer:** also achieves $O(n^2)$ time and $O(1)$ space, though its index arithmetic is less direct.
- **Repeatedly move rows and columns:** creates unnecessary copying and can become cubic depending on the data structure.
- A 1×1 matrix is unchanged by both operations. Odd-sized matrices keep the center cell fixed while all other cells move.
- The square shape is essential: transposition in place followed by row reversal does not represent the same operation for a rectangular matrix with different dimensions.

</details>
