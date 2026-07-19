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

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The height represented by one state**

For an upright orientation, let the state at `(r, c)` be the greatest fertile pyramid height whose apex is that cell. A barren apex has height zero. A fertile apex always supplies height one, but extending it by another level requires three supporting pyramids in the row below: those centered at columns `c - 1`, `c`, and `c + 1`.

Therefore an interior fertile cell satisfies

$$
\operatorname{height}(r,c)
= 1 + \min\!\bigl(
\operatorname{height}(r+1,c-1),
\operatorname{height}(r+1,c),
\operatorname{height}(r+1,c+1)
\bigr).
$$

A boundary column cannot extend beyond height one because an outside supporting cell is barren. Processing rows from bottom to top makes all three dependencies available.

**Why a maximum height contributes several plots**

If an apex supports maximum height $h$, then the nested shapes of heights $2,3,\ldots,h$ are all valid and distinct. Its contribution is therefore $h-1$. Summing that quantity over every apex counts each upright pyramid exactly once, at its unique topmost cell and chosen height.

**Reflecting the recurrence**

Inverse pyramids obey the identical recurrence with support in the row above. A second pass from top to bottom counts them. Only the immediately preceding support row is needed in either pass, so the two-dimensional state can be compressed to two length-$n$ arrays.

#### Complexity detail

Each of the $mn$ cells is processed once per orientation with constant work, for $O(mn)$ time. A current row and one supporting row use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Expand every candidate height:** Testing every cell in every possible triangular plot repeats the same fertility checks and has polynomially slower worst-case growth.
- **Full two-dimensional DP:** Storing every height is correct and still uses $O(mn)$ time, but requires $O(mn)$ rather than $O(n)$ auxiliary space.
- **Prefix sums by row:** Row sums can test whether each horizontal level is fertile, yet every apex may still try many heights, so the worst case remains slower than the local recurrence.
- A single fertile cell and every height-one shape are excluded because a plot must contain more than one cell.
- Upright and inverse plots with the same cells are counted separately when both definitions are satisfied.
- A zero anywhere in a required base level limits every larger pyramid containing that level.
- One-row or one-column matrices cannot contain a height-two pyramid.

</details>
