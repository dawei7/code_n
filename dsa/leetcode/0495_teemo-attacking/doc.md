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
