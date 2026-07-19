# Count Fertile Pyramids in a Land

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2088 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-fertile-pyramids-in-a-land/) |

## Problem Description

### Goal

A rectangular binary matrix `grid` represents farmland: `1` is a fertile unit cell and `0` is barren. Cells outside the matrix are also treated as barren. A pyramidal plot contains more than one cell, all fertile, and has a topmost apex `(r, c)`. At level $d$ below that apex, it includes every column from $c-d$ through $c+d$.

An inverse pyramid has the same filled triangular shape reflected vertically: its apex is the bottommost cell, and level $d$ above it spans the same width $2d+1$. Height is the number of occupied rows, so only heights of at least two count. Return the total number of upright and inverse fertile pyramids, counting every apex, height, and orientation separately.

### Function Contract

**Input**

- `grid`: an $m \times n$ binary matrix.
- $1 \le m,n \le 1000$ and $1 \le mn \le 10^5$.

For an upright pyramid of height $h$ with apex $(r,c)$, level $i$ contains

$$
\{(r+i,j) \mid c-i \le j \le c+i\},
\qquad 0 \le i < h.
$$

An inverse pyramid uses row $r-i$ instead. In either orientation, $h \ge 2$ and every included cell must equal `1`.

**Return value**

Return the number of valid upright and inverse pyramidal plots.

### Examples

**Example 1**

- Input: `grid = [[0,1,1,0],[1,1,1,1]]`
- Output: `2`
- Explanation: Two different top-row apexes form height-two upright pyramids.

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1]]`
- Output: `2`
- Explanation: The matrix contains one upright and one inverse height-two pyramid.

**Example 3**

- Input: `grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]`
- Output: `13`
- Explanation: Seven plots are upright and six are inverse.
