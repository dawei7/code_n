# Minimize the Maximum Adjacent Element Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3357 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/) |

## Problem Description

### Goal

An integer array contains known positive values and missing positions marked by `-1`. Choose one pair of positive integers $(x,y)$ exactly once for the entire array. Replace every missing position with either $x$ or $y$; different positions may choose different members of the pair, and the two chosen integers are allowed to be equal.

After all replacements, inspect the absolute difference between every pair of adjacent elements. Minimize the largest of those differences and return that minimum possible value. The pair is global: a replacement value chosen for one missing run must still be one of the same two values available to every other missing run.

### Function Contract

**Inputs**

- `nums`: A list of known positive integers and `-1` placeholders.

The array length $n$ satisfies $2\le n\le 10^5$. Every entry is either `-1` or an integer in $[1,10^9]$.

**Return value**

- The smallest achievable maximum absolute difference between adjacent values after replacing every `-1` with one of the two globally chosen positive integers.

### Examples

**Example 1**

- Input: `nums = [1, 2, -1, 10, 8]`
- Output: `4`
- Explanation: Choose $(6,7)$ and replace the missing value with $6$. The completed array is `[1, 2, 6, 10, 8]`, whose adjacent differences are $1$, $4$, $4$, and $2$.

**Example 2**

- Input: `nums = [-1, -1, -1]`
- Output: `0`
- Explanation: Choose equal positive integers, such as $(4,4)$, and give every position the same value.

**Example 3**

- Input: `nums = [-1, 10, -1, 8]`
- Output: `1`
- Explanation: With $(11,9)$, the completed array can be `[11, 10, 9, 8]`, so every adjacent difference is $1$.
