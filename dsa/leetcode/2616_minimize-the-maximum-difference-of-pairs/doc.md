# Minimize the Maximum Difference of Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2616 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `p`. Select exactly `p` pairs of indices. No index may appear in more than one selected pair.

The difference of a pair $(i,j)$ is $\lvert \texttt{nums}[i]-\texttt{nums}[j]\rvert$. Among the selected pairs, consider the largest such difference. Choose the pairs so this maximum is as small as possible, and return that minimum value.

When `p == 0`, no pairs are selected and the maximum of the empty set is defined to be $0$.

### Function Contract

**Inputs**

Let $n$ be the array length.

- `nums`: An integer array with $1 \leq n \leq 10^5$ and $0 \leq \texttt{nums}[i] \leq 10^9$.
- `p`: The exact number of disjoint index pairs to form, where $0 \leq p \leq \lfloor n/2\rfloor$.

**Return value**

Return the smallest possible maximum absolute difference among the `p` selected pairs.

### Examples

**Example 1**

- Input: `nums = [10, 1, 2, 7, 1, 3], p = 2`
- Output: `1`
- Explanation: Pair the two values $1$, and pair $2$ with $3$. Their differences are $0$ and $1$.

**Example 2**

- Input: `nums = [4, 2, 1, 2], p = 1`
- Output: `0`
- Explanation: The two occurrences of $2$ form a pair with difference zero.

**Example 3**

- Input: `nums = [8, 1, 5], p = 0`
- Output: `0`
- Explanation: The required set of pairs is empty.
