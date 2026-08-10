## General

**Every subtree's representatives must cross one parent edge**

Root the country tree at capital city 0. For a non-capital node `b`, every representative in its subtree has only one route to the capital: the edge from `b` toward its parent. They may consolidate into cars before crossing, but all of them must cross that edge.

If the subtree contains `t` representatives and each car has `seats` seats, the minimum number of cars crossing is

$$
\left\lceil \frac{t}{\texttt{seats}}\right\rceil.
$$

Each car crossing one road consumes one liter, so this ceiling is exactly the fuel contribution of that parent edge.

**Postorder subtree counting**

`dfs(a,fa)` returns the number of representatives in the subtree rooted at city `a`. It begins `sz=1` for that city's own representative.

For every neighbor `b` other than the parent:

1. Recursively obtain child subtree size `t`.
2. Add `ceil(t/seats)` to global fuel `ans` for the child-parent road.
3. Add `t` to `sz` so the parent knows the complete representative count below it.

The root call returns a total that is not used because capital's combined representatives do not cross another edge.

**Why consolidation can achieve the ceiling**

Representatives may switch cars freely. Within a child subtree, bring everyone to its root while consolidating whenever paths meet. At the edge to the parent, distribute the `t` people among exactly $\lceil t/seats\rceil$ cars, all full except possibly one.

No fewer cars can carry `t` people due to capacity. Thus the per-edge charge is both a lower bound and achievable.

Because a tree has unique routes, optimizing the car count independently on every edge is consistent: cars can be consolidated again after reaching the parent for the next edge.

Cars themselves do not need to return to their original cities. The rules allow representatives to change cars, so an empty seat can be reused conceptually wherever routes merge. The only invariant crossing an edge is how many representatives must pass and how many seats one car provides.

**Trace a simple star**

If cities 1, 2, and 3 connect directly to capital with five seats, each child subtree has one representative. Each edge needs `ceil(1/5)=1` car crossing, for total three liters. Representatives cannot combine before reaching the capital because their routes meet only at the destination, after the fuel-consuming edges.

In a deeper subtree with two representatives and two seats, one car can cross the edge after they meet, costing one liter rather than two.


For every edge directed child-to-parent, let $t$ be the number of representatives on the child side. Every feasible plan must transport all $t$ across that edge, requiring at least $\lceil t/seats\rceil$ car crossings and liters.

The postorder strategy can realize exactly that number on every edge through consolidation. Summing the independent unavoidable edge costs gives a global lower bound that is simultaneously achievable. The DFS computes each $t$ exactly, so `ans` is the minimum total fuel.

Using integer ceiling division would give `(t+seats-1)//seats`. It returns one for every positive subtree even when seats exceed `t`, and increases only when another full car becomes unavoidable. This matches the physical packing interpretation.

**Empty-road case**

When `roads=[]`, the graph dictionary has no entries for city 0. DFS still starts with `sz=1`, finds no children, and adds no fuel. The capital representative is already at the meeting, so zero is correct.

**Ceiling arithmetic**

The exact source uses `ceil(t/seats)`, which performs floating-point division. Here $t\le10^5$, so it is numerically safe. Integer arithmetic `(t+seats-1)//seats` would avoid floating point entirely.

## Complexity detail

Building adjacency takes $O(N)$ time and space for $N-1$ roads. DFS visits every city and directed adjacency entry once, so time is $O(N)$.

The adjacency list uses $O(N)$ space. Recursion depth is $O(h)$ and can reach $O(N)$ on a path-shaped tree, making total auxiliary space $O(N)$.

With $N=10^5$, recursion may exceed Python's default stack limit. An iterative parent-order traversal would be operationally safer.

## Alternatives and edge cases

- **Iterative leaf aggregation:** Record parents and degrees, then process leaves upward with a queue. It avoids recursion and computes the same subtree counts.
- **Explicit car simulation:** Tracking individual cars is unnecessary; only representative counts and ceiling capacity matter per edge.
- **One seat:** Every representative requires a separate car across every edge on its route.
- **Seats larger than a subtree:** At least one car is still needed for any nonempty child subtree.
- **Capital representative:** It never crosses an edge and adds no fuel directly.
- **Star tree:** Representatives cannot share before traversing their separate capital edges.
- **Deep branches:** Consolidation creates the greatest savings on edges shared near the root.
- **No roads:** Answer remains zero.
- **Floating-point ceiling:** Safe for bounds, though integer ceiling division is clearer.
- **Recursion depth:** A path of $10^5$ cities can overflow Python's call stack despite linear complexity.
