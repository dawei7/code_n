# Form Array by Concatenating Subarrays of Another Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/) |

## Problem Description

### Goal

You are given an ordered list of integer arrays called `groups` and a separate integer array `nums`. For every `groups[i]`, choose a contiguous subarray of `nums` containing exactly the same values in the same order.

The chosen subarrays must occur in `groups` order and may not overlap, although unused values of `nums` may appear before, between, or after them. Return whether all groups can be placed under these rules.

### Function Contract

**Inputs**

- `groups`: between $1$ and $10^3$ nonempty integer arrays, each of length at most $10^3$.
- `nums`: an integer array with $1 \le N \le 10^3$, where $N=\lvert\texttt{nums}\rvert$.
- Every stored integer lies between $-10^7$ and $10^7$, inclusive.

Let

$$
S=\sum_{g\in\texttt{groups}}\lvert g\rvert
$$

with $S\le 10^3$, and let $L=\max_{g\in\texttt{groups}}\lvert g\rvert$.

**Return value**

- Return `True` if every group can match a distinct, non-overlapping contiguous region of `nums` in the given group order; otherwise return `False`.

### Examples

**Example 1**

- Input: `groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]`
- Output: `True`
- Explanation: The first group starts at index `3`, and the second follows it at index `6`.

**Example 2**

- Input: `groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]`
- Output: `False`
- Explanation: Both arrays occur, but only in the reverse of the required group order.

**Example 3**

- Input: `groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]`
- Output: `False`
- Explanation: The only occurrences share the value `3`, and overlapping matches are forbidden.
