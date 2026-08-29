## General

**Model detonation as directed reachability**

Bomb `i` directly detonates bomb `j` when the center of `j` lies inside or on `i`'s circular range. This relationship is directional: a large-radius bomb may reach a small-radius bomb even when the reverse is false.

The source builds a directed graph `g`. An edge `i -> j` means detonating `i` directly triggers `j`.

For each unordered pair of bomb indices, it computes the center distance with `hypot(x1 - x2, y1 - y2)`. It then performs two independent radius tests:

- if `dist <= r1`, add edge `i -> j`;
- if `dist <= r2`, add edge `j -> i`.

Both may succeed, one may succeed, or neither may succeed. Using separate conditions rather than `else` preserves all four possibilities.

The inclusive `<=` is important because a bomb exactly on the circle boundary is within range.

**Why graph paths represent chain reactions**

If graph edge `i -> j` exists, detonating `i` triggers `j`. Once `j` detonates, every outgoing edge from `j` becomes active, and so on.

Thus every bomb reachable from a chosen start through a directed path will eventually detonate. Conversely, a bomb can detonate only through such a sequence of direct range relationships, so directed reachability exactly matches the chain reaction.

The task therefore becomes: compute the reachable-set size from every possible starting vertex and take the maximum.

**Traverse from each possible initial bomb**

For start `k`, `vis = {k}` counts the manually detonated bomb itself, and `q = [k]` begins the traversal.

The source uses a Python list as a growing queue:

`for i in q`

iterates over existing entries and also reaches entries appended later. Whenever an unvisited neighbor `j` is found, it is added to `vis` and appended to `q`. This behaves like breadth-first traversal without an explicit deque index.

The visited set prevents cycles from adding a bomb repeatedly or causing an infinite traversal.

After traversal, `len(vis)` is the exact number detonated from `k`. If it equals `n`, no larger answer is possible, so the method returns `n` immediately. Otherwise it updates the best value.

**A directional example**

Suppose bomb A's center is five units from bomb B. If A has radius 3 and B has radius 6, there is edge `B -> A` but no edge `A -> B`. Starting at A detonates only A, while starting at B detonates both.

This explains why an undirected graph would be wrong: physical distance is symmetric, but coverage depends on the source bomb's radius.

**Why the result is correct**

The pairwise construction adds edge `i -> j` if and only if bomb `j` lies in bomb `i`'s range. For a fixed start, traversal visits exactly every vertex connected by a directed path.

Induction on path length shows every visited bomb detonates: the start detonates manually, and each later vertex is triggered by a previously detonated predecessor. Conversely, every chain reaction step follows an edge, so no unvisited vertex can detonate.

The method evaluates every allowed initial bomb, so taking the largest reachable-set size gives the maximum possible chain reaction.

**Numerical detail**

The exact source uses floating-point `hypot`. With the stated coordinate bounds this is practical, but comparing squared integer distance,

$$
(x_i-x_j)^2+(y_i-y_j)^2\le r_i^2,
$$

would avoid square roots and boundary-rounding concerns. That alternative does not change the graph reasoning.

## Complexity detail

Let $n$ be the number of bombs and $E$ the number of directed reachability edges.

Graph construction checks every unordered bomb pair and costs $O(n^2)$ time. One traversal costs $O(n+E)$, which is $O(n^2)$ in a dense graph. Repeating from all $n$ starts gives $O(n^3)$ worst-case time, matching the manifest.

The adjacency lists can store $O(n^2)$ edges. One visited set and queue use $O(n)$ more, so auxiliary space is $O(n^2)$.

With the constraint $n <= 100$, the all-start reachability strategy is feasible.

## Alternatives and edge cases

- **Undirected connectivity:** Incorrect because one bomb's radius may reach another without reciprocal reach.
- **Floyd-Warshall transitive closure:** It also costs $O(n^3)$ time and $O(n^2)$ space, but repeated graph traversal is simpler.
- **Run DFS instead of the growing list:** DFS and BFS produce the same reachable set; traversal order does not affect the count.
- **Squared integer distance:** Avoids `hypot` and floating-point boundary comparisons while retaining $O(1)$ work per pair.
- **One bomb:** Its visited set contains itself, so the answer is one.
- **Bomb on the boundary:** `dist <= radius` includes it.
- **Same centers:** Positive radii make both bombs directly reach one another.
- **Cycles:** `vis` prevents repeated processing while still counting every bomb once.
- **Disconnected groups:** Each start reaches only its directed component; trying all starts finds the best group.
- **Early full reachability:** Returning `n` is safe because no answer can exceed the number of bombs.
- **Queue-list behavior:** Python's list iterator observes appended elements, which is why `for i in q` completes the traversal.
- **Input preservation:** The graph is separate; bomb coordinates and radii are not changed.
