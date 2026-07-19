# Number of Pairs of Interchangeable Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2001 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/) |

## Problem Description

### Goal

An array `rectangles` describes $N$ rectangles. Entry `rectangles[i] = [width_i, height_i]` gives the positive width and height of rectangle $i$.

Two distinct rectangles at indices $i<j$ are interchangeable when their width-to-height ratios are equal:

$$
\frac{\textit{width}_i}{\textit{height}_i}
=
\frac{\textit{width}_j}{\textit{height}_j}.
$$

Count all index pairs that satisfy this equality. Equal dimensions at different indices still represent different rectangles and therefore form distinct pairs.

### Function Contract

**Inputs**

- `rectangles`: an array of $N$ pairs, where $1 \le N \le 10^5$.
- Every width and height lies between $1$ and $10^5$ inclusive.
- Let $M$ be the largest supplied dimension.

**Return value**

Return the number of index pairs $(i,j)$ with $i<j$ whose rectangles have the same width-to-height ratio.

### Examples

**Example 1**

- Input: `rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]`
- Output: `6`
- Explanation: All four ratios reduce to $1/2$, so every pair is interchangeable.

**Example 2**

- Input: `rectangles = [[4, 5], [7, 8]]`
- Output: `0`
- Explanation: The two ratios differ.

**Example 3**

- Input: `rectangles = [[1, 2], [2, 4], [3, 6], [4, 7]]`
- Output: `3`
- Explanation: The first three rectangles share ratio $1/2$ and create three pairs; the last rectangle has a different ratio.
