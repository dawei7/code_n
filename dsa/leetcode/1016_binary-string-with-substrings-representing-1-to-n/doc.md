# Binary String With Substrings Representing 1 To N

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1016 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/) |

## Problem Description

### Goal

You are given a binary string `s` and a positive integer `n`. For every integer in the inclusive range `[1, n]`, write its standard binary representation without leading zeroes.

Return `true` if each of those representations occurs in `s` as a substring; otherwise return `false`. A substring must occupy contiguous character positions, although different required representations may overlap or occur at the same region of `s`.

### Function Contract

**Inputs**

- `s`: a binary string of length $M$, where $1\le M\le1000$.
- `n`: a positive upper bound satisfying $1\le n\le10^9$.

Let $L=\lfloor\log_2 n\rfloor+1$ be the bit length of `n`.

**Return value**

- `True` exactly when every standard binary representation from `1` through `n` is a substring of `s`.

### Examples

**Example 1**

- Input: `s = "0110", n = 3`
- Output: `True`
- Explanation: The representations `1`, `10`, and `11` all occur contiguously.

**Example 2**

- Input: `s = "0110", n = 4`
- Output: `False`
- Explanation: The representation `100` does not occur.

**Example 3**

- Input: `s = "1111000101", n = 5`
- Output: `True`
- Explanation: The string contains `1`, `10`, `11`, `100`, and `101`.
