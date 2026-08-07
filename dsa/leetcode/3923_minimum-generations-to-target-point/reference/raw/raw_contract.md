## Function Contract

**Inputs**

- `points`: A non-empty list of distinct three-element integer lists representing the generation-$0$ points.
- `target`: A three-element integer list representing the point to find.

Let $n=\lvert\texttt{points}\rvert$. Let $U$ be the number of distinct coordinate triples that eventually enter the reachable closure; the coordinate limits guarantee $U\le7^3=343$.

**Return value**

Return the smallest generation number in which `target` is available. Return `-1` if the closure stabilizes without the target.
