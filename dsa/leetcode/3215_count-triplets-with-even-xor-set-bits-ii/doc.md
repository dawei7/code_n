# Count Triplets with Even XOR Set Bits II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/) |

## Problem Description

### Goal

Choose one element from each of the three integer arrays `a`, `b`, and `c`. Every index combination $(i,j,k)$ defines a separate triplet `(a[i], b[j], c[k])`, even when some selected values are equal.

For each triplet, XOR its three values and count how many set bits appear in that result. Return the number of index triplets for which this set-bit count is even. Zero has no set bits, so its count is even.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: Nonempty integer arrays, each with at most $10^5$ elements.
- Every array value lies in $[0,10^9]$.

Let $N=\lvert a\rvert+\lvert b\rvert+\lvert c\rvert$.

**Return value**

- The number of triples $(i,j,k)$ whose value `a[i] ^ b[j] ^ c[k]` has even popcount.

### Examples

**Example 1**

- Input: `a = [1], b = [2], c = [3]`
- Output: `1`
- Explanation: `1 ^ 2 ^ 3 = 0`, which has zero set bits.

**Example 2**

- Input: `a = [1,1], b = [2,3], c = [1,5]`
- Output: `4`
- Explanation: Four index triplets produce XOR values with two set bits.
