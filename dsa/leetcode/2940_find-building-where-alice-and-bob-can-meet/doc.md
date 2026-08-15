# Find Building Where Alice and Bob Can Meet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2940 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Heap (Priority Queue), Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/) |

## Problem Description

### Goal

A 0-indexed array `heights` describes a row of buildings, where
`heights[i]` is the positive height of building `i`. From building `i`, a
person may move directly to building `j` if and only if $i<j$ and
$\texttt{heights[i]}<\texttt{heights[j]}$.

Each entry `queries[i] = [a_i, b_i]` independently places Alice at building
`a_i` and Bob at building `b_i`. For every query, find the leftmost
building that both people can reach, allowing either person to remain at their
starting building. Return `-1` for a query when no common reachable building
exists.

### Function Contract

**Inputs**

- `heights`: the building heights in left-to-right order
- `queries`: pairs containing Alice's and Bob's starting indices

Let $N=\lvert\texttt{heights}\rvert$ and
$Q=\lvert\texttt{queries}\rvert$. The contract guarantees
$1 \le N,Q \le 5\cdot10^4$, $1 \le \texttt{heights[i]} \le 10^9$, and
every query index is between $0$ and $N-1$, inclusive.

**Return value**

A length-$Q$ list whose entry for each query is the leftmost common reachable
building index, or `-1` when there is none.

### Examples

#### Example 1

- **Input:** `heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]`
- **Output:** `[2,5,-1,5,2]`
- **Explanation:** Some queries meet at a later building taller than both starts;
  the final query already places both people at building `2`.

#### Example 2

- **Input:** `heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]`
- **Output:** `[7,6,-1,4,6]`
- **Explanation:** A later starting building is itself the answer when the person
  on the left can move directly to it; otherwise the search continues right.

#### Example 3

- **Input:** `heights = [1,2,1,2], queries = [[0,0]]`
- **Output:** `[0]`
- **Explanation:** Alice and Bob already occupy the same building.
