# Mark Elements on Array by Performing Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3080 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of $n$ positive integers and an array `queries` containing $m$ pairs. Every element of `nums` begins unmarked.

Process the queries in their given order. For a query `[index, k]`, first mark the element at `index` if it is still unmarked. Then mark exactly $k$ of the remaining unmarked elements with the smallest values. When equal values are available, choose smaller indices first. If fewer than $k$ unmarked elements remain, mark all of them instead.

After each query, record the sum of every element that is still unmarked. Return the $m$ recorded sums in query order.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `queries`: A list of $m$ pairs `[index, k]` describing the explicit index and the number of smallest unmarked elements to mark.

The constraints are $1 \leq m \leq n \leq 10^5$, $1 \leq \texttt{nums[i]} \leq 10^5$, and $0 \leq \texttt{index}, k \leq n-1$ for every query.

**Return value**

- A list of $m$ integers where entry $i$ is the sum of the unmarked elements after processing query $i$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 2, 1, 2, 3, 1]`, `queries = [[1, 2], [3, 3], [4, 2]]`
- **Output:** `[8, 3, 0]`
- **Explanation:** The first query marks index `1` and the values at indices `0` and `3`, leaving a sum of `8`. Index `3` is already marked for the second query; the next three smallest eligible elements leave only the value `3`. The last query marks everything that remains.

#### Example 2

- **Input:** `nums = [1, 4, 2, 3]`, `queries = [[0, 1]]`
- **Output:** `[7]`
- **Explanation:** Marking index `0` and then the smallest remaining value, `2`, leaves `4 + 3 = 7`.
