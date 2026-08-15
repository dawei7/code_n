# Find the Sum of Subsequence Powers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3098 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-sum-of-subsequence-powers](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$ and a positive integer `k`. The power of a subsequence is the minimum absolute difference between any two of its elements.

Consider every subsequence of `nums` whose length is exactly `k`. Sum the power of each such subsequence and return the result modulo $10^9 + 7$. Equal values chosen from different indices still describe distinct index subsequences, even though any subsequence containing both has power zero.

### Function Contract

**Inputs**

- `nums`: An integer list of length $n$, where $2 \le n \le 50$ and $-10^8 \le \texttt{nums[i]} \le 10^8$.
- `k`: The exact number of elements chosen for each subsequence, where $2 \le k \le n$.

**Return value**

- The sum of the powers of all length-`k` subsequences, reduced modulo $10^9 + 7$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4], k = 3`
- **Output:** `4`
- **Explanation:** The four length-three subsequences have powers $1$, $1$, $1$, and $1$, so their sum is $4$.

#### Example 2

- **Input:** `nums = [2, 2], k = 2`
- **Output:** `0`
- **Explanation:** The only subsequence contains two equal values, making its minimum absolute difference zero.

#### Example 3

- **Input:** `nums = [4, 3, -1], k = 2`
- **Output:** `10`
- **Explanation:** The three pair powers are $\lvert 4 - 3 \rvert = 1$, $\lvert 4 - (-1) \rvert = 5$, and $\lvert 3 - (-1) \rvert = 4$.
