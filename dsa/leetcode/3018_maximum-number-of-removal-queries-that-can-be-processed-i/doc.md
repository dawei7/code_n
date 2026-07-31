# Maximum Number of Removal Queries That Can Be Processed I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3018 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/) |

## Problem Description

### Goal

You are given 0-indexed integer arrays `nums` and `queries`. Before processing any query, you may perform at most one preparation step: replace `nums` by any subsequence of itself. The chosen values keep their original relative order.

Queries must then be processed from left to right. For the current query value, inspect the first and last values of the remaining `nums`. If both are smaller than the query, processing stops. Otherwise, choose a qualifying end whose value is at least the query, remove that value, and advance to the next query.

Choose the optional subsequence and every end removal to maximize how many initial queries are processed. Return that maximum count.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers from which an initial subsequence may be selected.
- `queries`: A nonempty list of positive query thresholds that must be handled in order.

The source constraints guarantee $1 \le \lvert\texttt{nums}\rvert,\lvert\texttt{queries}\rvert \le 1000$ and values between $1$ and $10^9$.

**Return value**

- The maximum number of queries from the beginning of `queries` that can be processed.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`, `queries = [1, 2, 3, 4, 6]`
- Output: `4`
- Explanation: Keep the full array and remove `1`, `2`, `3`, then `4` from the front. The remaining value cannot meet query `6`.

**Example 2**

- Input: `nums = [2, 3, 2]`, `queries = [2, 2, 3]`
- Output: `3`
- Explanation: Remove the left `2`, the right `2`, and finally `3`.

**Example 3**

- Input: `nums = [3, 4, 3]`, `queries = [4, 3, 2]`
- Output: `2`
- Explanation: Choose subsequence `[4, 3]`, then remove its two values from the front. No value remains for the third query.
