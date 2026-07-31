# Find the Grid of Region Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3030 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-grid-of-region-average/) |

## Problem Description
### Goal
An $M \times N$ integer grid `image` represents a grayscale image. Each entry is a pixel intensity from $0$ through $255$. Two pixels are adjacent when they share an edge; diagonally touching pixels are not adjacent.

A region is a `3 x 3` subgrid in which the absolute intensity difference between every adjacent pair is at most the non-negative value `threshold`. Every one of the region's nine pixels belongs to that region, and overlapping regions may cause one pixel to belong to several regions.

For each valid region, first compute the average of its nine intensities and round it down. A pixel covered by one or more regions receives the rounded-down average of those already rounded-down region averages. A pixel covered by no valid region keeps its original intensity. Return the resulting $M \times N$ grid.

### Function Contract
Let $M$ and $N$ denote the number of rows and columns in `image`.

**Inputs**

- `image`: An $M \times N$ rectangular integer matrix, where $3 \le M, N \le 500$ and $0 \le \texttt{image[i][j]} \le 255$.
- `threshold`: The maximum allowed difference between adjacent pixels in a region, where $0 \le \texttt{threshold} \le 255$.

**Return value**

Return an $M \times N$ integer matrix containing the region-based intensities, with both required averaging stages rounded down.

### Examples
**Example 1**

- Input: `image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3`
- Output: `[[9,9,9,9],[9,9,9,9],[9,9,9,9]]`
- Explanation: Both `3 x 3` windows are valid. Their rounded-down averages are both `9`, so every covered pixel receives `9`.

**Example 2**

- Input: `image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12`
- Output: `[[25,25,25],[27,27,27],[27,27,27],[30,30,30]]`
- Explanation: The two regions average to `25` and `30`. Pixels in both receive `floor((25 + 30) / 2) = 27`.

**Example 3**

- Input: `image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1`
- Output: `[[5,6,7],[8,9,10],[11,12,13]]`
- Explanation: The only `3 x 3` subgrid contains vertically adjacent pixels differing by more than `1`, so no pixel belongs to a region.
