# Identify the Largest Outlier in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3371 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/) |

## Problem Description

### Goal

An integer array of length $n$ contains exactly $n-2$ special numbers. Of the two remaining positions, one stores the sum of all special numbers and the other stores an outlier. The outlier is neither one of the chosen special-number positions nor the position chosen as their sum.

These roles must use distinct indices, although two or more roles may hold equal numeric values. More than one assignment of roles may satisfy the array. Considering every valid assignment, return the largest value that can occupy the outlier position. The input guarantees that at least one valid potential outlier exists.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3\leq n\leq10^5$ and $-1000\leq\texttt{nums[i]}\leq1000$.

**Return value**

- The largest value that can be the outlier in a valid assignment of distinct indices.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, 5, 10]`
- **Output:** `10`
- **Explanation:** `2` and `3` are special, `5` is their sum, and `10` is the outlier.

#### Example 2

- **Input:** `nums = [-2, -1, -3, -6, 4]`
- **Output:** `4`
- **Explanation:** The three negative special numbers sum to `-6`, leaving `4` as the outlier.

#### Example 3

- **Input:** `nums = [1, 1, 1, 1, 1, 5, 5]`
- **Output:** `5`
- **Explanation:** Five special ones sum to one copy of `5`; the other copy of `5` is the outlier.
