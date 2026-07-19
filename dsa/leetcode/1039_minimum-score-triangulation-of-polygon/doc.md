# Minimum Score Triangulation of Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1039 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) |

## Problem Description

### Goal

A convex polygon has $N$ vertices, each carrying an integer value. The array `values` lists those vertex values in clockwise order.

Triangulate the polygon using only its original vertices and dividing it entirely into triangles; no other shapes are allowed. Every triangulation produces exactly $N-2$ triangles. The weight of a triangle is the product of its three vertex values, and a triangulation's score is the sum of all triangle weights.

Return the minimum score among every valid triangulation of the polygon.

### Function Contract

**Inputs**

- `values`: the clockwise values of the $N$ polygon vertices, where $3 \le N \le 50$ and $1 \le \texttt{values[i]} \le 100$.

**Return value**

- The minimum possible sum of triangle weights over a complete triangulation.

### Examples

**Example 1**

- Input: `values = [1,2,3]`
- Output: `6`
- Explanation: The polygon is already one triangle, whose weight is $1\cdot2\cdot3=6$.

**Example 2**

- Input: `values = [3,7,4,5]`
- Output: `144`
- Explanation: The better diagonal produces weights `3 * 4 * 5` and `3 * 4 * 7`, totaling `144`.

**Example 3**

- Input: `values = [1,3,1,4,1,5]`
- Output: `13`
