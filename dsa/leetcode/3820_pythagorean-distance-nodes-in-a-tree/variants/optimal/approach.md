## General

**Compute distances from targets rather than from every candidate node**

For each node `u`, the answer needs three distances: from `u` to `x`, `y`, and `z`. An undirected distance is symmetric, so

$$
\operatorname{dist}(u,x)=\operatorname{dist}(x,u),
$$

and similarly for the other two targets.

This symmetry changes the direction of the work. Running a traversal from every possible `u` would repeat nearly the same tree exploration $N$ times and could cost $O(N^2)$. Instead, only three breadth-first traversals are needed:

- BFS from `x` records the distance from `x` to every node;
- BFS from `y` records the distance from `y` to every node;
- BFS from `z` records the distance from `z` to every node.

After those traversals, the three array entries at position `u` are exactly the values needed to classify node `u`.

**Build an undirected adjacency list**

The source creates `g = [[] for _ in range(n)]`. For every edge `[u, v]`, it appends `v` to `g[u]` and `u` to `g[v]`.

Both insertions are required because the tree is undirected. A BFS starting at any target must be able to traverse an edge in either direction, regardless of how the endpoints happened to be ordered in `edges`.

A tree with $N$ nodes has exactly $N-1$ edges, so the adjacency lists contain $2(N-1)$ neighbor entries in total.

**Why breadth-first search gives edge-count distances**

The local `bfs(i)` function initializes every distance to infinity and sets the source's distance to zero. It places only the source in the queue.

Whenever node `u` is removed, an adjacent node `v` can be reached through one more edge, giving candidate distance `dist[u] + 1`. The condition

`dist[v] > dist[u] + 1`

updates `v` only when this route is shorter than the best route recorded so far. The updated neighbor is appended to the queue.

BFS explores an unweighted graph in nondecreasing distance from its source. All paths are measured only by their number of edges, so the first finite distance assigned to a node is its shortest distance. In a tree, the reason is even simpler: there is exactly one path from the source to every node. The traversal follows that unique path and assigns its length.

The outer `while q` contains a `for _ in range(len(q))` loop, which processes one queue layer at a time. The code does not use an explicit layer number because it derives each neighbor's distance from `dist[u]`. Layer grouping is therefore not necessary, but it remains correct.

The relaxation condition plays the role of a visited check. Once a node has its unique shortest tree distance, returning through the opposite direction would propose a larger value and fail the condition. Consequently, each node is enqueued once.

**Keep one complete distance array per target**

The calls `d1 = bfs(x)`, `d2 = bfs(y)`, and `d3 = bfs(z)` produce three aligned arrays. At node index `u`:

- `d1[u]` is $d_x$;
- `d2[u]` is $d_y$;
- `d3[u]` is $d_z$.

The tree is connected, so every entry becomes a finite nonnegative integer. A target's distance to itself is zero. The problem explicitly allows zero in a Pythagorean triplet, so target nodes are not excluded from consideration.

**Find the smallest, middle, and largest of three values**

The Pythagorean condition applies after sorting the three distances as $a\le b\le c$. The source avoids allocating and sorting a three-element list for every node.

It begins with the three aligned values and saves their total:

`s = a + b + c`.

It then assigns

`a, c = min(a, b, c), max(a, b, c)`.

After this simultaneous assignment, `a` is the smallest original distance and `c` is the largest. The middle value is whatever remains after subtracting those two from the total:

`b = s - a - c`.

This formula remains correct when distances are equal. For values 0, 2, and 2, the minimum is 0, the maximum is 2, and the middle becomes $4-0-2=2$. For three equal values, subtracting one chosen minimum and one chosen maximum still leaves the third equal value.

The source then checks

`a * a + b * b == c * c`.

Only exact integer multiplication and equality are used. No square roots or floating-point approximations are needed.

**Zero-distance cases are intentional**

The mathematical definition in this problem does not require all three values to be positive. For a target node, one distance is zero. A sorted triple `(0,p,q)` satisfies the equation exactly when

$$
0^2+p^2=q^2,
$$

which means $p=q$.

This is why each leaf target in the star example is special: its distances are 0, 2, and 2. An implementation that applies the conventional positive-integer restriction sometimes associated with Pythagorean triples would incorrectly reject these nodes. The exact source follows the stated equation and counts them.

**Why every and only special node is counted**

Each BFS array contains the true distance from its target to every node. Symmetry makes those entries the true distances from the candidate node back to the targets.

For every node, the min/max/sum transformation rearranges exactly its three distances without changing a value. The subsequent equality is exactly the definition of a special node. If it holds, `ans` increases once; if it does not, the node contributes nothing.

`zip(d1, d2, d3)` produces one triple for every common index in order. All arrays have length $N$, so every node is tested exactly once and no unrelated distances are combined.

For the first star example, the center produces `(1,1,1)` and fails because $1^2+1^2\ne1^2$. Each target leaf produces a permutation of `(0,2,2)`, which the min/max transformation normalizes and accepts. The result is three.

## Complexity detail

Let $N$ be the number of nodes and $E=N-1$ the number of edges. Building the adjacency list takes $O(N+E)=O(N)$ time. One BFS visits all $N$ nodes and examines both adjacency entries for every edge, costing $O(N+E)=O(N)$. Running it three times multiplies the constant by three but remains $O(N)$.

The final aligned scan performs a constant number of arithmetic operations for each node, adding another $O(N)$. Total time is $O(N)$.

The adjacency list uses $O(N+E)=O(N)$ space. The three distance arrays use $3N$ entries, and one BFS queue can hold $O(N)$ nodes. These coexist, so auxiliary space is $O(N)$. Sorting is simulated with fixed-count min/max arithmetic and does not add growing space.

## Alternatives and edge cases

- **Depth-first distance traversals:** Because the graph is a tree with unique paths, DFS from each target can also assign distances in $O(N)$ time. An iterative DFS avoids recursion-depth failures on a 100,000-node chain.
- **Run BFS from every node:** This computes far more distances than needed and costs $O(N^2)$ on a tree.
- **All-pairs preprocessing:** LCA structures can answer arbitrary pair distances, but building them is unnecessary for only three fixed targets; three linear traversals are simpler and asymptotically optimal.
- **Sort a three-element list:** `sorted((dx, dy, dz))` is clear and still constant work per node. The source's sum/min/max method avoids a tiny allocation and exactly matches its executable behavior.
- **A candidate equals a target:** One distance is zero. It qualifies when the other two distances are equal, because zero is allowed by this problem's definition.
- **Equal distances:** The middle-value formula works even when the minimum or maximum occurs more than once.
- **Path-shaped tree:** BFS remains linear, and its iterative queue avoids the recursion-depth issue a recursive DFS could face.
- **Pairwise-distinct targets:** No node can equal more than one target, but the traversal and equation would still be mechanically defined without this guarantee.
- **Connected-tree guarantee:** Every distance becomes finite. On a disconnected graph, infinity values would require separate handling, but such input is outside the contract.
- **Large squared distances:** A distance is at most $N-1$, and Python integers represent its square exactly without overflow.
- **No special nodes:** `ans` remains zero and is returned directly.
