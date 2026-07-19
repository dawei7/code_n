# Circular Permutation in Binary Representation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1238 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/circular-permutation-in-binary-representation/) |

## Problem Description

### Goal

Given integers `n` and `start`, return any permutation `p` of every integer from $0$ through $2^n-1$. The first element must be `start`, and the $n$-bit representations of each adjacent pair `p[i]` and `p[i + 1]` must differ in exactly one bit.

The permutation is circular: the binary representations of its last and first elements must also differ in exactly one bit. Every value in the $n$-bit domain must occur exactly once. More than one ordering may satisfy these requirements, and any valid ordering may be returned.

### Function Contract

**Inputs**

- `n`: The number of bits, where $1\le n\le16$.
- `start`: The required first value, where $0\le\texttt{start}<2^n$.

**Return value**

- Any circular one-bit-difference permutation of all $2^n$ values whose first element is `start`.

### Examples

**Example 1**

- Input: `n = 2`, `start = 3`
- Output: `[3,2,0,1]`

In binary, `11`, `10`, `00`, and `01` differ by one bit around the full cycle.

**Example 2**

- Input: `n = 3`, `start = 2`
- Output: `[2,6,7,5,4,0,1,3]`

The sequence contains every three-bit value and returns from `3` to `2` by one bit.

**Example 3**

- Input: `n = 1`, `start = 1`
- Output: `[1,0]`

The two one-bit values are adjacent in both circular directions.
