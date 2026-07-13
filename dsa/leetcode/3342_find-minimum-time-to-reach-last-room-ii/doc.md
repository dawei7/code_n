# Find Minimum Time to Reach Last Room II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3342 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-minimum-time-to-reach-last-room-ii](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/).

### Goal
Given a 2D grid representing move times, calculate the minimum time required to travel from the top-left cell (0, 0) to the bottom-right cell (n-1, m-1). Moving to an adjacent cell takes time equal to the maximum of the cell's value plus one, or the current time plus one. Crucially, the time cost alternates between adding 1 and adding 2 to the required wait time for each consecutive step taken.

### Function Contract
**Inputs**

- `moveTime`: A 2D list of integers where `moveTime[i][j]` represents the earliest time you can enter cell `(i, j)`.

**Return value**

- An integer representing the minimum time to reach the bottom-right corner.

### Examples
**Example 1**

- Input: `moveTime = [[0,3,2],[0,2,4]]`
- Output: `3`

**Example 2**

- Input: `moveTime = [[0,0,0],[0,0,0]]`
- Output: `3`

**Example 3**

- Input: `moveTime = [[0,1],[1,2]]`
- Output: `4`

---

## Solution
### Approach
Dijkstra's Algorithm. Since the edge weights are dynamic and depend on the number of steps taken (parity of the path length), we expand the state space to `(time, r, c, parity)` to ensure we always find the shortest path in a graph with non-negative edge weights.

### Complexity Analysis
- **Time Complexity**: `O(N * M * log(N * M))`, where N and M are the dimensions of the grid, due to the priority queue operations.
- **Space Complexity**: `O(N * M)`, required to store the minimum time to reach each cell for both parity states.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(moveTime: list[list[int]]) -> int:
    rows = len(moveTime)
    cols = len(moveTime[0])

    # dist[r][c][parity] stores the min time to reach (r, c)
    # where parity is (steps_taken % 2)
    # parity 0: next move adds 1, parity 1: next move adds 2
    dist = {}

    # Priority Queue stores (current_time, r, c, parity)
    pq = [(0, 0, 0, 0)]
    dist[(0, 0, 0)] = 0

    while pq:
        curr_time, r, c, parity = heapq.heappop(pq)

        if curr_time > dist.get((r, c, parity), float('inf')):
            continue

        if r == rows - 1 and c == cols - 1:
            return curr_time

        # Determine the time increment based on parity
        # parity 0 -> next move adds 1, parity 1 -> next move adds 2
        increment = 1 if parity == 0 else 2
        next_parity = 1 - parity

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                # The time to enter the next cell is max(moveTime[nr][nc], curr_time) + increment
                arrival_time = max(moveTime[nr][nc], curr_time) + increment

                if arrival_time < dist.get((nr, nc, next_parity), float('inf')):
                    dist[(nr, nc, next_parity)] = arrival_time
                    heapq.heappush(pq, (arrival_time, nr, nc, next_parity))

    return -1
```
</details>
