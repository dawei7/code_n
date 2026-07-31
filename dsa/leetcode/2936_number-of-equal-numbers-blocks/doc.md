# Number of Equal Numbers Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2936 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-equal-numbers-blocks/) |

## Problem Description

### Goal

A very large 0-indexed integer array `nums` has the property that every value's
occurrences are adjacent. Equivalently, each distinct value appears in one
contiguous run and can never reappear after a different value. Partition the
array into maximal blocks of equal numbers and return the number of blocks.

The source-native input is a `BigArray`, not a materialized array. Its
`size()` method returns the length and `at(index)` returns one value. The array
may contain up to $10^{15}$ elements, so the solution must locate block
boundaries with a small number of queries rather than inspect every index.

### Function Contract

**Inputs**

- `nums`: A read-only `BigArray` supporting `size()` and zero-indexed `at(index)` access. The app adapter receives the equivalent serialized integer list.

Let $n=\texttt{nums.size()}$ and let $b$ be the number of maximal equal-value
blocks. The constraints are $1\le n\le10^{15}$ and
$1\le\texttt{nums.at(i)}\le10^9$. All occurrences of each value are adjacent.

**Return value**

- The number $b$ of maximal contiguous blocks containing equal values.

### Examples

**Example 1**

- Input: `nums = [3, 3, 3, 3, 3]`
- Output: `1`
- Explanation: The whole array is one maximal equal-value block.

**Example 2**

- Input: `nums = [1, 1, 1, 3, 9, 9, 9, 2, 10, 10]`
- Output: `5`
- Explanation: The block values in order are 1, 3, 9, 2, and 10.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 6, 7]`
- Output: `7`
- Explanation: Every element has a different value, so each is its own block.
