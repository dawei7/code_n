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

### Required Complexity

- **Time:** $O(B\log B)$
- **Space:** $O(B)$

<details>
<summary>Approach</summary>

#### General

**Represent every boundary as a signed event.** At each building's start, add
its height to the active height sum and one to the active count. At its end,
subtract the same values. Combine all changes occurring at one coordinate,
then process the event coordinates in sorted order.

**Emit the interval before applying its right-boundary event.** Between two
consecutive event coordinates, the active set is constant. If its count is
positive, its average is `total_height // active_count`. Append that interval,
or extend the previous output segment when it ends at the current interval's
left boundary and has the same average. If the active count is zero, emit
nothing, so a gap naturally breaks later merging.

Every possible change in coverage or average occurs at a building endpoint.
The sweep therefore assigns the correct active sum and count to every maximal
elementary interval between endpoints. Merging exactly the adjacent intervals
with equal averages preserves their values and removes every unnecessary
boundary; no further merge is legal across a different average or uncovered
gap. The result consequently uses the minimum number of segments.

#### Complexity detail

Here $B$ is the number of buildings. Creating at most $2B$ combined events
takes $O(B)$ work, and sorting their coordinates takes $O(B\log B)$ time. The
sweep is linear in the event count. The event map and output use $O(B)$ space.

#### Alternatives and edge cases

- **Rescan every building between endpoints:** This computes correct averages
  but takes $O(B^2)$ time when there are linearly many distinct boundaries.
- **Coordinate-sized difference arrays:** Allocating through coordinate
  $10^8$ is wasteful because only building endpoints can change the answer.
- Integer division may keep an average unchanged when a building starts or
  ends; such adjacent regions still merge.
- Equal averages on opposite sides of an uncovered gap cannot merge.
- Starts and ends at the same coordinate must be combined before evaluating
  the interval to their right.

</details>
