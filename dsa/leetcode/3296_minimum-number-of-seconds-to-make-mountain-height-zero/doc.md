# Minimum Number of Seconds to Make Mountain Height Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3296 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) |

## Problem Description

### Goal

A mountain has positive integer height `mountainHeight`, and `workerTimes[i]` is worker $i$'s base work time. If that worker removes $x$ units, the successive units cost `workerTimes[i] * 1`, `workerTimes[i] * 2`, through `workerTimes[i] * x` seconds.

Workers operate simultaneously and may each remove any non-negative integer number of units. Therefore, an assignment finishes after the maximum time spent by any worker. Return the minimum number of seconds in which their combined removals can reduce the entire mountain height to zero.

### Function Contract

**Inputs**

- `mountainHeight`: The positive number of height units that must be removed.
- `workerTimes`: A list of positive base times, one per worker.

The constraints guarantee $1 \le mountainHeight \le 10^5$, at most $10^4$ workers, and $1 \le workerTimes[i] \le 10^6$.

**Return value**

- The minimum simultaneous completion time in seconds.

### Examples

#### Example 1

- **Input:** `mountainHeight = 4`, `workerTimes = [2,1,1]`
- **Output:** `3`

#### Example 2

- **Input:** `mountainHeight = 10`, `workerTimes = [3,2,2,4]`
- **Output:** `12`

#### Example 3

- **Input:** `mountainHeight = 5`, `workerTimes = [1]`
- **Output:** `15`
