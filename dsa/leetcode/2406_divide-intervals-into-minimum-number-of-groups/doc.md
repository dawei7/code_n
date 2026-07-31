# Divide Intervals Into Minimum Number of Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2406 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) |

## Problem Description

### Goal

You are given a collection of inclusive integer intervals `[left, right]`.
Place every interval into exactly one group so that no two intervals assigned
to the same group intersect.

Intervals intersect whenever they share at least one point. In particular,
`[1,5]` and `[5,8]` intersect at 5 and cannot share a group. Return the minimum
number of groups needed to place all intervals.

### Function Contract

**Inputs**

- `intervals`: A list of $n$ inclusive pairs `[left, right]`, where
  $1 \le n \le 10^5$ and
  $1 \le \texttt{left}\le\texttt{right}\le10^6$.

**Return value**

Return the smallest number of groups such that intervals within each group
are pairwise disjoint, including at their endpoints.

### Examples

**Example 1**

- Input: `intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]`
- Output: `3`
- Explanation: Three intervals overlap at some points, so at least three
  groups are necessary, and a three-group assignment exists.

**Example 2**

- Input: `intervals = [[1,3],[5,6],[8,10],[11,13]]`
- Output: `1`
- Explanation: No two intervals intersect.

**Example 3**

- Input: `intervals = [[1,5],[5,8]]`
- Output: `2`
- Explanation: Inclusive endpoints make the intervals intersect at 5.
