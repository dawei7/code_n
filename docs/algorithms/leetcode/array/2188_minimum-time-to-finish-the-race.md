# Minimum Time to Finish the Race

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2188 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-time-to-finish-the-race](https://leetcode.com/problems/minimum-time-to-finish-the-race/) |

## Problem Description & Examples
### Goal
Finish a fixed number of race laps in minimum time. A tire described by `[f, r]` takes `f * r^(x-1)` seconds on its `x`-th consecutive lap. Between laps, a tire may be replaced with any new tire at a fixed change cost.

### Function Contract
**Inputs**

- `tires`: pairs `[first_lap_time, degradation_factor]`.
- `changeTime`: seconds required to replace a tire.
- `numLaps`: the number of laps to finish.

**Return value**

The minimum total race time.

### Examples
**Example 1**

- Input: `tires = [[2, 3], [3, 4]]`, `changeTime = 5`, `numLaps = 4`
- Output: `21`

**Example 2**

- Input: `tires = [[1, 10], [2, 2], [3, 4]]`, `changeTime = 6`, `numLaps = 5`
- Output: `25`

**Example 3**

- Input: `tires = [[2, 2]]`, `changeTime = 3`, `numLaps = 2`
- Output: `6`

---

## Underlying Base Algorithm(s)
Precompute `best[len]`, the cheapest time to run `len` consecutive laps on one tire. Stop extending a stint once its next degraded lap is slower than changing and taking a fresh first lap, which keeps the useful stint range small. Then use dynamic programming over completed laps, trying each precomputed final stint; charge `changeTime` between stints but not before the first.

---

## Complexity Analysis
- **Time Complexity**: `O(TL + numLaps * L)`, where `T` is the tire count and `L` is the maximum useful stint length
- **Space Complexity**: `O(numLaps + L)`
