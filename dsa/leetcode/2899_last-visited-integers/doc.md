# Last Visited Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2899 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/last-visited-integers/) |

## Problem Description

### Goal

You are given an integer array `nums`. Every element is either a positive integer or `-1`. Process the array from left to right while maintaining the positive integers encountered so far, ordered from most recently seen to least recently seen.

When a positive integer appears, it becomes the most recently seen integer. When `-1` appears, let $k$ be the length of the current consecutive run of `-1` values, including this one. Append the $k$-th most recently seen positive integer to the answer if it exists; otherwise append `-1`. Encountering a positive integer ends the current run, so the next `-1` starts again with $k=1$.

Return the answers produced for all `-1` entries in their original order.

### Function Contract

**Inputs**

- `nums`: A nonempty array whose elements are positive integers or `-1` query markers.

The shared bounds are $1\le\lvert\texttt{nums}\rvert\le100$. Every positive entry is at most $100$.

**Return value**

Return one integer for each `-1` in `nums`: the requested previously seen value, or `-1` when that history position does not exist.

### Examples

**Example 1**

- Input: `nums = [1, 2, -1, -1, -1]`
- Output: `[2, 1, -1]`
- Explanation: The three queries ask for the first, second, and third most recent values. Only `2` and `1` have been seen.

**Example 2**

- Input: `nums = [1, -1, 2, -1, -1]`
- Output: `[1, 2, 1]`
- Explanation: Reading `2` resets the consecutive-query count, so the following two queries request the first and second most recent values.
