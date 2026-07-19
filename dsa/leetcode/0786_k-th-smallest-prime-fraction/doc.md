# K-th Smallest Prime Fraction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 786 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-smallest-prime-fraction/) |

## Problem Description

### Goal

Given a strictly increasing array `arr` containing `1` and distinct prime numbers, form every fraction `arr[i] / arr[j]` with `0 <= i < j < len(arr)`.

Order all such fractions by their numerical values and return the numerator and denominator of the `k`th smallest as `[arr[i], arr[j]]`, where `k` is one-based. Fractions are ranked as generated index pairs rather than simplified or replaced by decimal approximations.

### Function Contract

**Inputs**

- `arr`: a strictly increasing list containing `1` and prime numbers.
- `k`: a one-based rank between `1` and `len(arr) * (len(arr) - 1) / 2`.

**Return value**

- A two-element list `[numerator, denominator]` identifying the `k`-th fraction in increasing numeric order.

### Examples

**Example 1**

- Input: `arr = [1,2,3,5], k = 3`
- Output: `[2,5]`
- Explanation: The first fractions are $1/5$, $1/3$, and $2/5$.

**Example 2**

- Input: `arr = [1,7], k = 1`
- Output: `[1,7]`
- Explanation: Only one eligible pair exists.

**Example 3**

- Input: `arr = [1,2,3,5], k = 6`
- Output: `[2,3]`
- Explanation: This is the largest of the six eligible fractions.
