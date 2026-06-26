# Find Servers That Handled Most Number of Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1606 |
| Difficulty | Hard |
| Topics | Array, Heap (Priority Queue), Simulation, Ordered Set |
| Official Link | [find-servers-that-handled-most-number-of-requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/) |

## Problem Description & Examples
### Goal
Assign incoming requests to available servers using the cyclic preference rule,
then return the servers that handled the most requests.

### Function Contract
**Inputs**

- `k`: the number of servers labeled `0` through `k - 1`.
- `arrival`: request arrival times.
- `load`: processing time for each corresponding request.

**Return value**

All busiest server indices in increasing order.

### Examples
**Example 1**

- Input: `k = 3, arrival = [1, 2, 3, 4, 5], load = [5, 2, 3, 3, 3]`
- Output: `[1]`

**Example 2**

- Input: `k = 3, arrival = [1, 2, 3, 4], load = [1, 2, 1, 2]`
- Output: `[0]`

**Example 3**

- Input: `k = 3, arrival = [1, 2, 3], load = [10, 12, 11]`
- Output: `[0, 1, 2]`

---

## Underlying Base Algorithm(s)
Maintain a min-heap of busy servers ordered by finish time and an ordered set of
available server indices. Before each request, release servers whose finish time
is no later than the arrival time. Then choose the smallest available index at
least `i % k`, wrapping to the smallest available index if needed.

---

## Complexity Analysis
- **Time Complexity**: `O(n log k)`.
- **Space Complexity**: `O(k)`.
