# Sum of Values at Indices With K Set Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2859 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. Add the values whose array indices contain exactly `k` set bits in their binary representations, and return the resulting sum.

A set bit is a binary digit equal to `1`. For example, $21$ is written as `10101` in binary and therefore has three set bits. The condition applies to each index, not to the value stored at that index.

### Function Contract

**Inputs**

- `nums`: The integer array whose selected values are summed.
- `k`: The required number of set bits in an index.

Let $n = \lvert\texttt{nums}\rvert$. The constraints guarantee $1 \le n \le 1000$, $1 \le \texttt{nums[i]} \le 10^5$, and $0 \le \texttt{k} \le 10$.

**Return value**

The sum of every `nums[i]` for which the binary representation of `i` contains exactly `k` ones.

### Examples

#### Example 1

- **Input:** `nums = [5, 10, 1, 5, 2], k = 1`
- **Output:** `13`

Indices `1`, `2`, and `4` each have one set bit, so the sum is `10 + 1 + 2`.

#### Example 2

- **Input:** `nums = [4, 3, 2, 1], k = 2`
- **Output:** `1`

Only index `3`, whose binary form is `11`, has two set bits.

#### Example 3

- **Input:** `nums = [10, 20, 30], k = 0`
- **Output:** `10`

Index `0` is the only nonnegative index with zero set bits.
