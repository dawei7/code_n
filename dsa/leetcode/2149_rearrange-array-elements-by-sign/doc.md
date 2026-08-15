# Rearrange Array Elements by Sign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2149 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [rearrange-array-elements-by-sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` of even length containing no
zeros. It has the same number of positive and negative integers.

Rearrange all elements so that adjacent values always have opposite signs and
the first value is positive. Among the positive values, preserve their original
relative order; preserve the original relative order of the negative values as
well. Return the resulting array. The input does not need to be modified
in-place.

### Function Contract

**Inputs**

- `nums`: An even-length integer array of length $n$, where
  $2 \leq n \leq 2 \cdot 10^5$, $1 \leq \lvert\texttt{nums[i]}\rvert \leq
  10^5$, and positive and negative values occur equally often.

**Return value**

Return all input elements with positives at even indices, negatives at odd
indices, and the relative order within each sign unchanged.

### Examples

#### Example 1

- **Input:** `nums = [3, 1, -2, -5, 2, -4]`
- **Output:** `[3, -2, 1, -5, 2, -4]`
- **Explanation:** The positive subsequence `[3, 1, 2]` and negative subsequence
  `[-2, -5, -4]` are interleaved without changing either order.

#### Example 2

- **Input:** `nums = [-1, 1]`
- **Output:** `[1, -1]`
- **Explanation:** The only positive value must precede the only negative value.
