## General

View each cell as a graph vertex connected to its four orthogonal neighbors. Moving into a neighbor has cost equal to that neighbor's value, either zero or one. The starting cell is also visited, so its value initializes the cost at `(0, 0)`.

The walk is safe exactly when the minimum total number of visited `1` cells is strictly less than `health`. Equality is not enough because health must remain positive after every visit, including the destination.

Because every transition cost is zero or one, use 0-1 BFS. Maintain the least known unsafe-cell cost for each cell. When a relaxation reaches a zero-valued cell, place it at the front of the deque; when it reaches a one-valued cell, place it at the back. This preserves the same nondecreasing-distance processing property as Dijkstra's algorithm without a heap.

Every relaxation represents a real walk, so the destination label is an achievable cost. Conversely, 0-1 BFS relaxes every edge in the order needed to obtain shortest binary-weight distances; therefore, no walk visits fewer unsafe cells than the final label. Comparing that label with `health` gives the required Boolean result.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. The graph has $mn$ vertices and fewer than $4mn$ directed neighbor transitions. 0-1 BFS processes relaxations in $O(mn)$ time. The distance matrix and deque can each hold $O(mn)$ entries, so auxiliary space is $O(mn)$.

## Alternatives and edge cases

- **Dijkstra with a heap:** This is correct for nonnegative weights but costs $O(mn\log(mn))$ time; binary weights permit the faster deque discipline.
- **Ordinary BFS by step count:** The fewest moves need not minimize unsafe cells, so a longer zero-heavy detour can be safer.
- **Depth-first search over paths:** Repeated cells and exponentially many walks make direct path enumeration infeasible.
- **Unsafe starting cell:** Its value must be included before the first move.
- **Unsafe destination:** Entering the final cell also reduces health, and the remaining value must still be positive.
- **Cycles:** Revisiting cells is allowed, but only a strictly cheaper cost triggers another relaxation, preventing useless cycling.
