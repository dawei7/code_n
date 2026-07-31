# Minimizing Array After Replacing Pairs With Their Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2892 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. In one operation, choose two adjacent values $x$ and $y$ whose product satisfies $xy \le k$. Remove both values and insert the single value $xy$ in their position, reducing the array length by one. The new product can participate in later operations with either adjacent neighbor.

Perform this operation any number of times, including zero times. Return the smallest array length that can be reached while respecting the product limit at every merge.

### Function Contract

**Inputs**

- `nums`: A non-empty list of integers; each value is between $0$ and $10^9$, inclusive.
- `k`: An integer between $1$ and $10^9$, inclusive; every selected adjacent product must be at most `k`.

Let $n = \lvert\texttt{nums}\rvert$, where $1 \le n \le 10^5$.

**Return value**

Return the minimum possible length of `nums` after any legal sequence of adjacent-product replacements.

### Examples

**Example 1**

- Input: `nums = [2, 3, 3, 7, 3, 5], k = 20`
- Output: `3`
- Explanation: Merge the first three values into `18` and the final two values into `15`, producing `[18, 7, 15]`.

**Example 2**

- Input: `nums = [3, 3, 3, 3], k = 6`
- Output: `4`
- Explanation: Every adjacent product is `9`, so no operation is legal.

**Example 3**

- Input: `nums = [1000000000, 2, 0, 1000000000], k = 1`
- Output: `1`
- Explanation: Merge the zero with an adjacent value; the product remains zero and can continue absorbing every remaining neighbor.
