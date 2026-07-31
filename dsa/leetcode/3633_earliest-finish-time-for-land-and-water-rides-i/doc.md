# Earliest Finish Time for Land and Water Rides I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3633 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/) |

## Problem Description
### Goal

A theme park offers land rides and water rides. For each land ride, `landStartTime[i]` is its earliest boarding time and `landDuration[i]` is its duration. The corresponding water arrays describe the same information for each water ride.

A tourist must take exactly one ride from each category, and may choose either category first. A ride can begin at its opening time or later. After the first ride ends, the tourist may immediately start the selected second ride if it is open; otherwise, the tourist waits until that ride opens.

Return the earliest time at which both selected rides can be completed.

### Function Contract
**Inputs**

- `landStartTime`: Opening times for the $n$ land rides.
- `landDuration`: Durations for the same $n$ land rides.
- `waterStartTime`: Opening times for the $m$ water rides.
- `waterDuration`: Durations for the same $m$ water rides.

The paired arrays have matching lengths, $1 \le n,m \le 100$, and every opening time and duration lies from 1 through 1000.

**Return value**

Return the minimum possible finishing time after taking exactly one land ride and one water ride in either order.

### Examples
**Example 1**

- Input: `landStartTime = [2, 8], landDuration = [4, 1], waterStartTime = [6], waterDuration = [3]`
- Output: `9`
- Explanation: Take land ride 0 from time 2 to 6, then water ride 0 from time 6 to 9.

**Example 2**

- Input: `landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]`
- Output: `14`
- Explanation: The water ride ends at 11; the land ride is already open and then ends at 14.
