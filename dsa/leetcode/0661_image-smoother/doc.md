# Image Smoother

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 661 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/image-smoother/) |

## Problem Description
### Goal
An image smoother applies a $3 x 3$ filter to each cell of a grayscale image. For a cell, average its own value with the values of all surrounding cells that actually exist, then round that average down to an integer.

Given an $m \times n$ integer matrix `img`, return a new image containing the smoothed value for every cell. At an edge or corner, ignore neighboring positions outside the matrix rather than treating them as zero. Every result must be computed from the original image values, not from cells that have already been smoothed.

### Function Contract
**Inputs**

- `img`: a nonempty rectangular integer matrix of pixel values

**Return value**

- A matrix of the same dimensions containing the smoothed pixel values

### Examples
**Example 1**

- Input: `img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`
- Output: `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`

**Example 2**

- Input: `img = [[7]]`
- Output: `[[7]]`

**Example 3**

- Input: `img = [[1, 2, 3]]`
- Output: `[[1, 2, 2]]`
