# The Number of the Smallest Unoccupied Chair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1942 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Heap (Priority Queue) |
| Official Link | [the-number-of-the-smallest-unoccupied-chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/) |

## Problem Description & Examples
### Goal
Friends arrive and leave at known times. Each arriving friend takes the smallest-numbered currently free chair. Determine which chair the target friend receives.

### Function Contract
**Inputs**

- `times`: pairs `[arrival, leaving]` for each friend.
- `targetFriend`: the index of the friend to inspect.

**Return value**

Return the chair number assigned to `targetFriend`.

### Examples
**Example 1**

- Input: `times = [[1,4],[2,3],[4,6]], targetFriend = 1`
- Output: `1`

**Example 2**

- Input: `times = [[3,10],[1,5],[2,6]], targetFriend = 0`
- Output: `2`

**Example 3**

- Input: `times = [[1,2],[2,3]], targetFriend = 1`
- Output: `0`

---

## Underlying Base Algorithm(s)
Process friends in arrival order. Keep one min-heap of free chair numbers and one min-heap of occupied chairs keyed by leaving time. Before each arrival, release every chair whose leaving time is not later than the arrival time.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
