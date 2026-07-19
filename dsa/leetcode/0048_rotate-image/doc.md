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
