## General

**Precompute when water reaches each empty cell**

Initialize one queue with every `*` cell at time zero. A multi-source breadth-first search spreads only into `.` cells, recording the earliest flood time of each. Stones block propagation, and neither `S` nor `D` is an empty flood target; the destination is explicitly guaranteed never to flood.

**Search traveler states under strict deadlines**

Run a second BFS from `S`. Reaching an adjacent empty cell at time $t+1$ is legal only when $t+1$ is strictly less than that cell's flood time. Equality is rejected because the traveler cannot step onto a cell flooding during the same second. The destination may be entered directly because it never floods.

BFS explores positions in nondecreasing travel time, so the first arrival at `D` is the minimum safe time. Marking a cell seen on its first safe arrival is sufficient: any later arrival has less remaining time before flooding and cannot enable a route that the earlier arrival could not follow. If the queue empties, every feasible movement sequence has been exhausted and the answer is `-1`.

Separating flood propagation from movement avoids mutating the grid second by second. The precomputed deadline matrix captures the complete future water process, and the traveler BFS enforces those deadlines locally.

## Complexity detail

Let $N=rc$ be the number of cells. Each BFS visits every traversable cell and its constant number of grid edges at most once, so total time is $O(N)$. The flood-time matrix, queues, and visited set use $O(N)$ space.

## Alternatives and edge cases

- **Simulate the entire grid each second:** This is source-faithful but repeatedly scans unchanged cells and can take superlinear time.
- **Single mixed queue without event ordering:** Interleaving water and traveler states is error-prone because water for a second must invalidate simultaneous arrivals.
- **Traveler BFS without flood times:** Avoiding only initially flooded cells ignores future drowning.
- Arrival time equal to a flood time is unsafe; use a strict inequality.
- Stones block both movement and water.
- The destination is always safe from flooding and may be entered even when adjacent empty cells are threatened.
- Flooding spreads into `.` cells only, so an isolated source behind stones remains isolated.
- A destination adjacent to `S` is reached in one second.
