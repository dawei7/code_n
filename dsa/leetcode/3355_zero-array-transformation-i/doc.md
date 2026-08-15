# Zero Array Transformation I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3355 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zero-array-transformation-i/) |

## Problem Description

### Goal

You are given a nonnegative integer array `nums` and a list of inclusive index ranges `queries`. Process the queries sequentially. For a query `[left, right]`, choose any subset of the indices from `left` through `right`, then decrement the value at every chosen index by exactly one.

The subset chosen for one query may differ from every other choice, and an index in the range may be omitted. Determine whether choices can be made so that, after all queries have been processed, every element of `nums` equals zero. Return `true` when such choices exist and `false` otherwise.

### Function Contract

**Inputs**

- `nums`: The nonnegative integer array to transform.
- `queries`: The list of inclusive ranges, where each entry is `[left, right]`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. The source guarantees $1 \le n,q \le 10^5$, $0 \le \texttt{nums[i]} \le 10^5$, and $0 \le \texttt{left} \le \texttt{right} < n$ for every query.

**Return value**

- Return whether the available query coverage can transform `nums` into a Zero Array.

### Examples

#### Example 1

- **Input:** `nums = [1, 0, 1], queries = [[0, 2]]`
- **Output:** `true`
- **Explanation:** For the single query, choose indices $0$ and $2$; decrementing them produces `[0, 0, 0]`.

#### Example 2

- **Input:** `nums = [4, 3, 2, 1], queries = [[1, 3], [0, 2]]`
- **Output:** `false`
- **Explanation:** Index $0$ is covered only once, so its value $4$ cannot be reduced to zero.
