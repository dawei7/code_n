# Minimum Cost for Cutting Cake II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3219 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/) |

## Problem Description

### Goal

An $m \times n$ cake must be divided into $1 \times 1$ pieces. `horizontalCut` gives the fixed cost of each of the $m-1$ original horizontal boundary lines, and `verticalCut` gives the cost of each of the $n-1$ original vertical boundary lines.

Each operation selects one current non-unit piece and cuts it along an applicable original boundary, splitting that piece in two. A boundary retains its stated cost whenever it is used, but cutting in one orientation creates more pieces through which later perpendicular boundaries must pass. Return the minimum total cost. The dimensions may reach $10^5$, so the method must scale to nearly $2\cdot10^5$ boundary costs and totals beyond 32-bit range.

### Function Contract

**Inputs**

- `m`: The number of rows, with $1 \leq m \leq 10^5$.
- `n`: The number of columns, with $1 \leq n \leq 10^5$.
- `horizontalCut`: Exactly $m-1$ horizontal costs, each between $1$ and $10^3$.
- `verticalCut`: Exactly $n-1$ vertical costs, each between $1$ and $10^3$.

**Return value**

Return the minimum total cost of producing only $1 \times 1$ pieces.

### Examples

**Example 1**

- Input: `m = 3, n = 2, horizontalCut = [1, 3], verticalCut = [5]`
- Output: `13`

**Example 2**

- Input: `m = 2, n = 2, horizontalCut = [7], verticalCut = [4]`
- Output: `15`

**Example 3**

- Input: `m = 1, n = 4, horizontalCut = [], verticalCut = [2, 1, 3]`
- Output: `6`
