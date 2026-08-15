# Color the Triangle Red

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2647 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/color-the-triangle-red/) |

## Problem Description

### Goal

An equilateral triangle of side length $n$ is divided into $n^2$ unit equilateral triangles. Its rows are 1-indexed: row $i$ contains $2i-1$ unit triangles, whose coordinates run from $(i,1)$ through $(i,2i-1)$.

Two unit triangles are neighbors exactly when they share a complete side. Initially every unit triangle is white. Choose some triangles to color red, then repeatedly color any white triangle that has at least two red neighbors. The process stops when no such white triangle remains.

Return coordinates for a smallest possible initial red set that eventually makes all $n^2$ triangles red. More than one minimum construction may exist, and any one of them is acceptable.

### Function Contract

**Inputs**

- `n`: The side length, where $1 \le n \le 1000$.

**Return value**

- Return a list of distinct coordinate pairs `[row, column]` describing a minimum-size initial red set. Every coordinate must satisfy $1 \le \texttt{row} \le n$ and $1 \le \texttt{column} \le 2\texttt{row}-1$.

### Examples

#### Example 1

- **Input:** `n = 3`
- **Output:** `[[1,1],[2,1],[2,3],[3,1],[3,5]]`
- **Explanation:** These five triangles allow the four remaining triangles to become red one after another; no set of four can color the whole figure.

#### Example 2

- **Input:** `n = 2`
- **Output:** `[[1,1],[2,1],[2,3]]`
- **Explanation:** The middle triangle in row 2 then has enough red neighbors to turn red. Two initial triangles are insufficient.
