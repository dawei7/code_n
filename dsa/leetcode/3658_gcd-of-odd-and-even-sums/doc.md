# GCD of Odd and Even Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3658 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Number Theory |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/) |

## Problem Description

### Goal

Given a positive integer `n`, consider two finite sequences. The first contains the smallest `n` positive odd integers, and the second contains the smallest `n` positive even integers.

Let `sumOdd` be the sum of the odd sequence and `sumEven` the sum of the even sequence. Both sequences contain exactly `n` terms, with no skipped positive value of the corresponding parity. Return the greatest common divisor of these two sums.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1\le n\le 1000$.

**Return value**

Return the integer $\gcd(\texttt{sumOdd},\texttt{sumEven})$.

### Examples

#### Example 1

- **Input:** `n = 4`
- Odd sum: `1 + 3 + 5 + 7 = 16`
- Even sum: `2 + 4 + 6 + 8 = 20`
- **Output:** `4`

#### Example 2

- **Input:** `n = 5`
- Odd sum: `1 + 3 + 5 + 7 + 9 = 25`
- Even sum: `2 + 4 + 6 + 8 + 10 = 30`
- **Output:** `5`

#### Example 3

- **Input:** `n = 1`
- The sums are `1` and `2`, whose greatest common divisor is `1`.
- **Output:** `1`
