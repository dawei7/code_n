# Maximize Sum Of Array After K Negations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1005 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. One operation chooses an index `i` and replaces `nums[i]` with `-nums[i]`, reversing the sign of that element.

Apply this operation exactly `k` times and return the largest array sum that can be achieved. The same index may be chosen more than once, so surplus operations can cancel in pairs; a zero can also absorb any number of sign changes without affecting the array.

### Function Contract

**Inputs**

- `nums`: an integer array of length $N$, where $1\le N\le10^4$ and $-100\le\texttt{nums[i]}\le100$.
- `k`: the exact number of sign-negation operations to perform, where $1\le k\le10^4$.

**Return value**

- The largest possible sum after exactly `k` permitted sign changes.

### Examples

**Example 1**

- Input: `nums = [4, 2, 3], k = 1`
- Output: `5`
- Explanation: Negating `nums[1]` changes the array to `[4, -2, 3]`.

**Example 2**

- Input: `nums = [3, -1, 0, 2], k = 3`
- Output: `6`
- Explanation: Choosing indices `1`, `2`, and `2` produces `[3, 1, 0, 2]`.

**Example 3**

- Input: `nums = [2, -3, -1, 5, -4], k = 2`
- Output: `13`
- Explanation: Negating the values `-3` and `-4` produces `[2, 3, -1, 5, 4]`.
