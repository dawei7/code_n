# Zero Array Transformation IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3489 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zero-array-transformation-iv/) |

## Problem Description

### Goal

You are given a non-negative integer array `nums` and an ordered list of queries. A query `[l, r, val]` lets you choose any subset of indices from the inclusive range `[l, r]` and decrement every chosen element by exactly `val`. The chosen subset may be empty and may differ from the subsets chosen for other queries.

Process some prefix of the queries in their given sequence. Find the smallest non-negative prefix length `k` for which suitable subset choices can transform every element of `nums` to zero after the first `k` queries.

Return `-1` if no prefix, including the complete query list, can produce a Zero Array. Values must reach zero exactly; merely providing a total decrement greater than an element is insufficient.

### Function Contract

**Inputs**

- `nums`: The initial non-negative values.
- `queries`: An ordered list of triples `[l, r, val]` describing an inclusive index range and an exact decrement.

Let $n=\lvert\texttt{nums}\rvert$, $q=\lvert\texttt{queries}\rvert$, and $V=\max(\texttt{nums})$. The constraints are $1\le n\le10$, $0\le V\le1000$, $1\le q\le1000$, and $1\le\texttt{val}\le10$.

Each query satisfies $0\le l\le r<n$. Because a query permits an arbitrary subset of its range, the decision to decrement one covered index is independent of the decision at every other covered index.

**Return value**

Return the minimum prefix length `k` that can make every element zero, with `0` allowed when `nums` is already a Zero Array. Return `-1` when the full query sequence is insufficient.

### Examples

**Example 1**

- Input: `nums = [2, 0, 2]`, `queries = [[0,2,1],[0,2,1],[1,1,3]]`
- Output: `2`

Choose indices 0 and 2 in each of the first two queries.

**Example 2**

- Input: `nums = [4, 3, 2, 1]`, `queries = [[1,3,2],[0,2,1]]`
- Output: `-1`

No allowed combination of exact decrements reaches every target.

**Example 3**

- Input: `nums = [1, 2, 3, 2, 1]`, `queries = [[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]]`
- Output: `4`

After the first four queries, independent subset choices can supply exact decrement totals 1, 2, 3, 2, and 1 at the five indices.

**Example 4**

- Input: `nums = [0, 0]`, `queries = [[0,1,5]]`
- Output: `0`

No query is needed when the array starts at zero.
