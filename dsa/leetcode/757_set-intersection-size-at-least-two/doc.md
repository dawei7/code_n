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

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Process the earliest finishing obligation first**

Sort intervals by increasing end. When ends tie, process the larger start first because that interval is more restrictive. Points chosen as far right as possible inside the current interval have the best chance of also lying in every later interval.

**Only the two latest chosen points affect the next interval**

Maintain `left < right`, the greatest two selected integers, and the answer size. Because intervals are processed by end, any earlier selected point is no more useful to the current interval than these two.

- If `start <= left`, both latest points already lie in the interval.
- If `left < start <= right`, only `right` lies inside; add `end`, then make the old `right` and new `end` the latest pair.
- If `start > right`, neither lies inside; add `end - 1` and `end`.

**Why rightmost additions preserve optimality**

When the current interval lacks one or two required points, every feasible solution must add at least that many points within it. Moving those new points rightward to `end` or `end - 1` cannot invalidate any already processed interval that needs them: those intervals end no later, and the current deficit identifies exactly how many additions are unavoidable. The rightward choice can only increase overlap with later-ending intervals. Thus each greedy addition has an optimal exchange, and the accumulated count is minimum.

#### Complexity detail

Sorting `n` intervals costs $O(n \log n)$ time; the greedy scan is $O(n)$. Python's sort may use $O(n)$ auxiliary storage, while the scan itself uses only two point values and a counter.

#### Alternatives and edge cases

- **Store and scan every selected point:** With the same interval order and rightmost additions it remains correct, but counting coverage can take $O(n^2)$ time.
- **Choose arbitrary points inside a deficit interval:** This can waste points because earlier choices overlap fewer later intervals than rightmost choices.
- **Equal interval ends:** Sort larger starts first so the narrowest interval establishes the needed points.
- **One interval:** Its last two integers form an optimal set of size `2`.
- **Disjoint intervals:** Each interval contributes two distinct points.
- **Nested intervals:** Satisfying the narrowest early-ending interval may satisfy all wider containers without additions.
- **Touching boundaries:** A shared endpoint counts as one selected integer in both intervals.

</details>
