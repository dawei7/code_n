# Earliest Finish Time for Land and Water Rides II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3635 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/) |

## Problem Description
### Goal

A theme park has two categories of attractions: land rides and water rides. For land ride `i`, `landStartTime[i]` is the earliest time it can be boarded and `landDuration[i]` is its duration. The water arrays describe the corresponding opening times and durations for water rides.

A tourist must complete exactly one ride from each category. Either category may be taken first, and a ride may begin at its opening time or at any later time. After the first ride finishes, the tourist immediately boards the selected second ride if it is already open or waits for its opening.

Return the earliest possible time at which both chosen rides are finished. The large category limits require avoiding examination of every land-water pair.

### Function Contract
**Inputs**

- `landStartTime`: Opening times for $n$ land rides.
- `landDuration`: Durations for those $n$ land rides.
- `waterStartTime`: Opening times for $m$ water rides.
- `waterDuration`: Durations for those $m$ water rides.

The paired arrays have equal lengths, $1 \le n,m \le 5\times10^4$, and each opening time and duration is between 1 and $10^5$.

**Return value**

Return the minimum finishing time after taking exactly one land ride and one water ride in either order.

### Examples
**Example 1**

- Input: `landStartTime = [2, 8], landDuration = [4, 1], waterStartTime = [6], waterDuration = [3]`
- Output: `9`
- Explanation: Land ride 0 ends at 6, allowing the water ride to start immediately and end at 9.

**Example 2**

- Input: `landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]`
- Output: `14`
- Explanation: Taking water first ends at 11, after which the already-open land ride ends at 14.
