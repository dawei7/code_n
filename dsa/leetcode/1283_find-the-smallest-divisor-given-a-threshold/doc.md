# Find the Smallest Divisor Given a Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1283 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `threshold`, choose a positive integer divisor. Divide every array value by that divisor, round each individual quotient up to the nearest integer, and add the rounded quotients. For example, dividing $7$ by $3$ contributes $3$, while dividing $10$ by $2$ contributes $5$.

Find the smallest positive divisor for which this rounded-division sum is at most `threshold`. The input guarantees that at least one divisor satisfies the limit.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 5 \cdot 10^4$ and every value is at most $10^6$.
- `threshold`: an integer satisfying $n \le \texttt{threshold} \le 10^6$.
- Let $M = \max(\texttt{nums})$.

**Return value**

The smallest positive integer divisor $d$ such that

$$
\sum_{x \in \texttt{nums}} \left\lceil \frac{x}{d} \right\rceil \le \texttt{threshold}.
$$

### Examples
**Example 1**

- Input: `nums = [1,2,5,9]`, `threshold = 6`
- Output: `5`
- Explanation: Divisor $4$ produces $1+1+2+3=7$, but divisor $5$ produces $1+1+1+2=5$.

**Example 2**

- Input: `nums = [44,22,33,11,1]`, `threshold = 5`
- Output: `44`
- Explanation: With a threshold equal to the array length, every rounded quotient must be one.

**Example 3**

- Input: `nums = [21212,10101,12121]`, `threshold = 1000000`
- Output: `1`
