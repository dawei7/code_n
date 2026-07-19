# GCD Sort of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1998 |
| Difficulty | Hard |
| Topics | Array, Math, Union-Find, Sorting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/gcd-sort-of-an-array/) |

## Problem Description

### Goal

Given an integer array `nums`, an operation may choose any two positions $i$ and $j$ and swap their current elements when

$$
\gcd(\texttt{nums[i]},\texttt{nums[j]})>1.
$$

The operation may be performed any number of times, and later swaps may use values moved by earlier ones. Determine whether some sequence of legal swaps can place the array in non-decreasing order.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $1 \le N \le 3\cdot10^4$.
- Every value is between $2$ and $10^5$ inclusive.
- Let $M=\max(\texttt{nums})$.

**Return value**

Return `true` if legal greatest-common-divisor swaps can sort the array in non-decreasing order; otherwise, return `false`.

### Examples

**Example 1**

- Input: `nums = [7, 21, 3]`
- Output: `true`
- Explanation: Swap `7` with `21`, then `21` with `3`; the respective greatest common divisors are $7$ and $3$.

**Example 2**

- Input: `nums = [5, 2, 6, 2]`
- Output: `false`
- Explanation: The value `5` shares no factor greater than one with another value and cannot leave its incorrect position.

**Example 3**

- Input: `nums = [10, 5, 9, 3, 15]`
- Output: `true`
- Explanation: Shared factors connect the values through $3$ and $5$, permitting the needed rearrangement.
