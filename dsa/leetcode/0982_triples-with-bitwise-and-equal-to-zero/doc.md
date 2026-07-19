# Triples with Bitwise AND Equal To Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 982 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/) |

## Problem Description

### Goal

Given an integer array `nums`, count its AND triples. An AND triple is an ordered triple of indices `(i, j, k)` for which `nums[i] & nums[j] & nums[k] == 0`.

Each of `i`, `j`, and `k` may independently be any valid array index. The indices do not need to be distinct, and changing their order creates a different triple when the ordered index tuple changes. Return the total number of tuples satisfying the zero bitwise-AND condition.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le1000$ and $0\le\texttt{nums[i]}<2^{16}$.

Let $D$ be the number of distinct input values and $U$ the number of distinct masks produced by ANDing ordered pairs. Both are at most $N$ and $\min(N^2,2^{16})$, respectively.

**Return value**

- The number of ordered index triples whose three selected values have bitwise AND equal to zero.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `12`
- Explanation: twelve ordered choices of `(i, j, k)` produce zero after the two bitwise-AND operations.

**Example 2**

- Input: `nums = [0, 0, 0]`
- Output: `27`
- Explanation: all $3^3$ ordered triples qualify.
