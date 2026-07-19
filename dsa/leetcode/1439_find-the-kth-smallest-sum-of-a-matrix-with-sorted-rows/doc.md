# Find the Kth Smallest Sum of a Matrix With Sorted Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1439 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) |

## Problem Description

### Goal

The rows of `mat` are sorted in non-decreasing order. Form a sum by choosing exactly one element from every row. Different choices count separately even when they produce equal numeric sums.

Order all possible row-choice sums from smallest to largest, preserving duplicate values by multiplicity, and return the one-based `k`th value.

Every construction uses one position from every row: no row may be skipped, and equal values chosen from different positions remain separate combinations.

### Function Contract

**Inputs**

- `mat`: an $m\times n$ integer matrix, where $1 \le m,n \le 40$.
- Every row is sorted in non-decreasing order and contains positive integers.
- `k`: a one-based rank satisfying $1 \le k \le \min(200,n^m)$.

**Return value**

- The `k`th smallest sum obtainable by selecting exactly one value from each row.

### Examples

**Example 1**

- Input: `mat = [[1,3,11],[2,4,6]], k = 5`
- Output: `7`

**Example 2**

- Input: `mat = [[1,3,11],[2,4,6]], k = 9`
- Output: `17`

**Example 3**

- Input: `mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7`
- Output: `9`
