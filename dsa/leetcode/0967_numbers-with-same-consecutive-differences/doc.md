# Numbers With Same Consecutive Differences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 967 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [numbers-with-same-consecutive-differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) |

## Problem Description

### Goal

Given integers `n` and `k`, generate every positive integer with exactly `n` decimal digits such that the absolute difference between each pair of consecutive digits is exactly `k`.

The first digit cannot be zero, because representations with leading zeroes do not count as `n`-digit integers. Zero may appear in later positions. Return all valid integers in any order, without duplicates.

### Function Contract

**Inputs**

- `n`: the required number of digits, where $2 \le n \le 9$.
- `k`: the required absolute difference, where $0 \le k \le 9$.
- Let $F_\ell$ be the number of valid length-$\ell$ prefixes generated from nonzero first digits, and define

$$
T = \sum_{\ell=1}^{n} F_\ell,
\qquad
F = \max_{1\le \ell\le n} F_\ell.
$$

**Return value**

Return all `n`-digit integers whose adjacent digits differ by exactly `k`; result order is unrestricted.

### Examples

**Example 1**

- Input: `n = 3, k = 7`
- Output: `[181,292,707,818,929]`
- Explanation: A leading-zero form such as `070` is not a three-digit integer and is excluded.

**Example 2**

- Input: `n = 2, k = 1`
- Output: `[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]`
