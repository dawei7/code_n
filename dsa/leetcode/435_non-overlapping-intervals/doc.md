# Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 435 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) |

## Problem Description
### Goal
Given intervals `[start, end]` with `start < end`, remove selected intervals so that every pair left in the collection is nonoverlapping. Intervals that only meet at a shared endpoint are compatible and may both remain.

Return the minimum number of removals needed. Input order has no scheduling significance, and several optimal retained sets may exist. Removing one interval can resolve conflicts with several others, so counting overlapping pairs is not the answer. The function returns only the number removed, not the retained intervals or their reordered schedule. A one-interval input requires zero removals.

### Function Contract
**Inputs**

- `intervals`: a list of `[start, end]` pairs with `start < end`

**Return value**

- Return the minimum number of intervals that must be removed; intervals that only touch at an endpoint do not overlap.

### Examples
**Example 1**

- Input: `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`
- Output: `1`

**Example 2**

- Input: `intervals = [[1, 2], [1, 2], [1, 2]]`
- Output: `2`

**Example 3**

- Input: `intervals = [[1, 2], [2, 3]]`
- Output: `0`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn removals into a maximum compatible selection**

If `k` intervals can be retained without overlap, exactly $n - k$ are removed. Therefore maximize the number kept. Sort intervals by increasing end time and scan them in that order.

**Accept the earliest finishing compatible interval**

Keep `previous_end`, the end of the last selected interval. Select the current interval when its start is at least `previous_end`, then update the boundary to its end. Endpoint equality is allowed because touching intervals do not overlap.

**Why the earliest finish leaves the most choices**

Consider the first interval in any optimal compatible selection. The greedy first interval ends no later because it is the earliest-ending candidate overall. Replacing the optimal selection's first interval with the greedy one cannot invalidate any later interval: every later start that followed the old end also follows the no-later greedy end. Applying the same exchange after each selected interval proves the greedy scan keeps as many intervals as any solution.

**Recover the removal count**

Every rejected interval overlaps the current greedy boundary and cannot be inserted into that selected sequence. Once the scan counts the maximum number kept, subtract it from the original interval count.

#### Complexity detail

Sorting `n` intervals dominates the linear scan, giving $O(n \log n)$ time. Python's sorting implementation may use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Sort by start time:** on an overlap, retain the interval with the smaller end; this is an equivalent $O(n \log n)$ greedy method.
- **Dynamic programming:** compute the longest compatible subsequence after sorting in $O(n^2)$ time and $O(n)$ space.
- **Sort by shortest duration:** can discard a globally useful early-finishing interval and is not generally correct.
- **Touching endpoints:** `[a, b]` and `[b, c]` are compatible.
- **Duplicate intervals:** at most one copy can remain.
- **One interval:** no removal is necessary.

</details>
