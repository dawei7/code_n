# Zero Array Transformation III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3362 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii/) |

## Problem Description

### Goal

You are given a nonnegative integer array `nums` and a collection of inclusive index intervals. A query `[l, r]` may reduce every value from index `l` through `r` by at most one. The reduction amount is chosen independently at each covered index, so using a query does not require decrementing positions that are already zero.

Remove as many queries as possible while retaining a set that can reduce every element of `nums` to zero. Equivalently, each index must remain covered by at least its original value many retained queries. Return the maximum removable count, or return `-1` when even the complete query collection cannot provide sufficient coverage.

### Function Contract

**Inputs**

- `nums`: The required decrement count at each array index.
- `queries`: Inclusive intervals `[l, r]` whose endpoints are valid indices of `nums`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. Both satisfy $1\le n,q\le10^5$; every `nums[i]` is between $0$ and $10^5$, inclusive.

**Return value**

- The maximum number of queries that may be removed while preserving feasibility, or `-1` if all queries together are insufficient.

### Examples

**Example 1**

- Input: `nums = [2, 0, 2]`, `queries = [[0, 2], [0, 2], [1, 1]]`
- Output: `1`
- Explanation: Keep the two full-range queries. Each supplies one decrement at indices 0 and 2, while their effect at index 1 may be chosen as zero.

**Example 2**

- Input: `nums = [1, 1, 1, 1]`, `queries = [[1, 3], [0, 2], [1, 3], [1, 2]]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3, 4]`, `queries = [[0, 3]]`
- Output: `-1`
- Explanation: The single query supplies only one unit at the last index, but that index requires four.
