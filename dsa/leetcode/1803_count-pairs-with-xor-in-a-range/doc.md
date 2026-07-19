# Count Pairs With XOR in a Range

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/) |
| Frontend ID | 1803 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a positive integer array `nums` and two bounds `low` and `high`, a pair of indices $(i,j)$ is considered valid when $i<j$ and the bitwise XOR of their values lies in the inclusive interval $[\texttt{low},\texttt{high}]$.

Count all valid index pairs. Equal values at different indices remain distinct pair participants, and each unordered pair must be counted once.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 2\cdot10^4$ and $1 \le \texttt{nums[i]} \le 2\cdot10^4$.
- `low` and `high`: inclusive XOR bounds satisfying $1 \le \texttt{low}\le\texttt{high}\le2\cdot10^4$.
- Let $B=15$, the number of bits needed for all legal values and bounds.

**Return value**

- Return the number of pairs $(i,j)$ satisfying $i<j$ and $\texttt{low}\le\texttt{nums[i]}\oplus\texttt{nums[j]}\le\texttt{high}$.

### Examples

**Example 1**

- Input: `nums = [1,4,2,7], low = 2, high = 6`
- Output: `6`

Every one of the six index pairs has an XOR in the requested interval.

**Example 2**

- Input: `nums = [9,8,4,2,1], low = 5, high = 14`
- Output: `8`

Eight of the ten possible index pairs satisfy the inclusive bounds.

**Example 3**

- Input: `nums = [1,2,3], low = 1, high = 2`
- Output: `2`

The pair XOR values are `3`, `2`, and `1`.
