# Set Intersection Size At Least Two

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 757 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/set-intersection-size-at-least-two/) |

## Problem Description

### Goal

Each input interval `[start_i, end_i]` represents all integers from its start through its end, inclusively. A containing set is a set of integers that has at least two of its members inside every interval.

Return the minimum possible size of such a containing set. The same selected integer may help satisfy several overlapping intervals, but each individual interval must contain two distinct selected values. Return only the minimum cardinality, not the set itself.

### Function Contract

**Inputs**

- `intervals`: a list of inclusive integer intervals `[start, end]`, each containing at least two integers.

**Return value**

- The smallest possible number of distinct integers whose intersection with every interval has size at least two.

### Examples

**Example 1**

- Input: `intervals = [[1,3],[1,4],[2,5],[3,5]]`
- Output: `3`
- Explanation: Three carefully shared points can give every interval two members.

**Example 2**

- Input: `intervals = [[1,2],[2,3],[2,4],[4,5]]`
- Output: `5`
- Explanation: The two short boundary intervals force two points at each end, with one additional shared middle point.
