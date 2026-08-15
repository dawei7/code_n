# Partition Array into Two Equal Product Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3566 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Recursion, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/) |

## Problem Description

### Goal

Given an array of distinct positive integers, divide all of its elements between two subsets. The subsets must be disjoint, neither may be empty, and every original element must belong to exactly one of them.

Determine whether the product of the values in each subset can equal `target`. Both subsets must reach that same prescribed product; merely having equal products with a different value does not qualify.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct positive integers, where $3\le n\le12$ and every value is at most 100.
- `target`: The required product of each subset, with $1\le\texttt{target}\le10^{15}$.

**Return value**

Return `true` when all elements can be partitioned into two nonempty subsets whose products both equal `target`; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [3,1,6,8,4], target = 24`
- **Output:** `true`
- **Explanation:** `[3,8]` and `[1,6,4]` are disjoint, cover the array, and both have product 24.

#### Example 2

- **Input:** `nums = [2,5,3,7], target = 15`
- **Output:** `false`
- **Explanation:** No complete two-way partition gives both subsets product 15.

---
