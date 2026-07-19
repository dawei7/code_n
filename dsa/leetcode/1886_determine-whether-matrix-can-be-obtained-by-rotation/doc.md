# Determine Whether Matrix Can Be Obtained By Rotation

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/) |
| Frontend ID | 1886 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You receive two binary square matrices, `mat` and `target`, with the same dimensions. A legal operation rotates all of `mat` clockwise by exactly $90^\circ$ while preserving its square shape and every cell value.

Determine whether applying this operation zero, one, two, or three times can make `mat` identical to `target`. Four rotations return to the starting orientation, so no other distinct result is possible. Equality requires every corresponding cell to match; values cannot be flipped or rearranged in any other way.

### Function Contract

**Inputs**

- `mat`: an $N\times N$ matrix containing only `0` and `1`.
- `target`: another $N\times N$ binary matrix.
- $1 \le N \le 10$.

**Return value**

- Return `True` if one of the four quarter-turn orientations of `mat` equals `target`; otherwise return `False`.

### Examples

**Example 1**

- Input: `mat = [[0,1],[1,0]], target = [[1,0],[0,1]]`
- Output: `True`

One clockwise quarter-turn produces the target.

**Example 2**

- Input: `mat = [[0,1],[1,1]], target = [[1,0],[0,1]]`
- Output: `False`

None of the four orientations has the same cells as `target`.

**Example 3**

- Input: `mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]`
- Output: `True`

Two clockwise quarter-turns, or one $180^\circ$ rotation, produce the target.

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent the four possible orientations**

Keep four Boolean possibilities, conveniently as four bits. For target coordinate `(row, column)`, the corresponding source values under rotations of $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$ are respectively:

- `mat[row][column]`
- `mat[N - 1 - column][row]`
- `mat[N - 1 - row][N - 1 - column]`
- `mat[column][N - 1 - row]`

**Eliminate impossible rotations**

Visit every target cell once. Compare it with each of those four source coordinates and clear an orientation's bit when its value differs. A cleared orientation can never recover, because full matrix equality requires every coordinate to match. If all four bits are cleared, return `False` immediately.

**Why a remaining bit is sufficient**

Each orientation bit survives exactly when every visited target coordinate matches the source coordinate mapped to it by that rotation. After all $N^2$ coordinates have been visited, any surviving bit therefore certifies equality of the complete matrices under its rotation. Conversely, every invalid rotation has at least one mismatching coordinate and is cleared there.

#### Complexity detail

There are $N^2$ cells and four constant-time comparisons per cell, giving $O(N^2)$ time. The four-bit mask and loop indices occupy $O(1)$ auxiliary space; no rotated matrix is constructed.

#### Alternatives and edge cases

- **Build each rotated matrix:** Transposing and reversing rows is straightforward and still takes $O(N^2)$ time, but materializing a rotation uses $O(N^2)$ extra space.
- **Rotate in place:** Layer-by-layer swaps use $O(1)$ extra space but mutate `mat`, which is unnecessary for a Boolean comparison.
- **Zero rotations:** An already equal matrix must return `True`.
- **One-cell matrix:** Rotation changes nothing, so the two values alone determine the result.
- **Symmetric matrices:** Multiple orientation bits may survive; only one is required.
- **Different cell counts:** Rotation preserves the number of zeros and ones, so unequal counts guarantee `False`, though a separate count pass is not needed.

</details>
