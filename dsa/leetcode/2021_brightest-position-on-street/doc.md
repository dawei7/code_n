# Brightest Position on Street

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2021 |
| Difficulty | Medium |
| Topics | Array, Sorting, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/brightest-position-on-street/) |

## Problem Description

### Goal

A straight street is modeled as a number line containing several lamps. Each
entry `lights[i] = [position_i, range_i]` describes a lamp centered at
`position_i`. Its light covers every position in the inclusive interval from
`position_i - range_i` through `position_i + range_i`.

The brightness at a position is the number of lamp intervals containing that
position. Return a position with maximum brightness. If the maximum occurs at
several positions, return the smallest such position.

### Function Contract

Let $N$ be the number of lamps.

**Inputs**

- `lights`: a list of $N$ pairs `[position_i, range_i]`, where
  $1 \le N \le 10^5$, $-10^8 \le \text{position}_i \le 10^8$, and
  $0 \le \text{range}_i \le 10^8$.

**Return value**

- The smallest integer position attaining the greatest brightness.

### Examples

**Example 1**

- Input: `lights = [[-3, 2], [1, 2], [3, 3]]`
- Output: `-1`
- Explanation: Brightness is two at `-1` and throughout `0` through `3`;
  `-1` is the smallest maximizer.

**Example 2**

- Input: `lights = [[1, 0], [0, 1]]`
- Output: `1`
- Explanation: Both lamps cover position `1`, giving it brightness two.

**Example 3**

- Input: `lights = [[1, 2]]`
- Output: `-1`
- Explanation: Every position from `-1` through `3` has brightness one, so
  the smallest one is returned.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Represent only changes in brightness**

A lamp covering the inclusive interval `[left, right]` raises brightness by
one starting at `left`. Its contribution remains active at `right` and ends
immediately afterward, so record `+1` at `left` and `-1` at `right + 1`.
Combining equal event positions prevents coincident lamp boundaries from
requiring any special case.

**Sweep events from left to right**

Sort the event positions and maintain the sum of all changes seen so far.
After applying the change at a position, that sum is the brightness beginning
at that position and continuing until the next event. If it exceeds the best
brightness recorded so far, store the current position.

Event positions are processed in increasing order, and the answer changes only
for a strictly larger brightness. Therefore, the first position recorded for
any brightness is its smallest occurrence. Every lamp is included exactly
between its start event and its end event, so the running sum equals the true
brightness throughout the sweep. The stored position is consequently the
smallest position attaining the global maximum.

#### Complexity detail

There are at most $2N$ distinct event positions. Building their changes takes
$O(N)$ time, sorting them takes $O(N\log N)$ time, and the sweep takes $O(N)$
time. The event map and sorted keys use $O(N)$ space.

#### Alternatives and edge cases

- **Ordered event map:** Inserting changes into a balanced ordered map performs
  the same sweep online, with $O(N\log N)$ time and $O(N)$ space.
- **Scan every integer position:** Testing each coordinate and recounting all
  lamps is correct but can depend on an enormous coordinate span and take
  quadratic or worse time.
- A zero-range lamp illuminates its center only; placing its removal event at
  `position + 1` preserves that endpoint.
- Multiple changes at one coordinate must be combined before comparing the
  resulting brightness.
- Updating the answer on an equal brightness would incorrectly replace the
  smallest maximizer with a later position.
- Negative positions and intervals crossing zero require no separate handling.

</details>
