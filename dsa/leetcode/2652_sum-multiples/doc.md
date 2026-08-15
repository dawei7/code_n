# Sum Multiples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2652 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-multiples/) |

## Problem Description

### Goal

Given a positive integer `n`, consider every integer from $1$ through $n$, including both endpoints. Select a number when it is divisible by at least one of $3$, $5$, or $7$. A number divisible by several of these divisors still appears only once in the selected set.

Return the sum of all selected integers. Values that are divisible by none of the three specified numbers contribute nothing, and the inclusive upper endpoint contributes whenever it satisfies at least one divisibility condition.

### Function Contract

**Inputs**

- `n`: The inclusive upper bound, where $1 \le n \le 1000$.

**Return value**

- Return the sum of the integers in $[1,n]$ divisible by $3$, $5$, or $7$.

### Examples

#### Example 1

- **Input:** `n = 7`
- **Output:** `21`
- **Explanation:** The selected values are `3`, `5`, `6`, and `7`.

#### Example 2

- **Input:** `n = 10`
- **Output:** `40`
- **Explanation:** The selected values are `3`, `5`, `6`, `7`, `9`, and `10`.

#### Example 3

- **Input:** `n = 9`
- **Output:** `30`
- **Explanation:** The selected values are `3`, `5`, `6`, `7`, and `9`.
