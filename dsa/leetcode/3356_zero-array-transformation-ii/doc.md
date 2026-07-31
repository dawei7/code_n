# Zero Array Transformation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3356 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zero-array-transformation-ii/) |

## Problem Description

### Goal

You are given a nonnegative integer array `nums` and an ordered list of queries. A query `[left, right, value]` permits the element at every index from `left` through `right` to be decremented by any amount between zero and `value`, inclusive. The amount is chosen independently for every covered index.

Find the smallest nonnegative $k$ such that processing the first $k$ queries in their given sequence can make every element exactly zero. The choices made for one index do not constrain the amounts chosen for the others. If no prefix of the complete query list provides enough decrement capacity, return $-1$.

### Function Contract

**Inputs**

- `nums`: The nonnegative target values to reduce to zero.
- `queries`: The ordered queries, each represented as `[left, right, value]`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. The source guarantees $1 \le n,q \le 10^5$, $0 \le \texttt{nums[i]} \le 5\cdot10^5$, $0 \le \texttt{left} \le \texttt{right} < n$, and $1 \le \texttt{value} \le 5$.

**Return value**

- Return the minimum qualifying prefix length $k$, or $-1$ if even all queries are insufficient.

### Examples

**Example 1**

- Input: `nums = [2, 0, 2], queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]`
- Output: `2`
- Explanation: Each of the first two queries supplies one unit at indices $0$ and $2$, while index $1$ can choose a decrement of zero.

**Example 2**

- Input: `nums = [4, 3, 2, 1], queries = [[1, 3, 2], [0, 2, 1]]`
- Output: `-1`
- Explanation: Across the complete query list, index $0$ receives capacity only from the second query, which is not enough to remove its value $4$.
