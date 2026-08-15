# Subsequences with a Unique Middle Mode I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3395 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/) |

## Problem Description

### Goal

Given an integer array `nums`, count its subsequences of exactly five elements whose middle element is the unique mode. A subsequence retains the selected elements' original relative order but need not use consecutive indices.

A mode is a value with maximum frequency in a sequence. A sequence has a unique mode when exactly one value reaches that maximum. Therefore, for a selected sequence `seq` of length five, `seq[2]` must occur strictly more often than every other selected value.

Return the number of qualifying index selections modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $5\le n\le1000$ and $-10^9\le\texttt{nums[i]}\le10^9$.

**Return value**

- The number of length-five subsequences whose element at index 2 is their unique mode, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [1, 1, 1, 1, 1, 1]`
- **Output:** `6`

Every choice of five indices produces `[1, 1, 1, 1, 1]`; there are $\binom{6}{5}=6$ such choices.

#### Example 2

- **Input:** `nums = [1, 2, 2, 3, 3, 4]`
- **Output:** `4`

The valid selections have their third value occurring more often than every competitor. A selection containing two 2s and two 3s is invalid because its mode is tied.

#### Example 3

- **Input:** `nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]`
- **Output:** `0`

Every selected value is distinct, so no five-element subsequence has a unique mode.
