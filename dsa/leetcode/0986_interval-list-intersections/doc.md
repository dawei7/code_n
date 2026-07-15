# Interval List Intersections

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 986 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sweep Line |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/interval-list-intersections/) |

## Problem Description

### Goal

You are given two lists of closed intervals, `firstList` and `secondList`. Within each list, intervals are sorted by their positions and are pairwise disjoint.

A closed interval $[a,b]$ contains every real number $x$ satisfying $a\le x\le b$. The intersection of two closed intervals is empty when they do not overlap; otherwise it is the closed interval shared by both. Return the ordered list of every intersection between the two input lists. Because endpoints are included, intervals that meet at exactly one endpoint intersect in a one-point interval such as `[5, 5]`.

### Function Contract

**Inputs**

- `firstList`: $M$ sorted, pairwise-disjoint intervals `[start_i, end_i]`.
- `secondList`: $N$ sorted, pairwise-disjoint intervals `[start_j, end_j]`.
- Each list has at most $1000$ intervals, at least one interval exists across both lists, and every endpoint satisfies $0\le\texttt{start}<\texttt{end}\le10^9$.

Let $K$ be the number of intersections returned.

**Return value**

- All non-empty closed intersections, in increasing order.

### Examples

**Example 1**

- Input: `firstList = [[0, 2], [5, 10], [13, 23], [24, 25]], secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]`
- Output: `[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]`

**Example 2**

- Input: `firstList = [[1, 3], [5, 9]], secondList = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(M+N)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**Compare one current interval from each list:** Keep pointers `i` and `j`. The candidate overlap begins at `max(firstList[i][0], secondList[j][0])` and ends at `min(firstList[i][1], secondList[j][1])`. Append that closed interval when the beginning is at most the ending.

**Discard the interval that ends first:** If the current first-list interval has the smaller endpoint, advance `i`; it cannot intersect any later second-list interval because those intervals start beyond the current second interval's position. Otherwise advance `j`. On equal ending points, advancing either pointer is safe because neither ended interval can overlap a later interval in the opposite disjoint list.

Each iteration records the complete intersection of the current pair when one exists. The interval with the earlier end has then exhausted every possible overlap, so discarding it cannot miss a future result. At least one pointer advances on every iteration, and the scan ends only when one list has no interval left to intersect. Therefore every possible cross-list overlap is produced exactly once and in order.

#### Complexity detail

Pointer `i` advances at most $M$ times and `j` at most $N$ times, so time is $O(M+N)$. The returned $K$ intervals use $O(K)$ space; the two pointers use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Test every cross-list pair:** Direct comparison is correct but costs $O(MN)$ time and ignores sorted disjointness.
- **Event sweep line:** Sorting endpoint events can solve more general overlapping collections, but these inputs are already ordered and need no extra sort.
- **Touching endpoints:** Since intervals are closed, equal overlap boundaries produce a valid one-point interval.
- **Empty list:** If either input list is empty, there can be no intersection.
- **One interval contains another:** The overlap is exactly the contained interval, after which the shorter-ending pointer advances.

</details>
