# Average Height of Buildings in Each Segment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2015 |
| Difficulty | Medium |
| Topics | Array, Sorting, Heap (Priority Queue), Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/average-height-of-buildings-in-each-segment/) |

## Problem Description

### Goal

A straight street is represented by a number line. Each building
`[start, end, height]` occupies the half-closed interval `[start, end)`,
including its start but excluding its end.

Describe every covered part of the street with the minimum number of
non-overlapping segments. For each covered segment, report its left endpoint,
right endpoint, and the integer-division average of the heights of all
buildings present there. Adjacent covered regions with the same average must be
merged, even if their active building sets differ. Uncovered gaps are omitted
and prevent merging across them. The returned segments may appear in any
order.

### Function Contract

Let $B$ be the number of buildings.

**Inputs**

- `buildings`: a list of $B$ triples `[start, end, height]`, where
  $1\le B\le10^5$, $0\le\texttt{start}<\texttt{end}\le10^8$, and
  $1\le\texttt{height}\le10^5$.

**Return value**

Return triples `[left, right, average]` describing the minimum set of covered
half-closed segments.

### Examples

**Example 1**

- Input: `buildings = [[1, 4, 2], [3, 9, 4]]`
- Output: `[[1, 3, 2], [3, 4, 3], [4, 9, 4]]`
- Explanation: The overlap has integer average $(2+4)/2=3$.

**Example 2**

- Input: `buildings = [[1, 3, 2], [2, 5, 3], [2, 8, 3]]`
- Output: `[[1, 3, 2], [3, 8, 3]]`
- Explanation: Event boundaries at $2$ and $5$ do not appear in the output
  because the integer average remains unchanged across them.

**Example 3**

- Input: `buildings = [[1, 2, 1], [5, 6, 1]]`
- Output: `[[1, 2, 1], [5, 6, 1]]`
- Explanation: The uncovered interval `[2, 5)` prevents the equal averages
  from merging.
