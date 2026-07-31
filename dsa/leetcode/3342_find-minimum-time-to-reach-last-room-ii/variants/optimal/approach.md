## General

Model every room as a vertex and every shared wall as an edge. Reaching a neighbor from a room occupied at `time` requires waiting until the neighbor's opening value if necessary, then spending the duration of the next move. This gives the candidate arrival

$$
\max(\texttt{time},\texttt{moveTime[next_row][next_column]})+\textit{duration}.
$$

The alternating duration initially appears to require another state dimension, but the grid is bipartite. Every move flips the parity of `row + column`, and every cycle has even length. Thus every possible path ending at `(row, column)` has step-count parity `(row + column) % 2`: the next move costs one second on even cells and two seconds on odd cells.

The transition is monotone because a later arrival at the current room cannot produce an earlier arrival at its neighbor. Dijkstra's algorithm can therefore store one earliest time per room. Pop the smallest candidate, discard it if a better value has superseded it, relax the four neighbors, and return when the destination is popped with its current distance.

## Complexity detail

Let $n$ and $m$ be the grid dimensions. There are $nm$ rooms and $O(nm)$ neighbor edges. Heap insertion and removal cost $O(\log(nm))$, so the total time complexity is $O(nm\log(nm))$. The distance matrix and heap use $O(nm)$ auxiliary space.

The benchmark's size is $nm$, the room count. All-open square grids keep the destination in the last alternating-duration distance layer, exercising the priority queue across the grid. Replacing the heap with a full scan for the next unsettled room is a correct $O((nm)^2)$ comparison class.

## Alternatives and edge cases

- **Explicit parity state:** Tracking both parities per room remains correct but duplicates states because checkerboard parity already fixes the move number's parity.
- **Linear-scan Dijkstra:** Scanning every unsettled room for the next minimum is correct but needs $O((nm)^2)$ time.
- **Breadth-first search:** Edges do not have one uniform effective cost; duration alternates and waiting depends on the destination.
- **Start-time semantics:** `moveTime[i][j]` constrains when a move toward that room begins, after which the one- or two-second duration is added.
- **Starting room:** The journey already occupies `(0, 0)` at time `0`, so its matrix value is not an entry delay.
- **Large opening times:** The answer may exceed $10^9$, so the distance sentinel and arithmetic must accommodate larger values.
- **Stale heap entries:** A room may be relaxed more than once; expand only an entry equal to the currently recorded minimum.
