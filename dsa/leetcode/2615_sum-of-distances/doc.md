# Sum of Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2615 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-distances/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. Construct an array `arr` of the same length.

For every index $i$, consider each other index $j$ such that `nums[j] == nums[i]`. Set `arr[i]` to the sum of the index distances $\lvert i-j\rvert$ over all such $j$. When the value at $i$ occurs nowhere else, its sum is $0$.

Return the completed array `arr`.

### Function Contract

**Inputs**

Let $n$ be the length of the input.

- `nums`: An integer array with $1 \leq n \leq 10^5$ and $0 \leq \texttt{nums}[i] \leq 10^9$.

**Return value**

Return an integer array `arr` of length $n$, where

$$
\texttt{arr}[i]
=
\sum_{\substack{0 \leq j < n \\ j \neq i \\ \texttt{nums}[j]=\texttt{nums}[i]}}
\lvert i-j\rvert.
$$

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 1, 1, 2]`
- **Output:** `[5, 0, 3, 4, 0]`
- **Explanation:** Value $1$ appears at indices $0,2,3$. Their respective distance sums are $5,3,4$; the other values occur once.

#### Example 2

- **Input:** `nums = [0, 5, 3]`
- **Output:** `[0, 0, 0]`
- **Explanation:** Every value is unique, so every distance sum is zero.

#### Example 3

- **Input:** `nums = [1, 1, 1]`
- **Output:** `[3, 2, 3]`
- **Explanation:** Each position sums its distances to the other two indices.
