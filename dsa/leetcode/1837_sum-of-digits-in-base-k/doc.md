# Sum of Digits in Base K

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sum-of-digits-in-base-k/) |
| Frontend ID | 1837 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a positive integer `n` written as an ordinary base-10 value and a target base `k`. Convert the value of `n` to its base-$k$ digit representation.

The standard base-$k$ representation uses digits from 0 through $k-1$ and has no leading zeros. Interpret each resulting digit as a base-10 integer, add those digits, and return the sum as a base-10 integer. The representation itself does not need to be returned or stored.

### Function Contract

**Inputs**

- `n`: a positive base-10 integer, where $1 \le n \le 100$.
- `k`: the target base, where $2 \le k \le 10$.

**Return value**

- Return the sum of the digits in the standard base-$k$ representation of `n`.

### Examples

**Example 1**

- Input: `n = 34, k = 6`
- Output: `9`

The base-6 representation is `54`, and $5+4=9$.

**Example 2**

- Input: `n = 10, k = 10`
- Output: `1`

The representation remains `10`, whose digits sum to 1.

**Example 3**

- Input: `n = 8, k = 2`
- Output: `1`

The binary representation is `1000`.
