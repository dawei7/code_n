# Count Nice Pairs in an Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-nice-pairs-in-an-array/) |
| Frontend ID | 1814 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For a non-negative integer $x$, let `rev(x)` be the integer formed by reversing its decimal digits. Leading zeros in the reversed text disappear from the resulting integer, so `rev(123) = 321` and `rev(120) = 21`.

Given the non-negative integer array `nums`, an index pair `(i, j)` is nice when $0 \le i < j < n$ and `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`. Count all nice index pairs. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: a list of length $n$, where $1 \le n \le 10^5$ and every value is from $0$ through $10^9$.
- Let

$$
D = \sum_{x \in \texttt{nums}} \max(1,\text{digits}(x))
$$

be the total number of decimal digits processed.

**Return value**

- Return the number of pairs `(i, j)` satisfying the nice-pair equality and $i<j$.
- Return the count modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [42,11,1,97]`
- Output: `2`

The nice pairs are `(0,3)` and `(1,2)`.

**Example 2**

- Input: `nums = [13,10,35,24,76]`
- Output: `4`

Four pairs share equal values of `x - rev(x)`.

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `3`

All three index pairs are nice, even though their values are equal.
