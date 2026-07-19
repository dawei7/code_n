# Minimum XOR Sum of Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) |
| Frontend ID | 1879 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two equal-length integer arrays have an XOR sum obtained by XORing values at matching indices and adding the results:

$$
\sum_{i=0}^{N-1}\bigl(\texttt{nums1[i]}\mathbin{\mathrm{XOR}}\texttt{nums2[i]}\bigr).
$$

You may rearrange the elements of `nums2` in any order while leaving `nums1` fixed. Choose a permutation that minimizes this total and return the resulting minimum XOR sum. Every occurrence in `nums2`, including duplicate values, must be assigned to exactly one index of `nums1`.

### Function Contract

**Inputs**

- `nums1`, `nums2`: integer arrays of the same length $N$, where $1 \le N \le 14$ and every value lies from $0$ through $10^7$.

**Return value**

- Return the minimum sum of pairwise XOR values obtainable by permuting `nums2`.

### Examples

**Example 1**

- Input: `nums1 = [1,2], nums2 = [2,3]`
- Output: `2`

Rearranging `nums2` to `[3,2]` gives `(1 XOR 3) + (2 XOR 2) = 2`.

**Example 2**

- Input: `nums1 = [1,0,3], nums2 = [5,3,4]`
- Output: `8`

The arrangement `[5,4,3]` contributes $4+4+0$.

**Example 3**

- Input: `nums1 = [2,4,6], nums2 = [1,3,5]`
- Output: `9`

No permutation produces an XOR sum below $9$.
