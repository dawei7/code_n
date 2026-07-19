# Minimum Number of Taps to Open to Water a Garden

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1326 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |

## Problem Description
### Goal
A one-dimensional garden occupies the closed interval from 0 through `n`. One tap stands at every integer point `i` from 0 through `n`; opening it waters the interval from `i - ranges[i]` through `i + ranges[i]`, clipped conceptually to the garden.

Choose the fewest taps whose combined watered intervals cover every point of `[0, n]`. Return that minimum number, or `-1` when some part of the garden cannot be reached by any selection of taps.

Coverage is continuous rather than limited to integer positions. Intervals that meet at an endpoint connect without leaving a gap.

### Function Contract
**Inputs**

- `n`: the garden length, where $1\le n\le10^4$.
- `ranges`: an array of length $n+1$ with $0\le\texttt{ranges[i]}\le100$.

**Return value**

The minimum number of taps required to cover the entire closed interval $[0,n]$, or `-1` if full coverage is impossible.

### Examples
**Example 1**

- Input: `n = 5, ranges = [3,4,1,1,0,0]`
- Output: `1`
- Explanation: The tap at position 1 covers the whole garden.

**Example 2**

- Input: `n = 3, ranges = [0,0,0,0]`
- Output: `-1`
- Explanation: No tap covers any positive-length segment.

**Example 3**

- Input: `n = 7, ranges = [1,2,1,0,2,1,0,1]`
- Output: `3`
- Explanation: Three suitably overlapping tap intervals cover from 0 through 7.
