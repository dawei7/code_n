# Online Majority Element In Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1157 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Design, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/online-majority-element-in-subarray/) |

## Problem Description

### Goal

Design a `MajorityChecker` for an integer array `arr`. The constructor stores the array so that many online range queries can be answered without rescanning every requested subarray.

For `query(left, right, threshold)`, consider the inclusive subarray from index `left` through index `right`. Return a value that occurs at least `threshold` times in that range, or return `-1` if no such value exists. Every query guarantees $2 \cdot \texttt{threshold} > \texttt{right} - \texttt{left} + 1$, so at most one value can satisfy the threshold.

### Function Contract

**Inputs**

- `arr`: The constructor array of length $n$, where $1 \le n \le 2 \cdot 10^4$ and $1 \le \texttt{arr[i]} \le 2 \cdot 10^4$.
- `queries`: The app adapter's list of $q$ triples `[left, right, threshold]`. Each triple satisfies $0 \le \texttt{left} \le \texttt{right} < n$, $1 \le \texttt{threshold} \le \texttt{right} - \texttt{left} + 1$, and the strict-majority guarantee above. The native interface permits at most $10^4$ calls to `query`.

**Return value**

- The app-local `solve(arr, queries)` returns one result per query in input order. Each result is the qualifying value for that inclusive range, or `-1` when none exists.

### Examples

**Example 1**

- Input: `arr = [1,1,2,2,1,1]`, `queries = [[0,5,4]]`
- Output: `[1]`

**Example 2**

- Input: `arr = [1,1,2,2,1,1]`, `queries = [[0,3,3]]`
- Output: `[-1]`

**Example 3**

- Input: `arr = [1,1,2,2,1,1]`, `queries = [[2,3,2]]`
- Output: `[2]`
