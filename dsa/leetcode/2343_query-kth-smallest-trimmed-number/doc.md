# Query Kth Smallest Trimmed Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2343 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Radix Sort, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/query-kth-smallest-trimmed-number/) |

## Problem Description

### Goal

An array `nums` contains equal-length strings made only of decimal digits.
Each query `[k, trim]` temporarily replaces every string by its rightmost
`trim` digits, orders the resulting numeric values, and asks for the original
index of the $k$th smallest trimmed value. The original strings remain
unchanged for later queries.

Leading zeros are permitted and do not change a trimmed value's numeric
meaning. Since every trimmed string in one query has equal length, its
lexicographic and numeric orders agree. When two trimmed values are equal, the
one with the smaller original index is considered smaller. Return one index
for each query in its given order.

### Function Contract

**Inputs**

- `nums`: An array of $n$ equal-length digit strings, with
  $1 \le n \le 100$ and common length between 1 and 100.
- `queries`: An array of $q$ pairs `[k, trim]`, where $1 \le q \le 100$,
  $1 \le k \le n$, and `trim` is between 1 and the common string length.

**Return value**

An array of $q$ original indices, where each entry answers the corresponding
trim-and-rank query.

### Examples

#### Example 1

- **Input:** `nums = ["102","473","251","814"]`,
  `queries = [[1,1],[2,3],[4,2],[1,2]]`
- **Output:** `[2,2,1,0]`
- **Explanation:** The requested suffix orders select indices 2, 2, 1, and 0.

#### Example 2

- **Input:** `nums = ["24","37","96","04"]`, `queries = [[2,1],[2,2]]`
- **Output:** `[3,0]`
- **Explanation:** For one digit, the equal values at indices 0 and 3 are ordered
  by index; with two digits, `"24"` is second.
