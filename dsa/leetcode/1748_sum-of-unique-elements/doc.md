# Sum of Unique Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1748 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-unique-elements/) |

## Problem Description

### Goal

You are given an integer array `nums`. A value is called unique when it appears exactly once in the entire array; distinct values that occur two or more times are not unique, regardless of how far apart their occurrences are.

Return the sum of all unique values. Each qualifying value contributes itself once, while every repeated value contributes nothing. If the array has no unique values, return zero. The array is nonempty, and both its length and every element are between $1$ and $100$, inclusive.

### Function Contract

**Inputs**

- `nums`: a nonempty list of integers, where $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

- Return the sum of exactly those values whose total frequency in `nums` is one.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 2]`
- Output: `4`
- Explanation: Only `1` and `3` appear exactly once, so their sum is `4`.

**Example 2**

- Input: `nums = [1, 1, 1, 1, 1]`
- Output: `0`
- Explanation: No value occurs exactly once.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `15`
- Explanation: Every value is unique, so all five values contribute.
