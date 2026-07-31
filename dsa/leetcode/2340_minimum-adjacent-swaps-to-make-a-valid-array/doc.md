# Minimum Adjacent Swaps to Make a Valid Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2340 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/) |

## Problem Description

### Goal

You may repeatedly swap two adjacent elements of an integer array. An array is valid when a smallest element occupies its leftmost position and a largest element occupies its rightmost position. If either extreme value occurs more than once, any one of its occurrences may serve as the endpoint.

Return the minimum number of adjacent swaps needed to reach a valid arrangement. Elements between the chosen extremes do not otherwise need to be sorted, and their relative order matters only through the swaps used to move the two selected values.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.

The length $n$ and every value are between $1$ and $10^5$.

**Return value**

Return the smallest number of adjacent swaps that places a minimum value first and a maximum value last.

### Examples

**Example 1**

- Input: `nums = [3,4,5,5,3,1]`
- Output: `6`

Use the rightmost `5`, move it two steps right, and move `1` five steps left. The two chosen elements cross once, so that crossing contributes to both movements and the total is $2+5-1=6$.

**Example 2**

- Input: `nums = [9]`
- Output: `0`

The only element is simultaneously a minimum and maximum and is already at both endpoints.
