# Max Increase to Keep City Skyline

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) |

## Problem Description

### Goal

An $n \times n$ city grid contains one building per block, and `grid[r][c]` is its height. The skyline viewed from the north or south is determined by column maxima, while the skyline from the east or west is determined by row maxima.

Increase any building heights by non-negative amounts without changing any of those four directional skylines. Return the maximum total increase summed across all buildings. A building may rise only as high as both its original row maximum and its original column maximum permit.

### Function Contract

**Inputs**

- `grid`: a nonempty square matrix of nonnegative building heights.

**Return value**

- The maximum sum of all height increases that preserves every row and column skyline.

### Examples

**Example 1**

- Input: `grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]`
- Output: `35`
- Explanation: Each building can rise to the smaller of its row maximum and column maximum; the resulting increases sum to 35.

**Example 2**

- Input: `grid = [[1,2],[3,4]]`
- Output: `1`
- Explanation: Only the upper-left building can rise, from 1 to 2.

**Example 3**

- Input: `grid = [[5]]`
- Output: `0`
- Explanation: Increasing the only building would change both skylines.
