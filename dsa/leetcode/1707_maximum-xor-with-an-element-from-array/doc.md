# Maximum XOR With an Element From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1707 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) |

## Problem Description
### Goal

You are given a list `nums` of non-negative integers and a list of queries. Each query is `[x, m]` and may use only values `num` from `nums` satisfying $\texttt{num} \le m$. Among those eligible values, maximize the bitwise result `x ^ num`.

Return one answer for each query in its original order. When a query's limit is smaller than every number in `nums`, no eligible choice exists and its answer is `-1`. Numbers and queries may repeat, and equality with the limit is allowed.

### Function Contract
**Inputs**

- `nums`: a list of $n$ non-negative integers
- `queries`: a list of $q$ pairs `[x, m]`
- $1 \le n,q \le 10^5$, and every `nums[j]`, `x`, and `m` lies between $0$ and $10^9$

Let $B = 30$, the number of bits needed to represent values through $10^9$.

**Return value**

A length-$q$ list whose entry for `[x, m]` is the maximum `x ^ num` over all `num <= m`, or `-1` if that eligible set is empty.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]`
- Output: `[3, 3, 7]`

The eligible sets grow with limits `1`, `3`, and `6`; the best partners are `0`, `2`, and `2`, respectively.

**Example 2**

- Input: `nums = [5, 2, 4, 6, 6, 3], queries = [[12, 4], [8, 1], [6, 3]]`
- Output: `[15, -1, 5]`

The middle query has no value at most `1`. The other queries maximize their most significant differing bits among their eligible values.

**Example 3**

- Input: `nums = [1, 7, 9], queries = [[4, 0], [4, 8], [4, 10]]`
- Output: `[-1, 5, 13]`

Increasing the limit admits first `1` and `7`, then also `9`; the final XOR `4 ^ 9` equals `13`.
