# Minimum Speed to Arrive on Time

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) |
| Frontend ID | 1870 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You must take $N$ train rides in their given order to reach the office. `dist[i]` is the distance of ride `i`, and every train travels at one shared positive integer speed. The actual travel time of a ride is its distance divided by that speed.

Except for the final ride, the next train can depart only at an integer-hour mark. Finishing an earlier ride at a fractional time therefore adds a wait until the next integer hour; finishing exactly at an integer hour adds no wait. The final arrival is not rounded. Given the available time `hour`, return the smallest speed that arrives no later than the deadline, or `-1` when no valid speed up to the guaranteed bound can do so.

### Function Contract

**Inputs**

- `dist`: an integer list of $N$ positive ride distances, where $1 \le N \le 10^5$ and each distance is at most $10^5$.
- `hour`: the available time, with at most two decimal places.
- Let $U = 10^7$, the guaranteed maximum possible answer.

**Return value**

- Return the minimum positive integer speed that makes the total commute time at most `hour`.
- Return `-1` if no such speed exists.

### Examples

**Example 1**

- Input: `dist = [1,3,2], hour = 6`
- Output: `1`

At speed one, the rides finish at integer-hour marks and total exactly six hours.

**Example 2**

- Input: `dist = [1,3,2], hour = 2.7`
- Output: `3`

The first two departures occur at hours one and two; the last ride finishes after another $2/3$ hour.

**Example 3**

- Input: `dist = [1,3,2], hour = 1.9`
- Output: `-1`

Even at arbitrarily high speed, the two required departure boundaries consume at least two hours before the final ride.
