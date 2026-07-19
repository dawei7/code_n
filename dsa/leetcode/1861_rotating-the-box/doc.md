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
