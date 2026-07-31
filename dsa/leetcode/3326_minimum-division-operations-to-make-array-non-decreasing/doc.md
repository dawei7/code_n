# Minimum Division Operations to Make Array Non Decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3326 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/) |

## Problem Description

### Goal

You are given an integer array `nums`. A positive divisor of a natural number $x$ is a proper divisor when it is strictly less than $x$. In one operation, choose one array element and divide it by its greatest proper divisor. An element may be selected any number of times.

Find the minimum number of operations needed to make `nums` non-decreasing, meaning every element is at most the element immediately after it. Return `-1` when no sequence of allowed operations can produce such an ordering. Dividing a composite number this way leaves its smallest prime factor, whereas applying the operation to a prime divides it by $1$ and does not change it.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.

The constraints are $1\leq n\leq10^5$ and $1\leq\texttt{nums[i]}\leq10^6$.

**Return value**

Return the minimum number of allowed divisions that makes `nums` non-decreasing, or `-1` if that is impossible.

### Examples

**Example 1**

- Input: `nums = [25, 7]`
- Output: `1`
- Explanation: The greatest proper divisor of $25$ is $5$. Dividing produces $5$, so the array becomes `[5, 7]`.

**Example 2**

- Input: `nums = [7, 7, 6]`
- Output: `-1`
- Explanation: The middle $7$ exceeds $6$, but $7$ is prime and the operation cannot reduce it.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `0`
- Explanation: The array is already non-decreasing.
