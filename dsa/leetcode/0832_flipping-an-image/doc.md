# Flipping an Image

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 832 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Bit Manipulation, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flipping-an-image/) |

## Problem Description

### Goal

You are given an $n \times n$ binary matrix `image`. First flip the image horizontally, which means reversing the order of the entries within every row while leaving the row order unchanged.

Then invert the flipped image: replace every `0` with `1` and every `1` with `0`. Return the matrix after both operations have been applied in that order, with the same dimensions as the input.

### Function Contract

**Inputs**

- `image`: an $n \times n$ matrix containing only `0` and `1`, where $1 \le n \le 20$

**Return value**

- The binary matrix obtained by reversing each row and then inverting every entry

### Examples

**Example 1**

- Input: `image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]`
- Output: `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]`
- Explanation: Reversing the rows produces `[[0, 1, 1], [1, 0, 1], [0, 0, 0]]`; inverting those bits gives the output.

**Example 2**

- Input: `image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]`
- Output: `[[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]`

**Example 3**

- Input: `image = [[0]]`
- Output: `[[1]]`
- Explanation: Reversal leaves the one-cell row in place, and inversion changes its bit.
