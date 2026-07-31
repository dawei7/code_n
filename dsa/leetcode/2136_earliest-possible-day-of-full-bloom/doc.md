# Earliest Possible Day of Full Bloom

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2136 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) |

## Problem Description
### Goal
You have $n$ seeds. Seed $i$ requires `plantTime[i]` full days of planting
work before it can grow. You can plant only one seed on any day, but a seed's
planting days need not be consecutive; it is complete after receiving the
required total work.

Once planting for seed $i$ finishes, it grows on its own for
`growTime[i]` full days while you may plant other seeds. It blooms after its
last growth day and remains bloomed. Starting at day `0`, schedule the planting
work to minimize the first day on which every seed is blooming.

### Function Contract
**Inputs**

- `plantTime`: Positive planting durations for $n$ seeds.
- `growTime`: Their corresponding positive growth durations.

The arrays have equal length $1\le n\le 10^5$, and every duration is at most
$10^4$.

**Return value**

The earliest achievable day on which all seeds have bloomed.

### Examples
**Example 1**

- Input: `plantTime = [1,4,3]`, `growTime = [2,3,1]`
- Output: `9`

**Example 2**

- Input: `plantTime = [1,2,3,2]`, `growTime = [2,1,2,1]`
- Output: `9`

**Example 3**

- Input: `plantTime = [1]`, `growTime = [1]`
- Output: `2`
