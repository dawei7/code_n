# Find if Array Can Be Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3011 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-if-array-can-be-sorted/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of positive integers. In one operation,
you may swap two adjacent elements only when their binary representations
contain the same number of set bits. Perform any number of such operations,
including none.

Return whether the array can become sorted in ascending order.

The set-bit count of a value is the number of `1` digits in its binary
representation. Each operation acts on one neighboring pair in the current
array, and the final order must be non-decreasing across every adjacent pair.

### Function Contract

**Inputs**

- `nums`: the positive-integer array whose adjacent values may be swapped

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $1\le N\le100$
and $1\le\texttt{nums[i]}\le2^8$.

**Return value**

Return `true` exactly when some legal sequence of swaps sorts the array in
non-decreasing order; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [8,4,2,30,15]`
- **Output:** `true`

The first three values each have one set bit and may be reordered; the final
two each have four and may also be reordered.

#### Example 2

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `true`

The array is already sorted, so no operation is necessary.

#### Example 3

- **Input:** `nums = [3,16,8,4,2]`
- **Output:** `false`

The initial 3 cannot cross the following block of one-set-bit values.
