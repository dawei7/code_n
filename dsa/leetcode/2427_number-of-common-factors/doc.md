# Number of Common Factors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2427 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Common Factors](https://leetcode.com/problems/number-of-common-factors/) |

## Problem Description

### Goal

You are given two positive integers `a` and `b`. A positive integer is a common factor when it divides both inputs without leaving a remainder. Each qualifying value is counted once, and only positive divisors are considered.

Return how many distinct positive integers are common factors of the two values. The factors include 1 and may include either input when the two numbers are equal.

### Function Contract

**Inputs**

- `a`: A positive integer from 1 through 1000.
- `b`: A positive integer from 1 through 1000.

Let $g=\gcd(a,b)$. The common factors of `a` and `b` are exactly the positive divisors of $g$.

**Return value**

- The number of positive integers that divide both `a` and `b`.

### Examples

**Example 1**

- Input: `a = 12, b = 6`
- Output: `4`

The common factors are 1, 2, 3, and 6.

**Example 2**

- Input: `a = 25, b = 30`
- Output: `2`

Only 1 and 5 divide both values.

**Example 3**

- Input: `a = 17, b = 19`
- Output: `1`

The two primes are coprime, so their only common factor is 1.
