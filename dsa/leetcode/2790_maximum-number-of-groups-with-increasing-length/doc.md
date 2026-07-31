# Maximum Number of Groups With Increasing Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2790 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/) |

## Problem Description

### Goal

You are given a 0-indexed array `usageLimits` of length $n$. The number $i$ may be placed into groups at most `usageLimits[i]` times in total across every group that you create.

Every individual group must contain distinct numbers, so the same number cannot occur twice inside one group. Arrange the groups in an order where each group after the first has strictly greater length than its predecessor. Return the maximum number of groups that can satisfy both the per-number usage limits and the strictly increasing length requirement.

### Function Contract

**Inputs**

- `usageLimits`: An array of positive integers, where `usageLimits[i]` is the total number of groups in which number $i$ may appear, $1 \le n \le 10^5$, and $1 \le \texttt{usageLimits[i]} \le 10^9$.

Let $n = \lvert\texttt{usageLimits}\rvert$.

**Return value**

Return the greatest possible number of groups with pairwise distinct members inside each group and strictly increasing group lengths.

### Examples

**Example 1**

- Input: `usageLimits = [1, 2, 5]`
- Output: `3`
- Explanation: Groups `[2]`, `[1, 2]`, and `[0, 1, 2]` have lengths $1$, $2$, and $3$ while respecting every limit.

**Example 2**

- Input: `usageLimits = [2, 1, 2]`
- Output: `2`
- Explanation: One valid choice is `[0]` followed by `[1, 2]`. Three strictly increasing groups cannot be formed.

**Example 3**

- Input: `usageLimits = [1, 1]`
- Output: `1`
- Explanation: Each number is usable only once, which is insufficient for groups of both lengths $1$ and $2$.
