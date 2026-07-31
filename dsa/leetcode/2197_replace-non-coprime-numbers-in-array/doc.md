# Replace Non-Coprime Numbers in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2197 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/) |

## Problem Description

### Goal

Given an integer array `nums`, repeatedly choose any adjacent pair whose greatest common divisor is greater than $1$. Remove those two values and put their least common multiple in their place.

Continue until every neighboring pair is coprime, then return the remaining array. The choice of eligible pair does not affect the final result.

Two values $x$ and $y$ are non-coprime exactly when $\gcd(x,y) > 1$. Every value in the final array is guaranteed to be at most $10^8$.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers.

The bounds are $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$. Let $V$ denote the largest value involved in a greatest-common-divisor computation.

**Return value**

Return the unique array obtained after no adjacent non-coprime pair remains.

### Examples

**Example 1**

- Input: `nums = [6, 4, 3, 2, 7, 6, 2]`
- Output: `[12, 7, 6]`

The first four values can merge into `12`, while the final `6` and `2` merge into `6`.

**Example 2**

- Input: `nums = [2, 2, 1, 1, 3, 3, 3]`
- Output: `[2, 1, 1, 3]`

Equal adjacent `2` values collapse to one `2`, and the three adjacent `3` values collapse to one `3`. Values equal to `1` cannot merge with a neighbor.
