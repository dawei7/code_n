# Power of Heroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2681 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/power-of-heroes/) |

## Problem Description

### Goal

An integer array `nums` gives the strengths of a collection of heroes. Any non-empty group is formed by choosing a non-empty subset of array indices, so equal strengths at different indices still represent distinct choices.

The power of a group is the square of its greatest strength multiplied by its least strength. Sum this power over every possible non-empty group and return the result modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ hero strengths, where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^9$.

**Return value**

Return the sum of $\max(G)^2 \min(G)$ over every non-empty index subset $G$, reduced modulo $10^9 + 7$.

### Examples

#### Example 1

- **Input:** `nums = [2,1,4]`
- **Output:** `141`
- **Explanation:** The seven non-empty groups contribute 8, 1, 64, 4, 32, 16, and 16.

#### Example 2

- **Input:** `nums = [1,1,1]`
- **Output:** `7`
- **Explanation:** There are seven non-empty index subsets, and every one has power 1.
