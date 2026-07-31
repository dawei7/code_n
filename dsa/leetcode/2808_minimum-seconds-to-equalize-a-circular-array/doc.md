# Minimum Seconds to Equalize a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2808 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/) |

## Problem Description

### Goal

You are given a 0-indexed circular array `nums`. During each second, every index simultaneously chooses its replacement value from one of three values present at the start of that second: its own value, the value immediately to its left, or the value immediately to its right. The first and last indices are neighbors because the array is circular.

Return the minimum number of seconds required to make every array element equal. All positions update simultaneously, so a value can spread by at most one edge in each direction per second. The final common value must be one that already occurs in the input, and the operation need not be performed when all values are initially equal.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^9$.

**Return value**

Return the smallest integer number of simultaneous-update seconds needed to make the circular array constant.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1, 2]`
- Output: `1`
- Explanation: Either alternating value can spread to its two neighboring positions in one second.

**Example 2**

- Input: `nums = [2, 1, 3, 3, 2]`
- Output: `2`
- Explanation: Choosing `3` as the final value requires two seconds to cover the longest circular gap between its occurrences.

**Example 3**

- Input: `nums = [5, 5, 5, 5]`
- Output: `0`
- Explanation: Every position already contains the same value.
