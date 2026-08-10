## General

**Why running a traversal from every node is too expensive**

For one chosen node, a DFS or BFS can find its distance to all others in `O(n)` time. Repeating that for all `n` nodes costs `O(n^2)`, which is too slow for 30,000 nodes.

The tree structure lets us reuse one node's answer for each neighboring node. The optimal solution performs two traversals:

1. root the tree at node 0, compute subtree sizes, and compute the distance sum for node 0;
2. move the conceptual root across every edge and derive each child's distance sum from its parent's in constant time.

This technique is called rerooting dynamic programming.

**Build an undirected adjacency list**

For each edge `[a,b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Both directions are required because the input tree is undirected.

The recursive functions receive `fa`, the parent node from which they arrived. When examining adjacency list neighbors, `j != fa` prevents walking immediately back across the same edge. A valid tree has no other cycles, so a separate visited set is unnecessary.

**First traversal: compute the answer for root 0**

`dfs1(i, fa, d)` visits node `i` at depth `d` from node 0.

The statement `ans[0] += d` adds that node's distance from 0. Every node is reached once, so after the traversal:

$$
\texttt{ans}[0]=\sum_{v=0}^{n-1}\operatorname{dist}(0,v).
$$

The root contributes depth zero, which correctly has no effect.

**First traversal: compute subtree sizes at the same time**

When DFS enters node `i`, it sets `size[i] = 1` to count the node itself. After recursively processing child `j`, it adds `size[j]`.

Once all children are finished, `size[i]` equals the number of nodes in the subtree rooted at `i` under the chosen root 0. Postorder timing is important: a child's complete size must be known before its parent adds it.

These sizes are exactly the information needed to move a distance sum across an edge.

**What changes when the root moves from a parent to a child**

Suppose the current root is node `i` and `j` is one of its children in the root-0 orientation. Let `t` be the sum of distances from `i` to every node.

When we move the root one edge from `i` to `j`, divide the tree into two groups:

- the `size[j]` nodes inside `j`'s subtree;
- the remaining `n - size[j]` nodes outside it.

For every node inside `j`'s subtree, the new root `j` is one edge closer than `i` was. Each distance decreases by one, changing the total by `-size[j]`.

For every node outside that subtree, traveling from `j` must first cross the edge back to `i`. Each distance increases by one, changing the total by `+(n-size[j])`.

Therefore,

$$
\text{answer}[j]
=t-\texttt{size}[j]+(n-\texttt{size}[j]).
$$

Equivalently,

$$
\text{answer}[j]=t+n-2\cdot\texttt{size}[j].
$$

The exact call

`dfs2(j, i, t - size[j] + n - size[j])`

passes this derived child total.

**Second traversal: propagate every answer**

`dfs2(i, fa, t)` begins by setting `ans[i] = t`. For each child `j`, it calculates the rerooted total using `size[j]` and recurses.

At the starting call, `t = ans[0]` from the first traversal. Each tree edge is then crossed from parent to child once, so the formula eventually assigns an answer to every node.

Although subtree sizes were defined with root 0, they remain exactly the correct partition sizes for crossing the parent-child edge in that orientation. Removing an edge always creates the same two components; `size[j]` is the component on `j`'s side.

**Trace the six-node example**

Rooting at 0 gives edges to 1 and 2, while node 2 has children 3, 4, and 5.

The first traversal computes:

- `size[1] = size[3] = size[4] = size[5] = 1`;
- `size[2] = 4`;
- `size[0] = 6`.

Depths from 0 sum to `0+1+1+2+2+2=8`, so `ans[0]=8`.

Rerooting from 0 to child 2 gives

$$
8-4+(6-4)=6.
$$

Four nodes in node 2's side become one step closer, while nodes 0 and 1 become one step farther. This matches `answer[2]=6`.

Rerooting from 2 to leaf 3 gives

$$
6-1+(6-1)=10.
$$

The one-node subtree containing 3 becomes closer, while the other five nodes become farther, matching the expected answer.

**Why both traversals are correct**

The first DFS directly sums correct root-0 depths and uses standard postorder accumulation to obtain exact component sizes.

For the second DFS, assume parent `i` has the correct distance total `t`. The edge-partition argument accounts for every node exactly once and derives the correct total for child `j`. By induction along paths from node 0, every propagated value is correct. Because the tree is connected, all nodes are reached.

## Complexity detail

The adjacency list stores two entries per edge, or `2(n-1) = O(n)` space and construction time.

Each DFS visits every node once and examines every adjacency entry a constant number of times. Two linear traversals remain `O(n)` total time.

The adjacency list, `ans`, and `size` each use `O(n)` space. Recursive call depth is at most the tree height, which is `O(n)` for a chain. Total auxiliary space is `O(n)`.

With up to 30,000 nodes, a path-shaped tree can exceed Python's default recursion depth unless the execution environment adjusts it. Iterative traversal with an explicit parent/order array implements the same two passes and avoids that language-level stack limit; the exact protected solution is recursive.

## Alternatives and edge cases

- **BFS or DFS from every node:** It is simple but takes `O(n^2)` time.

- **All-pairs shortest paths:** General graph algorithms ignore the tree's unique paths and are far more expensive.

- **Iterative rerooting:** Build parent and traversal order with a stack, process reverse order for sizes, then forward order for answers. It preserves `O(n)` time and avoids recursion limits.

- **Single node:** The first depth is zero, `size[0]=1`, and the answer is `[0]`.

- **Two nodes:** Root 0 has total 1; rerooting across the one-node child gives `1-1+(2-1)=1`.

- **Path-shaped tree:** Subtree sizes vary along the path, and rerooting shifts the distance total by the appropriate imbalance at each edge.

- **Star-shaped tree:** Moving from the center to a leaf decreases one distance and increases the other `n-1` distances, which the formula captures.

- **Arbitrary choice of root 0:** Any initial root would work. Node 0 is convenient because labels include it and the output needs every node anyway.

- **Parent filtering:** The input is guaranteed to be a tree, so excluding only `fa` is enough to prevent revisits.

- **Distance to self:** It is zero and is included harmlessly in the sum.

- **Connected-tree guarantee:** Every node is reachable from 0, so both DFS traversals fill all array entries.

- **Input immutability:** The edge list is read into a new adjacency structure and is not modified.
