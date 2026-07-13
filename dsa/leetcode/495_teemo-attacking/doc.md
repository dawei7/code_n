# Teemo Attacking

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 495 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/teemo-attacking/) |

## Problem Description
### Goal
You are given attack times in `timeSeries`, which is sorted in non-decreasing order, and a poison `duration`. An attack at second `t` poisons the enemy for exactly `duration` seconds, covering the inclusive interval from `t` through `t + duration - 1`.

Return the total number of seconds during which the enemy is poisoned. If another attack occurs before the current effect ends, its timer resets and the overlapping seconds are counted only once; if it occurs after the effect ends, a separate interval begins. Preserve endpoint semantics when attacks touch, and return `0` when the duration is zero.

### Function Contract
**Inputs**

- `time_series`: attack times in nondecreasing order
- `duration`: the positive poison duration caused by each attack

**Return value**

- The total number of time units covered by at least one poison interval

### Examples
**Example 1**

- Input: `time_series = [1, 4], duration = 2`
- Output: `4`

**Example 2**

- Input: `time_series = [1, 2], duration = 2`
- Output: `3`

**Example 3**

- Input: `time_series = [1], duration = 5`
- Output: `5`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Measure what each later attack newly contributes**

An attack at time `t` covers `duration` units, ending just before `t + duration`. For consecutive attack times, the earlier interval contributes only until the next attack begins or until its full duration ends, whichever occurs first.

**Add capped gaps**

For each adjacent pair, add `min(duration, next_time - current_time)`. A small gap counts only the non-overlapping prefix before the poison is refreshed; a gap at least as large as the duration counts the entire earlier interval.

**Account for the last attack**

No later attack truncates the final interval, so add one full `duration` after processing all gaps. If the series is empty, there is no final interval and the answer is zero.

**Why no time unit is double-counted**

The capped contribution assigned to each attack ends at or before the next attack time. These contributions are disjoint and together cover the union through the final start; the last full interval covers the remaining suffix. Their sum is exactly the poison-interval union length.

#### Complexity detail

The algorithm scans $n - 1$ adjacent gaps once, giving $O(n)$ time. A running total and the current gap use $O(1)$ extra space.

#### Alternatives and edge cases

- **Track the current interval end:** add only the extension beyond the previous end; this is another linear interval-union formulation.
- **Store every poisoned time unit:** is correct for integer time but can require $O(n \cdot duration)$ time and space.
- **Single attack:** contributes exactly one full duration.
- **Overlapping attacks:** count only the gap before the refresh.
- **Touching intervals:** a gap equal to `duration` contributes two non-overlapping full intervals.
- **Repeated timestamp:** adds zero for that gap because the poison merely restarts immediately.
- **Duration one:** every distinct attack time contributes one unit.

</details>
