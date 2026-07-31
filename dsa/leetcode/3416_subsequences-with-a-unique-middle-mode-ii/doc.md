# Subsequences with a Unique Middle Mode II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3416 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/) |

## Problem Description

### Goal

Given an integer array `nums`, count its subsequences of length five whose middle element is their unique mode. A subsequence retains the relative order of the chosen array positions, and its middle element is therefore the third selected value.

A mode is a value having maximum frequency within the five selected values. It is unique only when no other value has the same frequency. Count the index choices, not merely distinct value sequences, and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An integer array from which five positions are selected in increasing index order.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $5\le n\le10^5$ and $-10^9\le\texttt{nums[i]}\le10^9$.

**Return value**

- The number of length-five subsequences whose third value is the only mode, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 1, 1, 1, 1, 1]`
- Output: `6`

Every choice of five positions contains only the value 1, so all $\binom{6}{5}=6$ choices qualify.

**Example 2**

- Input: `nums = [1, 2, 2, 3, 3, 4]`
- Output: `4`

The qualifying choices make their third selected value occur more often than every competing value; choices tying the frequencies of 2 and 3 do not qualify.

**Example 3**

- Input: `nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]`
- Output: `0`

Every chosen value is distinct, so no subsequence has a unique mode.
