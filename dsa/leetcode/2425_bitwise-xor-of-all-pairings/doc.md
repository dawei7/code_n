# Bitwise XOR of All Pairings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2425 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Bitwise XOR of All Pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings/) |

## Problem Description

### Goal

You are given two 0-indexed arrays `nums1` and `nums2` containing non-negative integers. Pair every element of `nums1` with every element of `nums2` exactly once, and compute the bitwise XOR of the two values in each pairing.

Conceptually place all of those pairwise XOR values into a third array. Return the bitwise XOR of every value in that array. The result must account for the full Cartesian product, although that product does not need to be constructed explicitly.

### Function Contract

**Inputs**

- `nums1`: A non-empty list of non-negative integers.
- `nums2`: A non-empty list of non-negative integers.

Let $n = \lvert\texttt{nums1}\rvert$ and $m = \lvert\texttt{nums2}\rvert$. The constraints are $1 \le n,m \le 10^5$ and $0 \le \texttt{nums1[i]},\texttt{nums2[j]} \le 10^9$.

**Return value**

- The XOR of all $n \cdot m$ values `nums1[i] ^ nums2[j]`.

### Examples

#### Example 1

- **Input:** `nums1 = [2,1,3], nums2 = [10,2,5,0]`
- **Output:** `13`

Every first-array value occurs in four pairings and cancels; the XOR of `nums2` remains because `nums1` has odd length.

#### Example 2

- **Input:** `nums1 = [1,2], nums2 = [3,4]`
- **Output:** `0`

Both array lengths are even, so every source value occurs an even number of times in the full XOR.

#### Example 3

- **Input:** `nums1 = [5], nums2 = [1,2,3]`
- **Output:** `5`

The source-array contributions reduce to `5 ^ 1 ^ 2 ^ 3`, which equals 5.
