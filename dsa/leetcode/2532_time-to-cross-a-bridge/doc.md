# Time to Cross a Bridge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2532 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [time-to-cross-a-bridge](https://leetcode.com/problems/time-to-cross-a-bridge/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/time-to-cross-a-bridge/).

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

- Input: `n = 3, k = 2, time = [[1,5,1,8],[10,10,10,10]]`
- Output: `37`

**Example 3**

- Input: `n = 1, k = 1, time = [[1,2,3,4]]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a discrete event simulation with four priority queues:
1. `left_wait`: Workers waiting to cross to the right (prioritized by efficiency, then index).
2. `right_wait`: Workers waiting to cross to the left (prioritized by efficiency, then index).
3. `left_busy`: Workers currently picking up or putting down boxes on the left (prioritized by finish time).
4. `right_busy`: Workers currently picking up or putting down boxes on the right (prioritized by finish time).

The simulation advances time to the next available event, prioritizing workers with higher efficiency (larger sum of crossing times) to cross the bridge.

### Complexity Analysis
- **Time Complexity**: `O(n log k + k log k)`, where `n` is the number of boxes and `k` is the number of workers. Each box involves a constant number of heap operations.
- **Space Complexity**: `O(k)` to store the state of the workers in the four priority queues.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(n: int, k: int, time: list[list[int]]) -> int:
    # Efficiency: left_to_right + right_to_left
    # Priority: Higher efficiency first, then higher index
    # We use negative values for max-heap behavior in Python's min-heap

    # left_wait: (-efficiency, -index)
    left_wait = []
    for i in range(k):
        heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))

    # right_wait: (-efficiency, -index)
    right_wait = []

    # left_busy: (finish_time, index)
    left_busy = []
    # right_busy: (finish_time, index)
    right_busy = []

    cur_time = 0
    boxes_left = n

    while boxes_left > 0 or right_wait or right_busy:
        # Move workers from busy to wait if they finished their tasks
        while left_busy and left_busy[0][0] <= cur_time:
            _, i = heapq.heappop(left_busy)
            heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))

        while right_busy and right_busy[0][0] <= cur_time:
            _, i = heapq.heappop(right_busy)
            heapq.heappush(right_wait, (-(time[i][0] + time[i][2]), -i))

        # Try to move someone across the bridge
        if right_wait:
            eff, neg_i = heapq.heappop(right_wait)
            i = -neg_i
            cur_time += time[i][2]
            heapq.heappush(left_busy, (cur_time + time[i][3], i))
        elif boxes_left > 0 and left_wait:
            eff, neg_i = heapq.heappop(left_wait)
            i = -neg_i
            cur_time += time[i][0]
            heapq.heappush(right_busy, (cur_time + time[i][1], i))
            boxes_left -= 1
        else:
            # Jump to the next event
            next_time = float('inf')
            if left_busy: next_time = min(next_time, left_busy[0][0])
            if right_busy: next_time = min(next_time, right_busy[0][0])
            if next_time != float('inf'):
                cur_time = max(cur_time, next_time)

    return cur_time
```
</details>
