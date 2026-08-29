## General

When a marked node causes marking to travel to an adjacent node, the delay depends on the node being entered: entering an odd node costs one time unit, while entering an even node costs two. Therefore, if node $s$ is initially marked, the marking time of another node $v$ is the sum of entry costs along the unique tree path from $s$ to $v$, excluding $s$ itself.

Define

$$
w(v)=
\begin{cases}
1,&v\text{ is odd},\\
2,&v\text{ is even}.
\end{cases}
$$

For a path $s=v_0,v_1,\ldots,v_k=v$, its marking time is $\sum_{j=1}^{k}w(v_j)$. All nodes are marked when the slowest destination is marked, so the answer for start $s$ is the maximum such directed, node-weighted path distance from $s$.

Running a traversal independently from every possible start would take $O(n^2)$. The source computes all weighted eccentricities with tree rerooting: first find best paths going down from an arbitrary root, then propagate the best path arriving from outside each subtree.

**Build a rooted view without recursion.** The undirected adjacency list `graph` stores both directions of every edge. The code temporarily roots the tree at node zero. `parent` is initialized to minus one, and `order` begins with zero. Python's `for node in order` loop sees items appended while it runs, so visiting a node and appending every non-parent neighbor produces an iterative parent-before-child traversal of the whole tree. Because the input is a tree, skipping the parent is enough to avoid revisiting nodes.

The traversal order need not be a particular DFS order. What matters is that every parent appears before its children. Reversing `order` then guarantees children are processed before their parent.

**First pass: best path inside each subtree.** `downward[u]` is the maximum marking time from `u` to any node in `u`'s rooted subtree. A leaf has value zero because choosing the leaf itself as the destination takes no time.

For each child `v` of `u`, a path from `u` into `v`'s subtree first enters `v`, costing `w(v)`, and then follows the best downward path beginning at `v`. Its contribution is

`downward[v] + (1 if v % 2 else 2)`.

Taking the maximum over children computes `downward[u]`. The test `parent[neighbor] == node` distinguishes children from the parent in the undirected adjacency list.

**Second pass: include paths outside the subtree.** `upward[u]` stores the best marking time from `u` to any node outside `u`'s rooted subtree. It is zero for root zero because there is no outside destination. When evaluating node `u`, every possible farthest destination is either outside its subtree, represented by `upward[u]`, or inside one child subtree, represented by that child's contribution. The largest of these values is exactly `answer[u]`.

To send information to a child, the method must exclude that child's own downward contribution. Otherwise it would describe a path that leaves the child toward its parent and immediately returns into the same child subtree, which is not a simple tree path and would double-count.

The code finds the largest and second-largest candidates at `u`. It initializes `best` with `upward[u]` and `second_best` with zero. As it scans child contributions, `best_child` remembers which child supplied a strictly new largest value. If a contribution exceeds `best`, the old best moves to `second_best`. If it does not exceed best but does exceed second best, only `second_best` changes. This also handles tied largest child contributions: the second copy becomes `second_best`, so excluding either one still leaves the other equal optimum available.

For child `v`, `outside` is `second_best` if `v` is the unique recorded `best_child`; otherwise it is `best`. From `v`, reaching any such outside destination first enters parent `u`, so the entry cost is based on `u`'s parity:

`upward[v] = w(u) + outside`.

This direction is easy to reverse accidentally. `downward[u]` adds the child's cost because the path enters the child. `upward[v]` adds the parent's cost because the path from child to outside first enters the parent.

For the tree with edges `[[0,1],[0,2]]`, downward contributions at root zero are one through odd node one and two through even node two, so `answer[0] = 2`. For child one, the best route excluding its own branch goes from one into even node zero for cost two, then into even node two for another two, totaling four. For child two, the corresponding route enters node zero for two and node one for one, totaling three. The result is `[2,4,3]`.

**Why the two passes are sufficient.** For any node `u`, rooting at zero partitions all destinations into its child subtrees, the outside portion through its parent, and `u` itself. The downward pass summarizes every child subtree. The upward pass summarizes the complement using the parent's already complete information, with `u`'s own branch excluded. Induction in parent-before-child order proves `upward` correct. Taking the maximum of these exhaustive disjoint directions therefore gives the marking time of the last node for every possible start.

The implementation is entirely iterative for tree construction and DP order, except that reroot propagation is also a loop. It avoids the recursion-depth failure that a recursive DFS could encounter on a chain of $10^5$ nodes.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list takes $O(n)$ time and space because a tree has $n-1$ edges and stores two adjacency entries per edge. The parent traversal examines each adjacency entry once. The reversed downward pass examines them once more, and the reroot pass scans child lists to find the top two contributions and again to assign child `upward` values. A constant number of complete edge scans is still $O(n)$ time.

The adjacency list, `parent`, `order`, `downward`, `upward`, and `answer` each use $O(n)$ storage. Excluding the returned answer does not change the $O(n)$ auxiliary-space bound. No call stack proportional to tree height is used.

All path times are at most $2(n-1)$, because each of at most $n-1$ entered nodes costs at most two. Python integers easily hold this range.

## Alternatives and edge cases

- **Traversal from every start:** A weighted DFS or BFS can compute one answer in $O(n)$, but repeating it for all $n$ starts costs $O(n^2)$ and is infeasible at $10^5$ nodes.
- **Tree diameter endpoints:** In ordinary nonnegative edge-weighted trees, eccentricities can be derived from distances to diameter endpoints. Here path cost is directional because entering `v` costs `w(v)` while the reverse path enters different nodes. A carefully transformed directed-weight method may work, but rerooting expresses the asymmetric node costs directly.
- **Recursive rerooting:** Two recursive DFS functions can implement the same recurrence elegantly. A chain of $10^5$ nodes exceeds Python's default recursion depth, while the explicit `order` avoids that risk.
- **Use only the largest child contribution:** When propagating to that same child, its contribution must be excluded. Without a second-best value, `upward` would incorrectly reuse a path inside the child's own subtree.
- **Tied best children:** The `elif contribution > second_best` branch preserves another equal best as the second best. Excluding one tied child can still use the other.
- **Two-node tree:** The downward and upward formulas reduce to entering the one other node. Starting at zero costs `w(1)=1`, while starting at one costs `w(0)=2`.
- **A chain:** Downward values accumulate toward one end and upward values toward the other. The answer at each node is the larger directional weighted distance.
- **A star:** The center's answer is the most expensive child entry. A leaf's answer may travel through the center and into another leaf, correctly adding the costs of the center and destination leaf.
- **The starting node's parity:** Its cost is never charged at time zero. It is charged only when a path from a different start enters it, exactly as the upward formula does.
- **Valid-tree guarantee:** Skipping only `parent[node]` is safe because there are no cycles. On a general undirected graph, a separate visited check would be necessary during parent construction.
