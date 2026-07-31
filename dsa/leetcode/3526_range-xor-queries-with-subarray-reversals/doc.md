# Range XOR Queries with Subarray Reversals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3526 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/) |

## Problem Description

### Goal

You are given an integer array `nums` and a sequence of three-field queries. Process the queries in order while treating `nums` as one mutable sequence. An update query `[1, index, value]` assigns `value` at `index`. A range query `[2, left, right]` computes the bitwise XOR of every element in the inclusive subarray from `left` through `right`. A reversal query `[3, left, right]` reverses that inclusive subarray in place.

Only type-2 queries produce output. Return their XOR results in the same order in which those queries occur. Both point updates and reversals persist, so every later query observes the sequence produced by all earlier operations.

### Function Contract

**Inputs**

- `nums`: The initial mutable integer array of length $n$.
- `queries`: A list of queries, each encoded as three integers according to its type.

The constraints are $1 \le n \le 10^5$, $0 \le \texttt{nums[i]} \le 10^9$, and $1 \le \lvert\texttt{queries}\rvert \le 10^5$. Query indices form valid inclusive positions or ranges, and update values are between $0$ and $10^9$.

**Return value**

- An integer array containing one result for every type-2 range XOR query.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], queries = [[2, 1, 3], [1, 2, 10], [3, 0, 4], [2, 0, 4]]`
- Output: `[5, 8]`
- Explanation: The first queried range has XOR `2 ^ 3 ^ 4 = 5`. After the update and full reversal, the array is `[5, 4, 10, 2, 1]`, whose full XOR is `8`.

**Example 2**

- Input: `nums = [7, 8, 9], queries = [[1, 0, 3], [2, 0, 2], [3, 1, 2]]`
- Output: `[2]`
- Explanation: The update produces `[3, 8, 9]`, and `3 ^ 8 ^ 9 = 2`. The final reversal produces no additional output.
