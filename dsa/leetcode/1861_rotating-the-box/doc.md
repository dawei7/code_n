# Rotating the Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1861 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotating-the-box/) |

## Problem Description
### Goal
An $m \times n$ character matrix `boxGrid` shows a box from the side. A `#`
cell contains a stone, a `*` cell contains a stationary obstacle, and a `.`
cell is empty. Initially, every stone is supported by an obstacle, another
stone, or the bottom of the box.

Rotate the entire box $90^\circ$ clockwise. Gravity then makes each stone fall
down until the next cell is an obstacle, another stone, or the new bottom.
Obstacles remain fixed relative to the rotating box, and rotational inertia
does not move stones sideways. Return the resulting $n \times m$ matrix.

### Function Contract
**Inputs**

- `boxGrid`: a rectangular matrix with $1 \le m,n \le 500`; every cell is
  exactly `"#"`, `"*"`, or `"."`.

Let $N = mn$ be the number of cells.

**Return value**

An $n \times m$ character matrix representing the clockwise-rotated box after
all stones have fallen.

### Examples
**Example 1**

- Input: `boxGrid = [["#",".","#"]]`
- Output: `[["."],["#"],["#"]]`

**Example 2**

- Input: `boxGrid = [["#",".","*","."],["#","#","*","."]]`
- Output: `[["#","."],["#","#"],["*","*"],[".","."]]`

**Example 3**

- Input: `boxGrid = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]`
- Output: `[[".","#","#"],[".","#","#"],["#","#","*"],["#","*","."],["#",".","*"],["#",".","."]]`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**View downward gravity before rotation**

After a clockwise rotation, falling downward corresponds to moving right in
each original row. Obstacles divide a row into independent segments: stones
within one segment pack against its right boundary without crossing an
obstacle.

**Write settled cells directly into rotated coordinates**

Create an $n \times m$ result filled with empty cells. Scan each original row
from right to left while tracking the rightmost available landing column.
When an obstacle appears at column `c`, place it at its rotated coordinate and
reset the landing column to `c - 1`. When a stone appears, place it at the
rotated coordinate corresponding to the current landing column, then decrement
that pointer. Empty cells need no action.

The scan encounters stones from rightmost to leftmost, so each stone receives
the rightmost unoccupied cell in its obstacle-delimited segment. That is
exactly where gravity leaves the stones. Original coordinate $(r,c)$ maps to
rotated coordinate $(c,m-1-r)$, so writing every obstacle and settled stone
through this mapping constructs the required orientation without a second
matrix rotation.

#### Complexity detail

Every one of the $N=mn$ source cells is inspected once and every nonempty
result cell is written once, for $O(N)$ time. The returned $n \times m$ matrix
uses $O(N)$ space; aside from that output, the landing pointer and loop indices
use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Settle then rotate:** modifying a copy row by row and rotating it afterward
  is also $O(N)$, but it performs two distinct matrix passes.
- **Move each stone one cell repeatedly:** this direct simulation is correct
  but can take $O(mn^2)$ time when many stones cross long empty suffixes.
- Obstacles reset the landing pointer and can never be overwritten or crossed.
- A row containing only empty cells remains empty after rotation.
- One-row and one-column boxes still swap dimensions according to the same
  coordinate mapping.

</details>
