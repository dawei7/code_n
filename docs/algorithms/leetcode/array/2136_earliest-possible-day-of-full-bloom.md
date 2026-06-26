# Earliest Possible Day of Full Bloom

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2136 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting |
| Official Link | [earliest-possible-day-of-full-bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) |

## Problem Description & Examples
### Goal
Schedule planting work to make every seed bloom as early as possible. Seed `i` requires `plantTime[i]` days of exclusive planting work, can be planted across nonconsecutive days, and blooms after another `growTime[i]` days during which other seeds may be planted.

### Function Contract
**Inputs**

- `plantTime`: planting durations for the seeds.
- `growTime`: growth durations at matching indices.

**Return value**

The earliest day on which all seeds are in bloom.

### Examples
**Example 1**

- Input: `plantTime = [1, 4, 3]`, `growTime = [2, 3, 1]`
- Output: `9`

**Example 2**

- Input: `plantTime = [1, 2, 3, 2]`, `growTime = [2, 1, 2, 1]`
- Output: `9`

**Example 3**

- Input: `plantTime = [1]`, `growTime = [1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Plant seeds in descending order of growth time. After each seed's planting finishes, its bloom day is the cumulative planting time plus its growth time. Track the maximum such day. An exchange argument shows that putting the longer growth phase first never delays the earlier completion of the pair's final bloom.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for the sorted schedule, or `O(1)` auxiliary space if pairs are sorted in place
