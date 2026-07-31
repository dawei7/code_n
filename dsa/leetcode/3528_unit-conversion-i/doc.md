# Unit Conversion I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3528 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unit-conversion-i/) |

## Problem Description

### Goal

There are $n$ unit types numbered from $0$ through $n-1$. Each entry `[source, target, factor]` in `conversions` states that one unit of type `source` equals `factor` units of type `target`. The $n-1$ directed conversions form a rooted tree: starting from unit `0`, every other unit is reachable through exactly one directed sequence of conversions. The entries themselves need not be ordered by that sequence.

Return an array in which position $i$ gives the number of type-$i$ units equivalent to one unit of type `0`. Multiply the factors along the unique directed path from `0` to $i$, and report every value modulo $10^9+7$.

### Function Contract

**Inputs**

- `conversions`: A list of $n-1$ triples `[source, target, factor]` describing the directed conversion tree.

The constraints are $2 \le n \le 10^5$, valid unit indices, and $1 \le \texttt{factor} \le 10^9$. Every unit is reachable from unit `0` through one unique forward-only conversion path.

**Return value**

- An array of length $n$ containing each conversion amount from one base unit, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `conversions = [[0, 1, 2], [1, 2, 3]]`
- Output: `[1, 2, 6]`
- Explanation: One type-0 unit gives two type-1 units, then six type-2 units.

**Example 2**

- Input: `conversions = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 2], [4, 6, 3], [5, 7, 4]]`
- Output: `[1, 2, 3, 8, 10, 6, 30, 24]`
