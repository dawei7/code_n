# Count Positions on Street With Required Brightness

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2237 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) |

## Problem Description

### Goal

A straight street contains the integer positions from $0$ through $n-1$. Each
street lamp is described by `lights[i] = [position_i, range_i]`. That lamp
illuminates every position in the inclusive interval from
`max(0, position_i - range_i)` through
`min(n - 1, position_i + range_i)`; clipping keeps its coverage within the
street.

The brightness of a position is the number of lamps whose illuminated
intervals contain it. A 0-indexed array `requirement` gives the minimum
brightness required at every street position. Return the number of positions
whose actual brightness is at least their corresponding requirement.

### Function Contract

**Inputs**

- `n`: The street length, satisfying $1\le n\le 10^5$.
- `lights`: A list of between $1$ and $10^5$ pairs `[position, range]`.
- `requirement`: An array of length $n$ whose entry at index $i$ is the minimum required brightness at position $i$.

Every lamp position satisfies $0\le\texttt{position}<n$, every range satisfies
$0\le\texttt{range}\le 10^5$, and every requirement satisfies
$0\le\texttt{requirement[i]}\le 10^5$.

**Return value**

Return the number of indices $i$ for which the number of lamp intervals
containing $i$ is at least `requirement[i]`.

### Examples

#### Example 1

- **Input:** `n = 5, lights = [[0, 1], [2, 1], [3, 2]], requirement = [0, 2, 1, 4, 1]`
- **Output:** `4`

#### Example 2

- **Input:** `n = 1, lights = [[0, 1]], requirement = [2]`
- **Output:** `0`

#### Example 3

- **Input:** `n = 4, lights = [[1, 0]], requirement = [0, 1, 0, 0]`
- **Output:** `4`
