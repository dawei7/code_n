# Time to Cross a Bridge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2532 |
| Difficulty | Hard |
| Topics | Array, Heap (Priority Queue), Simulation |
| Official Link | [time-to-cross-a-bridge](https://leetcode.com/problems/time-to-cross-a-bridge/) |

## Problem Description & Examples
### Goal
Manage a bridge crossing simulation where workers move boxes between a left and right warehouse. Each worker has a unique efficiency rating (sum of time to cross left-to-right and right-to-left). Workers must cross in a specific priority order based on their efficiency, and the bridge can only hold one person at a time. The goal is to determine the exact time the last box is placed in the right warehouse.

### Function Contract
**Inputs**

- `n` (int): The total number of boxes to move.
- `k` (int): The number of workers.
- `time` (List[List[int]]): A list of size `k` where each element contains four integers: `[left_to_right, pick_up, right_to_left, put_down]`.

**Return value**

- `int`: The timestamp when the final box is successfully placed in the right warehouse.

### Examples
**Example 1**

- Input: `n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]`
- Output: `6`

**Example 2**

- Input: `n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]`
- Output: `50`

**Example 3**

- Input: `n = 1, k = 1, time = [[1,2,3,4]]`
- Output: `10`

---

## Underlying Base Algorithm(s)
The problem is solved using a discrete event simulation with four priority queues:
1. `left_wait`: Workers waiting to cross to the right (prioritized by efficiency, then index).
2. `right_wait`: Workers waiting to cross to the left (prioritized by efficiency, then index).
3. `left_busy`: Workers currently picking up or putting down boxes on the left (prioritized by finish time).
4. `right_busy`: Workers currently picking up or putting down boxes on the right (prioritized by finish time).

The simulation advances time to the next available event, prioritizing workers with higher efficiency (larger sum of crossing times) to cross the bridge.

---

## Complexity Analysis
- **Time Complexity**: `O(n log k + k log k)`, where `n` is the number of boxes and `k` is the number of workers. Each box involves a constant number of heap operations.
- **Space Complexity**: `O(k)` to store the state of the workers in the four priority queues.
