# Length of Longest Fibonacci Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 873 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) |

## Problem Description
### Goal
A sequence $x_1,x_2,\ldots,x_m$ is Fibonacci-like when it contains at least three values and every value after the first two is the sum of its two predecessors:

$$
x_i+x_{i+1}=x_{i+2}
$$

for every applicable index.

Given a strictly increasing array `arr` of positive integers, find the length of its longest Fibonacci-like subsequence. A subsequence may delete any number of elements while retaining the original order of those that remain. Return `0` when no Fibonacci-like subsequence of length at least three exists.

### Function Contract
**Inputs**

- `arr`: a strictly increasing array of $n$ positive integers, where $3 \leq n \leq 1000$ and $1 \leq \texttt{arr[i]} < \texttt{arr[i + 1]} \leq 10^9$.

**Return value**

Return the maximum length of a Fibonacci-like subsequence of `arr`, or `0` if there is no such subsequence.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5,6,7,8]`
- Output: `5`

One longest Fibonacci-like subsequence is `[1,2,3,5,8]`.

**Example 2**

- Input: `arr = [1,3,7,11,12,14,18]`
- Output: `3`

Examples of maximum-length choices include `[1,11,12]`, `[3,11,14]`, and `[7,11,18]`.

**Example 3**

- Input: `arr = [1,4,10]`
- Output: `0`

The only length-three subsequence does not satisfy the required sum.
