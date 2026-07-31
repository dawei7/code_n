# Subarrays Distinct Element Sum of Squares I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2913 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/) |

## Problem Description

### Goal

For every contiguous non-empty subarray of the zero-indexed integer array
`nums`, determine its distinct count: the number of different values appearing
between its chosen left and right endpoints, inclusive. Equal values contribute
only once to that particular subarray's count, even when they occur at several
positions.

Square the distinct count of each possible subarray and add all of those
squares. Return this total over the complete set of endpoint pairs
$0\le i\le j<n$. Subarrays with the same sequence of values but different
positions are separate choices and must each contribute to the sum.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le 100$ and $1\le\texttt{nums[i]}\le 100$.

**Return value**

Return the sum of the squared distinct counts of all non-empty contiguous
subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `15`
- Explanation: The three singleton subarrays contribute $1$ each, while `[1, 2]`, `[2, 1]`, and `[1, 2, 1]` each have two distinct values and contribute $4$.

**Example 2**

- Input: `nums = [1, 1]`
- Output: `3`
- Explanation: Both singletons and the length-two subarray have distinct count one.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `20`
- Explanation: The three length-one, two length-two, and one length-three subarrays contribute $3\cdot1^2+2\cdot2^2+1\cdot3^2=20$.
