# Minimum Operations to Make All Array Elements Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2602 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers and an array `queries` containing $m$ target values. For one operation, you may increase or decrease any single element of `nums` by exactly $1$.

For each query `queries[i]`, determine the minimum number of operations needed to make every element of `nums` equal to that target. Each query is independent: after answering one query, `nums` is restored to its original values before the next query is considered.

Return an array `answer` of length $m$ in which `answer[i]` is the minimum cost for `queries[i]`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `queries`: A list of $m$ positive target integers.

The constraints are $1 \leq n, m \leq 10^5$ and $1 \leq \texttt{nums[i]}, \texttt{queries[i]} \leq 10^9$.

**Return value**

- A list of $m$ integers giving the minimum operation count for each query in its original order.

### Examples

**Example 1**

- Input: `nums = [3,1,6,8], queries = [1,5]`
- Output: `[14,10]`

Making every value equal to $1$ costs $2 + 0 + 5 + 7 = 14$. Making every value equal to $5$ costs $2 + 4 + 1 + 3 = 10$.

**Example 2**

- Input: `nums = [2,9,6,3], queries = [10]`
- Output: `[20]`

The required increases are $8$, $1$, $4$, and $7$, for a total of $20$.
