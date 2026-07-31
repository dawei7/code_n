## General

**Turn the boundary into one ordered cycle.** Map a point to its clockwise distance from $(0,0)$ along the square's perimeter:

$$
t(x,y)=
\begin{cases}
x, & y=0,\\
\texttt{side}+y, & x=\texttt{side},\\
3\cdot\texttt{side}-x, & y=\texttt{side},\\
4\cdot\texttt{side}-y, & x=0.
\end{cases}
$$

The branch order assigns every corner exactly once. Sorting these positions gives the input points in cyclic boundary order on a perimeter of length $P=4\cdot\texttt{side}$.

**Why circular spacing represents the relevant Manhattan distances.** Among any $k\ge4$ selected points, some adjacent pair in cyclic order has a boundary gap at most $P/k\le\texttt{side}$. Manhattan distance never exceeds the length of a boundary route connecting the same points, so the optimum cannot exceed `side`.

For a tested distance $d\le\texttt{side}$, two points on opposite sides already have Manhattan distance at least `side`, and points on the same or adjacent sides have Manhattan distance equal to their shortest boundary route. Thus requiring every pair's Manhattan distance to be at least $d$ is equivalent to requiring at least $d$ units of perimeter between consecutive selected points, including the closing gap around the cycle. Nonconsecutive selected points have at least one valid consecutive gap on each boundary route between them.

**Binary-search the largest feasible spacing.** Feasibility is monotone: if `k` points can be placed with cyclic gaps of at least $d$, the same points work for every smaller distance. Binary-search $d$ over $[1,\texttt{side}]$.

For one candidate $d$, duplicate the sorted positions after adding $P$. A two-pointer scan computes `next_index[i]`, the earliest later point at least $d$ beyond position `i`. Choosing that earliest possible successor is safe because it leaves at least as much room as every alternative for all remaining choices.

The first successor table represents one greedy jump. Build binary-lifting tables in which level $b$ represents $2^b$ greedy jumps. For every original point as a possible start, apply exactly $k-1$ jumps using the binary representation of $k-1$. This yields the earliest possible last selected point for that start. The start is feasible exactly when this last point exists and lies no later than `start + P - d`, which reserves a closing gap of at least $d$. If any start succeeds, the candidate distance is feasible.

## Complexity detail

Let $n=\lvert\texttt{points}\rvert$. Mapping and sorting cost $O(n\log n)$. For one distance, the monotone two-pointer scan costs $O(n)$, while building and querying the jump tables costs $O(n\log k)$ time and $O(n\log k)$ space. Binary search performs $O(\log\texttt{side})$ feasibility checks, so total time is $O(n\log n+n\log k\log\texttt{side})$ and auxiliary space is $O(n\log k)$.

## Alternatives and edge cases

- **Try every start with direct greedy jumps:** Reusing the same successor table but taking up to $k-1$ jumps per start costs $O(nk)$ per feasibility check. It is valid under the small bound $k\le25$, but binary lifting gives the sharper $O(n\log k)$ check.
- **Scan forward separately from every start:** Searching through the doubled array again for each start can cost $O(n^2)$ per tested distance.
- **Use Euclidean distance:** The contract asks for Manhattan distance; squared Euclidean comparisons produce different orderings and answers.
- **Treat perimeter distance as Manhattan distance without the bound:** Opposite-side points can have a shorter Manhattan route through the square's interior. The reduction is valid here because $k\ge4$ proves the searched optimum is at most `side`.
- **Forget the closing gap:** A linear greedy chain may space its internal choices correctly while placing its last point too close to the first across the perimeter seam.
- **Map a corner twice:** Each input point is unique, but careless independent edge tests can give a corner multiple perimeter coordinates. The ordered conditions make the mapping single-valued.
- **Minimum square:** When `side = 1`, the constraints force the four corners and `k = 4`, so the answer is $1$.
- **Sparse boundary input:** Only coordinates present in `points` may be selected; the algorithm never invents intermediate perimeter locations.
