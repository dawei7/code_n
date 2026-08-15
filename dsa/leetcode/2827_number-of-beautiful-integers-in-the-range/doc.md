# Number of Beautiful Integers in the Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2827 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/) |

## Problem Description

### Goal

You are given positive integers `low`, `high`, and `k`. Consider every integer in the inclusive range from `low` through `high`.

An integer is beautiful only when it satisfies both conditions: its decimal representation contains equally many even and odd digits, and the integer is divisible by `k`. The digit `0` is even, and leading zeros are not part of an integer's decimal representation.

Return the number of beautiful integers in the range. Each endpoint is included when it satisfies both requirements.

### Function Contract

**Inputs**

- `low`: The positive lower endpoint, where $1 \le \texttt{low} \le \texttt{high}$.
- `high`: The positive upper endpoint, where $\texttt{high} \le 10^9$.
- `k`: A positive divisor, where $1 \le k \le 20$.

**Return value**

Return the count of integers $x$ such that $\texttt{low} \le x \le \texttt{high}$, $x$ is divisible by `k`, and its decimal digits contain the same number of even and odd values.

### Examples

#### Example 1

- **Input:** `low = 10, high = 20, k = 3`
- **Output:** `2`
- **Explanation:** `12` and `18` are divisible by `3`, and each has one even digit and one odd digit.

#### Example 2

- **Input:** `low = 1, high = 10, k = 1`
- **Output:** `1`
- **Explanation:** `10` is the only integer in the range with equal counts of even and odd digits.

#### Example 3

- **Input:** `low = 5, high = 5, k = 2`
- **Output:** `0`
- **Explanation:** The only integer in the range is not divisible by `2` and does not balance even and odd digits.
