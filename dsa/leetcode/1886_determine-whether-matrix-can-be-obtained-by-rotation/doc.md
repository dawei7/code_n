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
