# Image Overlap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 835 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/image-overlap/) |

## Problem Description
### Goal
Two images, `img1` and `img2`, are represented by binary square matrices of size `n` by `n`. A translation slides all `1` bits of one image together by any number of units left, right, up, and/or down before that image is placed over the other. The overlap is the number of positions containing `1` in both images.

Translation never rotates an image. Any `1` bit moved beyond a matrix border disappears. Choose any translation of either image and return the largest overlap that can be obtained.

### Function Contract
**Inputs**

- `img1`: an `n` by `n` matrix containing only `0` and `1`.
- `img2`: another binary `n` by `n` matrix.
- Both images have the same side length, with $1 \leq n \leq 30$.

**Return value**

Return the maximum number of aligned positions at which both images contain `1` after translating one image without rotation.

### Examples
**Example 1**

- Input: `img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]`
- Output: `3`

Moving `img1` one unit right and one unit down aligns three of its `1` bits with `1` bits in `img2`.

**Example 2**

- Input: `img1 = [[1]], img2 = [[1]]`
- Output: `1`

**Example 3**

- Input: `img1 = [[0]], img2 = [[0]]`
- Output: `0`
