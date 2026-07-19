# Closest Room

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/closest-room/) |
| Frontend ID | 1847 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each entry in `rooms` supplies a unique room identifier and that room's size. Every query supplies a preferred identifier and a minimum acceptable size. A room is eligible for the query only when its size is at least that minimum.

Among eligible rooms, choose the identifier with the smallest absolute difference from the preferred identifier. If two identifiers are equally distant, choose the smaller identifier. Return the selected identifier for every query in the original query order, using `-1` when no room meets the size requirement.

### Function Contract

**Inputs**

- `rooms`: a list of `[roomId, size]` pairs with unique `roomId` values.
- `queries`: a list of `[preferred, minSize]` pairs.
- $1 \le \lvert\texttt{rooms}\rvert,\lvert\texttt{queries}\rvert \le 10^5$.
- Room IDs, preferred IDs, room sizes, and minimum sizes are positive and at most $10^7$.
- Let $r=\lvert\texttt{rooms}\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- For each query, consider exactly rooms whose size is at least `minSize`.
- Minimize $\lvert\texttt{roomId}-\texttt{preferred}\rvert$.
- On equal distance, choose the smaller `roomId`.
- Return `-1` if the eligible set is empty.
- Preserve the original order of the queries in the output list.

### Examples

**Example 1**

- Input: `rooms = [[2, 2], [1, 2], [3, 2]]`, `queries = [[3, 1], [3, 3], [5, 2]]`
- Output: `[3, -1, 3]`

No room reaches size 3 for the second query.

**Example 2**

- Input: `rooms = [[1, 4], [2, 3], [3, 5], [4, 1]]`, `queries = [[2, 3], [2, 4], [2, 5]]`
- Output: `[2, 1, 3]`

For minimum size 4, IDs 1 and 3 are equally distant from preferred ID 2, so ID 1 wins the tie.

**Example 3**

- Input: `rooms = [[10, 2]]`, `queries = [[5, 1], [20, 3]]`
- Output: `[10, -1]`
