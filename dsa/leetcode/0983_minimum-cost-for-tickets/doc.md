# Minimum Cost For Tickets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 983 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-for-tickets/) |

## Problem Description

### Goal

You plan train travel during one year. The strictly increasing array `days` lists every calendar day on which you will travel, using day numbers from `1` through `365`.

Three passes are available: a 1-day pass costs `costs[0]`, a 7-day pass costs `costs[1]`, and a 30-day pass costs `costs[2]`. A pass covers its stated number of consecutive calendar days, including the purchase day; for example, a 7-day pass starting on day `2` covers days `2` through `8`. Buy any combination of passes and return the minimum total cost that covers every listed travel day.

### Function Contract

**Inputs**

- `days`: a strictly increasing list of $N$ travel days, where $1\le N\le365$ and $1\le\texttt{days[i]}\le365$.
- `costs`: exactly three positive ticket prices, each from $1$ through $1000$, corresponding to durations $1$, $7$, and $30$.

**Return value**

- The minimum number of dollars required to cover every day in `days`.

### Examples

**Example 1**

- Input: `days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]`
- Output: `11`
- Explanation: one optimal plan uses 1-day passes for days `1` and `20` plus a 7-day pass covering the middle travel days.

**Example 2**

- Input: `days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs = [2, 7, 15]`
- Output: `17`
- Explanation: a 30-day pass covers days `1` through `30`, and a 1-day pass covers day `31`.
