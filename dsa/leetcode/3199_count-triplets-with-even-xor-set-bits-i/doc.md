# Count Triplets with Even XOR Set Bits I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3199 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/) |

## Problem Description

### Goal

You are given three integer arrays, `a`, `b`, and `c`. Form a triplet by independently choosing one element from each array, so every index combination `(i, j, k)` represents the values `(a[i], b[j], c[k])`.

For each such triplet, compute `a[i] XOR b[j] XOR c[k]`. A set bit is a binary digit equal to one. Count and return the index triplets whose XOR result contains an even number of set bits. Repeated values at different indices represent distinct choices and therefore contribute separately.

### Function Contract

**Inputs**

- `a`: A nonempty array of integers.
- `b`: A nonempty array of integers.
- `c`: A nonempty array of integers.

Each array length is between $1$ and $100$, and every element lies in $[0,100]$.

Let $A=\lvert\texttt{a}\rvert$, $B=\lvert\texttt{b}\rvert$, and $C=\lvert\texttt{c}\rvert$.

**Return value**

- The number of index triplets `(i, j, k)` for which `a[i] XOR b[j] XOR c[k]` has even set-bit count.

### Examples

#### Example 1

- **Input:** `a = [1], b = [2], c = [3]`
- **Output:** `1`
- **Explanation:** The only XOR is `1 XOR 2 XOR 3 = 0`, whose binary representation contains zero set bits.

#### Example 2

- **Input:** `a = [1,1], b = [2,3], c = [1,5]`
- **Output:** `4`
- **Explanation:** Exactly four index triplets produce an XOR with two set bits, including both choices of the repeated `1` in `a`.
