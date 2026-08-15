# Maximum Product of Two Integers With No Common Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3670 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/) |

## Problem Description

### Goal

Given a positive integer array `nums`, select elements at two distinct indices. Their binary representations must have no bit position at which both values contain a one.

Among every index pair satisfying that disjoint-set-bit condition, maximize the product of the two selected values. Duplicate array occurrences are distinct choices, although two equal positive values always share their own set bits and therefore cannot pair with each other.

Return the maximum valid product. If every pair shares at least one set bit, return `0`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $2\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^6$.

Let $B$ be the bit length of the largest input value; the contract has $B\le20$.

**Return value**

Return the largest value of `nums[i] * nums[j]` over distinct indices satisfying `nums[i] & nums[j] == 0`, or `0` if no such pair exists.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5, 6, 7]`
- **Output:** `12`
- Values `3` (`011`) and `4` (`100`) are bit-disjoint.

#### Example 2

- **Input:** `nums = [5, 6, 4]`
- **Output:** `0`
- Every pair shares a set bit.

#### Example 3

- **Input:** `nums = [64, 8, 32]`
- **Output:** `2048`
- The two largest values, `64` and `32`, use different bit positions.
