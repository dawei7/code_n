# Maximize Area of Square Hole in Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2943 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/) |

## Problem Description

### Goal

A grid contains $n+2$ horizontal bars and $m+2$ vertical bars, all indexed
starting from $1$. Adjacent bars initially bound unit cells. The arrays
`hBars` and `vBars` list the horizontal and vertical bars, respectively,
that are permitted to be removed; every unlisted bar is fixed.

Remove any subset of the permitted bars, possibly none, to create a
square-shaped hole. Return the maximum possible area of such a square. Removing
consecutive interior bars joins the unit strips on both sides, while gaps
between removable indices leave fixed separators in place.

### Function Contract

**Inputs**

- `n`: two fewer than the number of horizontal grid bars
- `m`: two fewer than the number of vertical grid bars
- `hBars`: the distinct removable horizontal bar indices
- `vBars`: the distinct removable vertical bar indices

Let $H=\lvert\texttt{hBars}\rvert$ and
$V=\lvert\texttt{vBars}\rvert$. The contract guarantees
$1\le n,m\le10^9$, $1\le H,V\le100$, each horizontal index lies from $2$
through $n+1$, and each vertical index lies from $2$ through $m+1$.

**Return value**

The maximum area of a square-shaped hole obtainable by removing only listed
bars.

### Examples

#### Example 1

- **Input:** `n = 2, m = 1, hBars = [2,3], vBars = [2]`
- **Output:** `4`
- **Explanation:** Removing one suitable bar in each direction creates a square
  with side length `2`.

#### Example 2

- **Input:** `n = 1, m = 1, hBars = [2], vBars = [2]`
- **Output:** `4`
- **Explanation:** Removing both listed bars joins a two-by-two block of cells.

#### Example 3

- **Input:** `n = 2, m = 3, hBars = [2,3], vBars = [2,4]`
- **Output:** `4`
- **Explanation:** The separated vertical indices cannot create a three-unit
  opening, so the largest square has side length `2`.
