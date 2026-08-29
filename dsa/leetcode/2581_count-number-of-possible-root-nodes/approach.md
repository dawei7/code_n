## General

**A root determines every edge direction**

An undirected tree becomes a rooted tree by directing every edge away from the chosen root. A guess `(u,v)` is correct exactly when that directed edge points from parent $u$ to child $v$.

Recomputing all guess truth values for every possible root would cost $O(ng)$. The solution computes the correct-guess count for root zero once, then moves the root across tree edges. Crossing one edge changes the truth of only guesses about that edge, so each new count is obtained in constant time.

**Build adjacency and directed-guess lookup**

`g` stores both directions of every undirected edge, allowing DFS traversal from any node. `gs` is a Counter keyed by ordered pairs `(u,v)`. Because guesses are unique, each present key has value one, while a missing orientation returns zero automatically.

The Counter makes expressions such as `gs[(i,j)]` safe without membership branches.

**First DFS: score root zero**

`dfs1(0,-1)` treats zero as root. Parameter `fa` is the parent in this temporary rooting, preventing traversal back across the edge just used.

For every child `j` of current node `i`, orientation $i\to j$ is the parent-to-child direction under root zero. Adding `gs[(i,j)]` counts one exactly when Bob guessed that orientation. Recursing covers every tree edge once.

After `dfs1`, global `cnt` equals the number of correct guesses when root is zero.

**What changes when the root crosses one edge**

Suppose the current root is somewhere on node $i$'s side of edge $\{i,j\}$, so in the current rooting $i$ is parent of $j$. Now reroot at $j$.

The edge between them reverses direction: $i\to j$ becomes $j\to i$. Every other edge keeps its orientation. To see why, removing $\{i,j\}$ splits the tree into two components. Inside each component, paths toward the old and new roots leave through the same boundary node, so parent-child relations do not change. Only the bridge edge itself points differently.

Therefore the correct-guess count changes by

$$
-\mathbf{1}[(i,j)\text{ was guessed}]
+\mathbf{1}[(j,i)\text{ was guessed}].
$$

The code performs this as

`cnt -= gs[(i,j)]` and `cnt += gs[(j,i)]`.

**Second DFS: evaluate every possible root**

At entry to `dfs2(i,fa)`, `cnt` is the correct score when $i$ is the root. The statement `ans += cnt >= k` uses Python's boolean-to-integer behavior: true adds one and false adds zero.

For each child `j` in the traversal:

1. adjust `cnt` for rerooting from $i$ to $j$;
2. recursively evaluate every root in $j$'s side;
3. undo both adjustments after returning.

Restoring is essential because the next neighboring subtree must begin from the score for root $i$, not from the score for the previously explored root.

The restoration reverses the arithmetic:

`cnt -= gs[(j,i)]` and `cnt += gs[(i,j)]`.

**Why every root gets the correct score**

The initial score for root zero is exact by direct edge traversal. The unique tree path from zero to any node $r$ provides a sequence of reroot operations. At each step, the update changes exactly the one edge whose orientation reverses. Inductively, when DFS2 reaches $r$, `cnt` equals the truth count for rooting the tree at $r$.

DFS2 visits every node once, so every possible root is tested exactly once. `ans` counts exactly those with at least $k$ correct guesses.

**Small reroot example**

For path $0-1-2$, suppose guesses are $(0,1)$ and $(2,1)$. With root zero, directions are $0\to1\to2$, so only $(0,1)$ is correct and `cnt=1`.

Moving root to one reverses edge $0-1$: subtract guess $(0,1)$ and add nonexistent $(1,0)$, giving zero. Moving from one to two reverses $1-2$: subtract nonexistent $(1,2)$ and add guessed $(2,1)$, giving one. No other edge score changes during either step.

**Why tree structure is crucial**

A tree has exactly one path between any nodes. Rerooting across one edge reverses only that edge because there are no cycles or alternate parent routes. In a general graph, “parent” would require choosing a spanning tree, and this constant-time reroot rule would not directly apply.

## Complexity detail

Let $n$ be the number of nodes and $g$ the number of guesses. Building adjacency takes $O(n)$ time and space because there are $n-1$ edges. Building the Counter takes $O(g)$ expected time and $O(g)$ space.

Each DFS traverses every edge a constant number of times, so total time is $O(n+g)$. Adjacency, guesses, and recursion use $O(n+g)$ space. A path-shaped tree can create recursion depth $O(n)$, which may exceed Python's default recursion limit for $10^5$ nodes; an iterative traversal would avoid that runtime concern.

## Alternatives and edge cases

- **Recompute each root independently:** Running a fresh DFS for every node costs $O(n^2+ng)$ in the worst case.
- **Store guesses in a set:** A set is sufficient because guesses are unique; Counter is used for convenient zero-valued missing lookups.
- **Zero threshold:** Every root has at least zero correct guesses, so the answer is $n$.
- **No qualifying root:** Every `cnt >= k` test is false, leaving `ans=0`.
- **Both orientations guessed:** Rerooting subtracts one and adds one, so the total remains unchanged for that edge.
- **Neither orientation guessed:** Crossing the edge changes no guess score.
- **Leaf root:** DFS2 reaches leaves normally; all path edge orientations have been adjusted along the recursion route.
- **Backtracking restoration:** Failing to undo `cnt` would contaminate sibling-root scores.
- **Deep tree:** Recursive code is mathematically linear but may need a higher recursion limit or iterative conversion in Python.
