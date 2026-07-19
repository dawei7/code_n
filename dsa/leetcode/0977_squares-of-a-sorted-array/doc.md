# Squares of a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 977 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/squares-of-a-sorted-array/) |

## Problem Description

### Goal

An integer array `nums` is already sorted in non-decreasing order. Square every number and return the resulting values, also sorted in non-decreasing order.

Negative inputs require care because squaring reverses their magnitude order: a value farther below zero can produce a larger square than a later positive value. Preserve every occurrence, including duplicate values and duplicate squares, and produce an output with exactly the same length as the input. The requested solution should exploit the input ordering to run in linear time rather than sorting all squares again.

### Function Contract

**Inputs**

- `nums`: a non-decreasing list of $N$ integers, where $1 \le N \le 10^4$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- A list containing each value `nums[i] * nums[i]`, sorted in non-decreasing order.

### Examples

**Example 1**

- Input: `nums = [-4, -1, 0, 3, 10]`
- Output: `[0, 1, 9, 16, 100]`
- Explanation: direct squaring gives `[16, 1, 0, 9, 100]`; ordering those values gives the output.

**Example 2**

- Input: `nums = [-7, -3, 2, 3, 11]`
- Output: `[4, 9, 9, 49, 121]`
