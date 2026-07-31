# Minimum Time to Complete Trips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2187 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/) |

## Problem Description

### Goal

Each entry `time[i]` is the duration one bus needs to complete a trip. A bus
may begin its next trip immediately after finishing its current one, and all
buses operate independently and concurrently.

Given the required combined count `totalTrips`, find the minimum elapsed time
by which the buses have completed at least that many trips in total. Completing
more than the target at the same earliest time is allowed; individual trips
cannot be partially counted.

### Function Contract

**Inputs**

- `time`: an array of bus trip durations, with
  $1\le\lvert\texttt{time}\rvert\le10^5$ and each duration in $[1,10^7]$.
- `totalTrips`: the required total number of completed trips, in $[1,10^7]$.

Define the guaranteed feasible upper bound

$$
U=\min(\texttt{time})\cdot\texttt{totalTrips}.
$$

**Return value**

Return the smallest positive integer time at which the combined completed-trip
count is at least `totalTrips`.

### Examples

**Example 1**

- Input: `time = [1,2,3]`, `totalTrips = 5`
- Output: `3`

**Example 2**

- Input: `time = [2]`, `totalTrips = 1`
- Output: `2`

**Example 3**

- Input: `time = [5,5]`, `totalTrips = 3`
- Output: `10`
