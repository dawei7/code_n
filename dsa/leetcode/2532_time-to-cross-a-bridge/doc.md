# Time to Cross a Bridge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2532 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/time-to-cross-a-bridge/) |

## Problem Description

### Goal

There are `n` boxes in an old warehouse on the right side of a bridge, a new warehouse on the left, and `k` workers initially waiting on the left. For worker $i$, `time[i] = [right_i, pick_i, left_i, put_i]`: crossing left-to-right takes `right_i`, picking up one box takes `pick_i`, crossing back with it takes `left_i`, and putting it into the new warehouse takes `put_i` minutes. Only one worker may occupy the bridge at a time, while pickup and put-down work can proceed concurrently away from it.

A worker is less efficient when `right_i + left_i` is larger; equal sums are broken by larger worker index. Whenever the bridge becomes free, a waiting box-carrying worker on the right has priority over every worker on the left. Within the chosen side, the least efficient waiting worker crosses. Do not send another worker right after enough workers have already been dispatched to collect every remaining box.

Simulate these rules and return the time when the last box reaches the left side of the bridge. The final worker's later `put_i` time is not included because the box has already reached the requested side.

### Function Contract

**Inputs**

- `n`: The number of boxes to move from the right warehouse.
- `k`: The number of workers.
- `time`: Exactly `k` rows `[right_i, pick_i, left_i, put_i]` describing each worker.

The constraints are $1 \le n,k \le 10^4$, and every entry of `time` is between $1$ and $1000$, inclusive.

**Return value**

Return the elapsed time at which the worker carrying the final box finishes crossing from right to left.

### Examples

#### Example 1

- **Input:** `n = 1, k = 3, time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]`
- **Output:** `6`
- **Explanation:** Worker `2` has highest priority, crosses right in one minute, picks up the box in one minute, and crosses left in four minutes. The following put-down minute is excluded.

#### Example 2

- **Input:** `n = 3, k = 2, time = [[1, 5, 1, 8], [10, 10, 10, 10]]`
- **Output:** `37`
