# Minimize Connected Groups by Inserting Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3323 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) |

## Problem Description

### Goal

Each pair `[start, end]` describes a closed interval. A connected group is a maximal collection whose union covers every point from its smallest start through its largest end without an uncovered gap. Intervals that overlap or meet at an endpoint belong to the same group, while a positive uncovered segment separates groups.

Add exactly one new interval `[start_new, end_new]` whose length `end_new - start_new` is at most `k`. Choose its placement so the number of connected groups after insertion is as small as possible, and return that minimum. The original intervals may be unsorted and may already overlap; one added interval can join several consecutive existing groups if it spans every separating gap between its first and last group.

### Function Contract

**Inputs**

- `intervals`: A list of $n$ closed intervals `[start, end]`, where $1\leq n\leq10^5$ and $1\leq\texttt{start}\leq\texttt{end}\leq10^9$.
- `k`: The maximum permitted length of the one newly inserted interval, where $1\leq k\leq10^9$.

**Return value**

Return the minimum possible number of connected groups after inserting exactly one qualifying interval.

### Examples

#### Example 1

- **Input:** `intervals = [[1, 3], [5, 6], [8, 10]], k = 3`
- **Output:** `2`
- **Explanation:** Adding `[3, 5]` joins the first two groups. The group `[8, 10]` remains separate.

#### Example 2

- **Input:** `intervals = [[5, 10], [1, 1], [3, 3]], k = 1`
- **Output:** `3`
- **Explanation:** Neither positive gap can be bridged by an interval of length at most one, so a new zero-length interval may be placed inside an existing group without changing the count.
