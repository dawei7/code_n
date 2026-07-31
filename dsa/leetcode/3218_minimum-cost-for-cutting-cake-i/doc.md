# Minimum Cost for Cutting Cake I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3218 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/) |

## Problem Description

### Goal

An $m \times n$ rectangular cake must be divided into $1 \times 1$ pieces. The array `horizontalCut` assigns a fixed cost to each of the $m-1$ original horizontal boundary lines, while `verticalCut` assigns a fixed cost to each of the $n-1$ original vertical boundary lines.

In one operation, choose a current piece that is larger than $1 \times 1$ and cut it along one of its applicable original boundary lines. The operation splits that piece into two, and using a boundary line always costs its stored amount. Because earlier cuts create more pieces, the same original line may later need to be cut through several pieces separately. Return the minimum total cost required to produce only unit squares.

### Function Contract

**Inputs**

- `m`: The number of cake rows, with $1 \leq m \leq 20$.
- `n`: The number of cake columns, with $1 \leq n \leq 20$.
- `horizontalCut`: The $m-1$ positive horizontal-line costs, each at most $10^3$.
- `verticalCut`: The $n-1$ positive vertical-line costs, each at most $10^3$.

**Return value**

Return the minimum total cost of cutting the whole cake into $1 \times 1$ pieces.

### Examples

**Example 1**

- Input: `m = 3, n = 2, horizontalCut = [1, 3], verticalCut = [5]`
- Output: `13`
- Explanation: Cutting vertically for `5` first makes each horizontal line necessary in two pieces, giving `5 + 2 * 3 + 2 * 1 = 13`.

**Example 2**

- Input: `m = 2, n = 2, horizontalCut = [7], verticalCut = [4]`
- Output: `15`
- Explanation: Use the cost-`7` horizontal line first, then pay `4` in each of the two resulting pieces.

**Example 3**

- Input: `m = 1, n = 4, horizontalCut = [], verticalCut = [2, 1, 3]`
- Output: `6`
- Explanation: With one row, every vertical boundary is used exactly once.
