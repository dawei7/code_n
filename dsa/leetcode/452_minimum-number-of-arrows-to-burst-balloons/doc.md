# Minimum Number of Arrows to Burst Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 452 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) |

## Problem Description
### Goal
Each balloon spans a closed horizontal interval `[start, end]`. An arrow fired vertically at coordinate `x` bursts every balloon whose interval contains `x`, including balloons for which `x` equals either endpoint.

Return the minimum number of arrow coordinates needed to burst all balloons. One arrow may cover many overlapping intervals, while disjoint groups require separate arrows. Touching intervals can share an endpoint arrow because their boundaries are inclusive. Input order does not matter, and the function returns only the minimum count rather than the chosen coordinates. A single balloon requires one arrow.

### Function Contract
**Inputs**

- `points`: a list of intervals `[start, end]`; an arrow fired at coordinate `x` bursts an interval when `start <= x <= end`

**Return value**

- The minimum number of arrow coordinates whose union intersects every interval

### Examples
**Example 1**

- Input: `points = [[10, 16], [2, 8], [1, 6], [7, 12]]`
- Output: `2`

**Example 2**

- Input: `points = [[1, 2], [3, 4], [5, 6], [7, 8]]`
- Output: `4`

**Example 3**

- Input: `points = [[1, 2], [2, 3], [3, 4], [4, 5]]`
- Output: `2`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Commit at the earliest finishing balloon**

Sort intervals by their right endpoint. Fire the first arrow at the smallest endpoint. Any solution must use some arrow to burst that earliest-ending interval; moving that arrow rightward to the interval's endpoint cannot lose compatibility with any later-ending interval that the original arrow also hit. Therefore an optimal solution exists with this greedy first choice.

**Reuse an arrow while intervals contain it**

Keep the coordinate of the most recent arrow. In endpoint order, an interval is already burst exactly when its start is at most that coordinate. If its start is greater, it cannot share the previous arrow, so fire a new one at this interval's endpoint. Repeating the exchange argument after discarding already-burst intervals proves every greedy choice is compatible with an optimum.

**Closed endpoints make touching intervals overlap**

The containment test is `start <= arrow`, not a strict comparison. An arrow at `2` bursts both `[1, 2]` and `[2, 3]`.

#### Complexity detail

Sorting dominates at $O(n \log n)$ time, and the greedy scan is $O(n)$. Creating a sorted copy uses $O(n)$ auxiliary space; an in-place sort can reduce explicit container space subject to the language's sorting implementation.

#### Alternatives and edge cases

- **Sort by starts and maintain an intersection:** track the minimum end within the current overlapping group; starting a disjoint group adds one arrow and is also $O(n \log n)$.
- **Repeatedly choose the smallest remaining endpoint:** follows the same greedy rule but rescanning and filtering the remaining intervals costs $O(n^2)$.
- **Merge intervals first:** can count overlap groups, but stores merged ranges that are unnecessary for the count.
- **Empty input:** requires zero arrows.
- **Nested intervals:** the innermost interval's endpoint can burst the entire containing group.
- **Duplicate intervals:** all copies are burst by the same arrow.
- **Negative coordinates:** comparisons work without any coordinate offset or special case.

</details>
