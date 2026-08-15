# Maximum White Tiles Covered by a Carpet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2271 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sorting, Prefix Sum, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/) |

## Problem Description

### Goal

Each entry `tiles[i] = [li, ri]` describes an inclusive interval of integer
positions: every position $j$ with $l_i\le j\le r_i$ contains a white tile.
The intervals do not overlap, but they may be given in any order.

One carpet of length `carpetLen` may be placed at any integer position. It
covers a consecutive inclusive range of exactly `carpetLen` positions, and
only white positions inside that range contribute to the result. Gaps between
white intervals are covered physically but add nothing.

Choose the carpet placement that covers the greatest possible number of white
tiles and return that maximum.

### Function Contract

**Inputs**

- `tiles`: A list of $n$ pairwise non-overlapping inclusive intervals `[left, right]`.
- `carpetLen`: The positive number of consecutive positions covered by the carpet.

The constraints are $1\le n\le5\cdot10^4$,
$1\le\texttt{left}\le\texttt{right}\le10^9$, and
$1\le\texttt{carpetLen}\le10^9$.

**Return value**

Return the maximum number of white integer positions contained in any
inclusive interval of length `carpetLen`.

### Examples

#### Example 1

- **Input:** `tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10`
- **Output:** `9`

A carpet beginning at position `10` covers nine white tiles across the
adjacent intervals `[10,11]` and `[12,18]`.

#### Example 2

- **Input:** `tiles = [[10,11],[1,1]], carpetLen = 2`
- **Output:** `2`

Placing the carpet on `[10,11]` covers both white positions.
