## General

Treat each room as a graph vertex and each shared wall as an edge. The relevant state for a room is the earliest known time at which it can be occupied. If the current room is reached at time `time`, moving into a neighbor cannot begin until both `time` has been reached and the neighbor is open. Its candidate arrival time is therefore

$$
\max(\texttt{time},\texttt{moveTime[next_row][next_column]})+1.
$$

This transition is monotone: reaching the current room later can never produce an earlier arrival at its neighbor. Consequently, Dijkstra's greedy rule applies even though the effective edge cost includes waiting. Store each room's best candidate in `distances` and process the smallest candidate from a min-heap.

When a heap entry no longer equals the recorded distance, a better route has already superseded it and the entry can be discarded. Once the destination is removed with its current best distance, no unprocessed route can reach it earlier, so that time is the answer.

## Complexity detail

Let $n$ be the row count and $m$ the column count. The grid graph has $nm$ vertices and fewer than $4nm$ directed neighbor transitions. Each successful relaxation inserts one heap entry, so the time complexity is $O(nm\log(nm))$. The distance matrix and heap require $O(nm)$ auxiliary space.

The benchmark defines size as $nm$, the number of rooms. Its all-open grids force the destination to remain at the final Manhattan-distance layer, exercising the grid-wide priority-queue path. A linear scan for the next unsettled room has $O((nm)^2)$ behavior and is the calibrated slower class.

## Alternatives and edge cases

- **Linear-scan Dijkstra:** Selecting the smallest unsettled distance by scanning every room is correct but takes $O((nm)^2)$ time.
- **Breadth-first search:** Unit travel duration alone is insufficient because room-dependent waiting makes effective transition costs vary.
- **Dynamic programming in row-major order:** Optimal routes may move in any of four directions, so an acyclic table order does not capture all dependencies.
- **Opening versus arrival time:** A move into a room opening at time $t$ may start at $t$ and finishes at $t+1$.
- **Starting room:** The journey begins there at time `0`; `moveTime[0][0]` is not applied as an entry delay.
- **Large opening values:** Arrival times can exceed $10^9$, so fixed small sentinels are unsafe.
- **Stale heap entries:** Multiple relaxations can enqueue the same room; only the entry matching its current distance should be expanded.
