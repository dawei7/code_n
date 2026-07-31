# Count the Number of Good Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2963 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-good-partitions/) |

## Problem Description
### Goal
You are given a 0-indexed array `nums` of positive integers. Partition the
entire array into one or more non-empty contiguous subarrays, preserving the
original order and using every element exactly once.

A partition is good when no numeric value occurs in two different pieces. A
value may appear repeatedly within one piece, but all of its occurrences must
belong to that same piece.

Return the total number of good partitions modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: the positive integer array to divide into contiguous pieces

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{nums[i]}\le10^9$.

**Return value**

The number of partitions in which each distinct value is confined to exactly
one piece, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `8`
- Explanation: All values are distinct, so each of the three boundaries can independently be cut or retained.

**Example 2**

- Input: `nums = [1,1,1,1]`
- Output: `1`
- Explanation: Cutting anywhere would put `1` in two pieces, leaving only the whole array as one piece.

**Example 3**

- Input: `nums = [1,2,1,3]`
- Output: `2`
- Explanation: The repeated `1` forces the first three positions together; the final `3` may remain joined or form a second piece.
