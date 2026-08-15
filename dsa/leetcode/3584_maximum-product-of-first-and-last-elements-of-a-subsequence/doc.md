# Maximum Product of First and Last Elements of a Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3584 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `m`, choose a subsequence containing exactly `m` elements. A subsequence retains the selected elements' original relative order but does not need to occupy consecutive positions.

For every eligible subsequence, multiply its first selected element by its last selected element. Return the maximum product obtainable. When `m = 1`, the first and last elements are the same selected value, so that subsequence contributes the value's square.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le10^5$ and $-10^5\le\texttt{nums[i]}\le10^5$.
- `m`: The exact subsequence length, where $1\le m\le n$.

**Return value**

Return the largest possible product of the first and last elements among all length-`m` subsequences.

### Examples

#### Example 1

- **Input:** `nums = [-1, -9, 2, 3, -2, -3, 1], m = 1`
- **Output:** `81`
- **Explanation:** Selecting only `-9` makes both endpoints `-9`, whose product is 81.

#### Example 2

- **Input:** `nums = [1, 3, -5, 5, 6, -4], m = 3`
- **Output:** `20`
- **Explanation:** The subsequence `[-5, 6, -4]` has endpoint product 20.

#### Example 3

- **Input:** `nums = [2, -1, 2, -6, 5, 2, -5, 7], m = 2`
- **Output:** `35`
- **Explanation:** The subsequence `[5, 7]` has endpoint product 35.

---
