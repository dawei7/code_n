# Find The Original Array of Prefix Xor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) |

## Problem Description

### Goal

An integer array `pref` of length $n$ was produced from an unknown array `arr` of the same length. For every index $i$, `pref[i]` is the bitwise XOR of all original values from `arr[0]` through `arr[i]`.

Reconstruct and return the complete original array of values. Bitwise XOR is denoted by `^`, and the prefix information determines exactly one valid answer.

### Function Contract

**Inputs**

- `pref`: The nonempty array of prefix-XOR values.

Its length satisfies $1 \le n \le 10^5$, and every value lies in $[0,10^6]$.

**Return value**

- The unique array `arr` satisfying `pref[i] = arr[0] ^ ... ^ arr[i]` at every index.

### Examples

**Example 1**

- Input: `pref = [5, 2, 0, 3, 1]`
- Output: `[5, 7, 2, 3, 2]`

Successively XORing the returned values produces the supplied prefixes 5, 2, 0, 3, and 1.

**Example 2**

- Input: `pref = [13]`
- Output: `[13]`

The first prefix contains only the first original value.

**Example 3**

- Input: `pref = [7, 7, 7]`
- Output: `[7, 0, 0]`

An unchanged prefix XOR means the newly added original value is zero.
