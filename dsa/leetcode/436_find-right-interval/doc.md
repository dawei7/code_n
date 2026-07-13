# Find Right Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 436 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-right-interval/) |

## Problem Description
### Goal
Given intervals with unique start values, find a right interval for every original interval `i`. A candidate `j` is on the right when `intervals[j].start >= intervals[i].end`; among candidates, choose the one with the smallest qualifying start.

Return one original index per input interval in the same order as the input. Use `-1` when no start reaches the required end. The chosen interval need not be adjacent in input order, and endpoint equality qualifies. Return indices rather than interval values, preserving the unique-start tie guarantee.

### Function Contract
**Inputs**

- `intervals`: a list of `[start, end]` pairs whose start values are unique

**Return value**

- Return one index per input interval. Use the chosen right interval's original index, or `-1` when no start is large enough.

### Examples
**Example 1**

- Input: `intervals = [[1, 2]]`
- Output: `[-1]`

**Example 2**

- Input: `intervals = [[3, 4], [2, 3], [1, 2]]`
- Output: `[-1, 0, 1]`

**Example 3**

- Input: `intervals = [[1, 4], [2, 3], [3, 4]]`
- Output: `[-1, 2, -1]`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate searchable starts from original positions**

Create `(start, original_index)` pairs and sort them by start. The original interval order remains untouched, while the sorted starts form the monotone search space needed for every query.

**Find the lower bound of each end**

For an interval ending at `end`, binary-search for the first sorted start that is at least `end`. If the insertion position is inside the array, its paired original index is the answer; if it equals `n`, no right interval exists.

**Why the lower bound is exactly the requested interval**

Every sorted position before the lower bound has a start smaller than the current end and is invalid. The lower-bound position, when present, is valid and no later position can have a smaller start. Unique starts make its original index unambiguous.

#### Complexity detail

Sorting the `n` indexed starts costs $O(n \log n)$. Each of `n` binary searches costs $O(\log n)$, so total time remains $O(n \log n)$. The sorted pairs, start array, and output use $O(n)$ space.

#### Alternatives and edge cases

- **Two sorted sweeps:** sort starts and ends separately, then advance a start pointer to answer every end in $O(n \log n)$ total time.
- **Scan every interval for every query:** directly tracks the smallest valid start but takes $O(n^2)$ time.
- **One interval:** it usually has no right interval because its end exceeds its own start.
- **Negative coordinates:** ordering and lower bounds work unchanged.
- **Exact endpoint match:** a start equal to the current end is valid.
- **No qualifying start:** return `-1` for that position.

</details>
