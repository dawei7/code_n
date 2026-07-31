## General

**Revisiting turns every component edge into a candidate.** Cities $1$ and $n$ lie in the same connected component by guarantee. Consider any road in that component. Starting at city $1$, travel to one endpoint of the road, cross it, return through the connected component as needed, and then continue to city $n$. Because repeated vertices and roads are allowed, this produces a valid path whose score is at most that road's distance.

Conversely, every road used by a path from $1$ lies in city $1$'s connected component. Therefore no path can have a score smaller than the minimum edge distance inside that component, while the detour construction shows that this minimum edge can always be included. The answer is exactly the lightest road in the component, whether or not that road lies on a simple route to city $n$.

Build an undirected adjacency list and run an iterative depth-first traversal from city `1`. Examine every incident road of each reached city, update the minimum distance, and add unseen neighbors to the stack. Edges in disconnected components are never visited and cannot affect a path from `1` to `n`.

## Complexity detail

Let $m = \lvert\texttt{roads}\rvert$. Building the adjacency list and traversing city `1`'s component take $O(n+m)$ time. The adjacency list stores two entries per road, while the visited set and stack store at most $n$ cities, for $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Union-Find:** Unite every road's endpoints, then scan roads incident to city `1`'s final component. This also takes near-linear time but requires a second road pass.
- **Repeated full-edge relaxation:** Expanding the reachable set by rescanning every road until no city changes is correct but can take $O(nm)$ time on an adversarially ordered chain.
- **Shortest-path algorithms:** Dijkstra's algorithm optimizes additive distance, whereas this contract minimizes the smallest edge deliberately encountered; it solves a different objective.
- **Low edge on a detour:** It still determines the answer because the path may visit it and return before proceeding to city `n`.
- **Disconnected low edge:** A road outside city `1`'s component cannot occur on a valid path and is ignored.
- **Single connecting road:** With two cities and one road, that road's distance is the score.
- **Cycles and duplicate visits:** The visited set prevents traversal work from repeating even though the conceptual witness path may revisit nodes.
