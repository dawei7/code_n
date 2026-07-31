## General

**Minimum time is Chebyshev distance.** Let $d_x=\lvert\texttt{sx}-\texttt{fx}\rvert$ and $d_y=\lvert\texttt{sy}-\texttt{fy}\rvert$. One move changes either coordinate by at most one, so every route needs at least

$$
d=\max(d_x,d_y)
$$

seconds. This bound is attainable: move diagonally toward the destination while both coordinate differences are positive, then move straight along the remaining coordinate. Thus reaching the destination at all requires $d\le t$.

**Use extra time without losing the destination.** When the endpoints differ, a shortest path contains at least one move. Any one move can be replaced by a two-move detour through a cell adjacent to both its endpoints, adding one second. Further local cycles can add more time, so every duration at least $d$ is attainable.

The only exception occurs when the start already equals the destination. At `t = 0`, no movement is required and the answer is true. At `t = 1`, the mandatory move must leave the cell, so returning in that single second is impossible. For every `t >= 2`, the infinite eight-neighbor grid provides return cycles: move to a neighbor and back in two seconds, and combine two- and three-step cycles for any larger duration. Therefore the answer is `d <= t` except for identical endpoints with `t == 1`.

## Complexity detail

The method evaluates two absolute differences, one maximum, and the special case. It takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Step-by-step simulation:** Moving greedily toward the target can calculate the minimum time, but it performs $O(d)$ iterations even though the distance has a closed form.
- **Breadth-first search:** BFS finds shortest paths on finite graphs, but the grid is infinite and coordinates reach $10^9$; exploring cells is unnecessary and infeasible.
- **Manhattan distance:** Using $d_x+d_y$ ignores diagonal moves and overestimates the required time whenever both coordinates differ.
- **Zero seconds:** The destination is reachable at `t = 0` only when the two cells are already identical.
- **Identical cells at one second:** This is the sole case where `d <= t` is insufficient because staying still is forbidden.
- **Extra seconds for distinct cells:** An added detour makes `t = d + 1` reachable; longer durations can likewise be absorbed without changing the endpoint.
