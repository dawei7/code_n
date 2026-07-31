# Maximum Balanced Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2926 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-balanced-subsequence-sum/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, select a non-empty subsequence whose
indices are $i_0<i_1<\dots<i_{k-1}$. The subsequence is balanced when every
pair of consecutive selected indices satisfies

$$
\texttt{nums}[i_j]-\texttt{nums}[i_{j-1}]\ge i_j-i_{j-1}
\qquad\text{for }1\le j<k.
$$

A subsequence of length one is balanced automatically. Return the maximum
possible sum of the selected values. As with every subsequence, elements may
be deleted without changing the relative order of those that remain.

### Function Contract

**Inputs**

- `nums`: The integer array from which the balanced subsequence is selected.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le10^5$ and
$-10^9\le\texttt{nums[i]}\le10^9$.

**Return value**

- The greatest sum among all non-empty balanced subsequences of `nums`.

### Examples

**Example 1**

- Input: `nums = [3, 3, 5, 6]`
- Output: `14`
- Explanation: Indices 0, 2, and 3 give `[3, 5, 6]`; both consecutive
  differences satisfy the balance inequality.

**Example 2**

- Input: `nums = [5, -1, -3, 8]`
- Output: `13`
- Explanation: Selecting indices 0 and 3 gives `[5, 8]`, and $8-5\ge3-0$.

**Example 3**

- Input: `nums = [-2, -1]`
- Output: `-1`
- Explanation: The singleton subsequence containing `-1` is optimal.
