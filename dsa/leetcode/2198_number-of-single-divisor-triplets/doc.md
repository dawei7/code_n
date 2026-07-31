# Number of Single Divisor Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-single-divisor-triplets/) |

## Problem Description

### Goal

An ordered triplet of distinct indices $(i,j,k)$ is a single divisor triplet when the sum

$$
\texttt{nums[i]}+\texttt{nums[j]}+\texttt{nums[k]}
$$

is divisible by exactly one of the three selected values. Divisibility is tested against each selected position, so equal values in two different positions still contribute two successful divisibility tests.

Given the positive-integer array `nums`, count all ordered triplets of distinct indices that satisfy this condition. Different orders of the same three indices are separate triplets.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $3 \le n \le 10^5$ and every value lies in $[1,100]$.

Let $U$ be the number of distinct values in `nums`; the contract guarantees $U \le 100$.

**Return value**

Return the number of ordered single divisor triplets.

### Examples

**Example 1**

- Input: `nums = [4, 6, 7, 3, 2]`
- Output: `12`

The value multisets `{4,3,2}` and `{4,7,3}` each qualify. Every selection uses three distinct indices and contributes all six orders.

**Example 2**

- Input: `nums = [1, 2, 2]`
- Output: `6`

The sum is `5`, which is divisible only by the selected value `1`; all six orders of the three indices qualify.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `0`

The sum `3` is divisible by the value at all three selected positions, not exactly one.
