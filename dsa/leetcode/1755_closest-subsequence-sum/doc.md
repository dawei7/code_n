# Closest Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1755 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Bit Manipulation, Sorting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-subsequence-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `goal`. A subsequence may be formed by deleting any number of elements, including all of them, without changing the order of those retained. Its sum is the total of its selected elements.

Among every possible subsequence of `nums`, find one whose sum is closest to `goal`. Return the minimum possible absolute difference between that subsequence sum and `goal`. The selected subsequence need not be contiguous, and the empty subsequence contributes a sum of zero.

### Function Contract

**Inputs**

- `nums`: an integer array with $1 \le n \le 40$, where $n=\lvert\texttt{nums}\rvert$ and each value lies between $-10^7$ and $10^7$, inclusive.
- `goal`: an integer satisfying $-10^9 \le \texttt{goal} \le 10^9$.

**Return value**

- Return $\min\lvert\texttt{goal}-x\rvert$ over all sums $x$ of subsequences of `nums`.

### Examples

**Example 1**

- Input: `nums = [5, -7, 3, 5], goal = 6`
- Output: `0`
- Explanation: Selecting `5`, `-7`, `3`, and `5` gives a sum of `6`, exactly matching the goal.

**Example 2**

- Input: `nums = [7, -9, 15, -2], goal = -5`
- Output: `1`
- Explanation: A subsequence sum of `-6` is attainable, and no attainable sum is closer to `-5`.

**Example 3**

- Input: `nums = [1, 2, 3], goal = -7`
- Output: `7`
- Explanation: Every nonempty subsequence has a positive sum, so the empty subsequence with sum zero is closest.
