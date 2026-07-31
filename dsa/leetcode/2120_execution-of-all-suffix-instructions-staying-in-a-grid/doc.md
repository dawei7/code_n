# Execution of All Suffix Instructions Staying in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/) |

## Problem Description
### Goal

An $n \times n$ grid uses zero-based coordinates from the top-left cell
`[0, 0]` through the bottom-right cell `[n - 1, n - 1]`. A robot begins at the
cell `startPos`.

The string `s` contains movement instructions: `L` moves one column left, `R`
moves one column right, `U` moves one row up, and `D` moves one row down. For
each index $i$, independently reset the robot to `startPos` and attempt to
execute the suffix `s[i:]` in order. Stop before the first instruction that
would leave the grid, or after the suffix ends.

Return one count per starting index: the number of instructions successfully
executed before that run stops. An instruction that would leave the grid is
not included in its count.

### Function Contract
**Inputs**

- `n`: The positive side length of the square grid.
- `startPos`: The two-element starting coordinate `[row, column]`, which lies
  inside the grid.
- `s`: A nonempty instruction string containing only `L`, `R`, `U`, and `D`.
  Let $m = \lvert s\rvert$.

**Return value**

Return a list of $m$ integers. Element `answer[i]` is the number of executable
instructions in the suffix beginning at `s[i]` when starting anew from
`startPos`.

### Examples
**Example 1**

- Input: `n = 3, startPos = [0, 1], s = "RRDDLU"`
- Output: `[1, 5, 4, 3, 1, 0]`

The suffix beginning at index zero executes one right move before the next
would leave the grid; the suffix beginning at index one executes all five
moves.

**Example 2**

- Input: `n = 2, startPos = [1, 1], s = "LURD"`
- Output: `[4, 1, 0, 0]`

**Example 3**

- Input: `n = 1, startPos = [0, 0], s = "LRUD"`
- Output: `[0, 0, 0, 0]`

Every possible first move leaves a one-cell grid.
