# Count Integers With Even Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2180 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-integers-with-even-digit-sum/) |

## Problem Description

### Goal

For a positive integer, its digit sum is obtained by adding all of its decimal
digits. For example, the digit sum of `241` is $2+4+1=7$.

Given a positive integer `num`, consider every positive integer from $1$
through `num`, including the upper endpoint. Count how many of those integers
have an even digit sum. This property depends on the sum of the digits, not on
whether the integer itself is even: for instance, `11` qualifies because its
digit sum is $2$, whereas `10` does not because its digit sum is $1$.

### Function Contract

**Inputs**

- `num`: a positive integer satisfying $1\le\texttt{num}\le1000$.

**Return value**

Return the number of positive integers at most `num` whose decimal digits sum
to an even integer.

### Examples

#### Example 1

- **Input:** `num = 4`
- **Output:** `2`
- **Explanation:** `2` and `4` have even digit sums.

#### Example 2

- **Input:** `num = 30`
- **Output:** `14`

#### Example 3

- **Input:** `num = 1`
- **Output:** `0`
