# Find the Prefix Common Array of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2657 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) |

## Problem Description

### Goal

You are given two 0-indexed integer arrays `A` and `B`, each of length $n$. Both arrays are permutations of the integers from $1$ through $n$, so every value in that range occurs exactly once in each array.

Construct a prefix common array `C` of length $n$. For every index `i`, `C[i]` is the number of distinct values that have appeared at or before `i` in both arrays: a value counts once when it belongs to both `A[0:i + 1]` and `B[0:i + 1]`. Return the complete array `C`.

### Function Contract

**Inputs**

- `A`: A permutation of the integers from $1$ through $n$.
- `B`: Another permutation of the integers from $1$ through $n$, where $1 \le n \le 50$.

**Return value**

- Return an array `C` where `C[i]` is the number of values present in both prefixes ending at `i`.

### Examples

**Example 1**

- Input: `A = [1,3,2,4], B = [3,1,2,4]`
- Output: `[0,2,3,4]`
- Explanation: The common-value counts for the growing prefixes are zero, two, three, and four.

**Example 2**

- Input: `A = [2,3,1], B = [3,1,2]`
- Output: `[0,1,3]`
- Explanation: No value is common after the first positions, only `3` is common after the second, and all values are common at the end.
