# Smallest Rectangle Enclosing Black Pixels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 302 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) |

## Problem Description
### Goal
Given a nonempty binary image, `"1"` marks a black pixel and `"0"` marks a white pixel. All black pixels form one horizontally or vertically connected component, and coordinates `(x, y)` identify one known black pixel within it.

Find the tightest axis-aligned rectangle whose rows and columns contain every black pixel, then return its area. The rectangle's boundaries are the minimum and maximum occupied row and column, inclusive, even when white pixels lie inside that box. Do not return the perimeter or coordinates. Use the connected-image and known-pixel information to meet the required sublinear search behavior where applicable.

### Function Contract
**Inputs**

- `image`: a nonempty rectangular grid containing character `"0"` for white and `"1"` for black
- `x`: the row of a known black pixel
- `y`: the column of that pixel

**Return value**

The area of the tightest rectangle covering all black pixels.

### Examples
**Example 1**

- Input: `image = ["0010","0110","0100"], x = 0, y = 2`
- Output: `6`

**Example 2**

- Input: `image = ["1"], x = 0, y = 0`
- Output: `1`

**Example 3**

- Input: `image = ["01110"], x = 0, y = 2`
- Output: `3`
