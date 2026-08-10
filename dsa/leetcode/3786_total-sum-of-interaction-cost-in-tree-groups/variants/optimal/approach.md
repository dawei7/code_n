## General

**Count how many valid paths use each edge**

The distance between two tree nodes is the number of edges on their unique path. Instead of computing every same-group pair's path separately, reverse the summation:

- each valid pair contributes one for every edge on its path;
- for each edge, count the same-group pairs whose path crosses it;
- sum those counts over all edges.

Removing one tree edge splits the tree into two components. A pair's path crosses that edge exactly when its endpoints lie on opposite sides.

**Root the tree to name the two sides**

The source builds an undirected adjacency list and roots the tree at node zero. `parent` records the edge toward the root, and `order` stores parents before children.

Iterating over the growing `order` list visits every node. For each neighbor, the parent edge is skipped; because the input is a tree, every other neighbor is a new child.

For a non-root node `u`, cutting edge $(parent[u],u)$ separates `u`'s rooted subtree from the rest of the tree. This supplies the two components needed for edge counting.

**Know the total population of every group**

`totals = Counter(group)` records how many nodes carry each label. Labels are constrained to 1 through 20.

`subtree[u][label]` will hold the number of nodes of that label in `u`'s rooted subtree. The source uses a fixed list of 21 counters per node so the label itself can be the index and position zero remains unused.

**Build subtree counts from leaves upward**

Nodes are processed in `reversed(order)`, ensuring every child has already merged its completed vector into its parent before the parent is finalized.

At node `u`, the source first adds the node itself:

`subtree[u][group[u]] += 1`.

For a non-root node, its vector now represents the complete component below edge $(parent[u],u)$. After counting that edge's contribution, every label count is added into the parent's vector.

The root has no parent edge, so it skips edge contribution and merging.

**Count separated same-label pairs for one edge**

Fix the parent edge above node `u` and group label $g$. Let

$$
c=\texttt{subtree}[u][g]
$$

be the number of group-$g$ nodes below the edge. The other side contains

$$
T_g-c
$$

such nodes, where $T_g=\texttt{totals}[g]$.

Choosing one endpoint from each side produces

$$
c(T_g-c)
$$

unordered same-group pairs whose unique path crosses this edge. The source adds this quantity for labels 1 through 20.

There is no division by two. The two sides play distinct roles—one endpoint below, one outside—so each separated unordered pair is formed exactly once for this edge.

**Why summing edge contributions equals total distance**

Take any unordered same-group pair $(x,y)$ whose path length is $d$. Removing any one of the $d$ path edges separates $x$ and $y$, so the pair appears once in that edge's product.

Removing an edge outside the path leaves both endpoints in the same component, so the pair contributes nothing there. Across the entire algorithm, this pair is therefore counted exactly $d$ times, equal to its interaction cost.

Summing over all labels and edges counts every required pair exactly once per path edge and excludes different-group pairs completely. The accumulated `answer` is the requested distance sum.

**Trace a three-node chain**

For chain $0-1-2$ with all nodes in group one, total population is three.

The edge above node two has subtree count one, contributing $1(3-1)=2$: pairs $(2,1)$ and $(2,0)$ cross it.

After merging, the edge above node one has subtree count two, contributing $2(3-2)=2$: pairs $(1,0)$ and $(2,0)$ cross it.

Total contribution is four, matching distances one, one, and two.

**Why fixed label iteration is linear**

The source loops through all 20 possible labels for every non-root node, even if most are absent. Since 20 is a constraint-bounded constant, this is $20(N-1)=O(N)$ work.

If labels were unbounded, storing and merging sparse maps would require a different complexity discussion. Here the dense vectors make operations predictable.

## Complexity detail

Building the adjacency list and rooted traversal takes $O(N)$ time because a tree has $N-1$ edges. The reverse pass performs 20 constant-time label operations per non-root node, so it is also $O(N)$ under the fixed group range.

Total time is $O(N)$.

The adjacency list stores $O(N)$ entries. The parent and order arrays use $O(N)$ space, and `subtree` stores 21 integers per node, also $O(N)$. Total auxiliary space is $O(N)$.

The answer can be large—many pairs may cross many edges—so fixed-width implementations need a 64-bit integer.

## Alternatives and edge cases

- **Run a path search for every same-group pair:** This can require quadratic pairs and linear work per path.
- **Lowest common ancestor distances:** LCA can answer individual distances quickly, but enumerating all within-group pairs can still be quadratic.
- **Count all pairs crossing an edge:** Group labels must match; summing separately by label enforces this.
- **Divide the product by two:** That would undercount because `c(T-c)` already counts each cross-cut unordered pair once.
- **Process parents before children:** Subtree vectors would be incomplete. Reverse traversal is essential.
- **Forget the node itself:** Each subtree count must include its root node before its parent edge is evaluated.
- **Single-node tree:** There are no edges or unordered pairs, so answer remains zero.
- **Every label unique:** All products are zero because no same-group pair exists.
- **All nodes one group:** The method becomes the standard sum of all tree-pair distances by edge cuts.
- **A group appearing once:** Its count products are always zero.
- **Root choice:** Any root defines valid edge cuts and yields the same total.
- **Fixed labels 1 through 20:** Index zero is intentionally unused.
- **Iterative traversal:** It avoids recursion-depth failure on a long chain.
- **Input preservation:** The graph and count arrays are derived without modifying `edges` or `group`.
