## General

**Convert good and bad nodes into additive weights**

Assign weight $+1$ to a good node and $-1$ to a bad node. Then the score of any selected connected subgraph is simply the sum of its node weights.

For each required node `u`, the subgraph must contain `u`, but every branch connected to `u` is optional. A branch should be included only when its best connected contribution is positive. This observation leads to tree dynamic programming, followed by rerooting so every node can receive contributions from all directions.

**Build an undirected adjacency list**

Each edge is stored in both directions in `graph`. The input is a tree, so it is connected and contains exactly $N-1$ edges.

The source temporarily roots the tree at node zero. It creates `parent` and an `order` list beginning with zero. Iterating directly over `order` is intentional: as each node is processed, its children are appended, so the loop eventually visits the whole tree.

For a neighbor equal to `parent[node]`, traversal skips the edge back toward the root. Because a tree has no cycles, every other neighbor is an unvisited child; no separate visited set is needed. The resulting `order` places every parent before its children.

The choice of root does not constrain the final answer. Rooting only gives names to the two sides of each edge so the two passes can be organized.

**First pass: find the best contribution below each node**

`downward[u]` is initialized to node `u`'s own weight. Processing nodes in reversed traversal order ensures every child has already been solved before its parent.

The recurrence is

$$
\texttt{downward}[u]
=
\sum_{v\text{ child of }u}
\max(0,\texttt{downward}[v]).
$$

`downward[v]` is the maximum score of a connected selection entirely inside `v`'s rooted subtree that must contain `v`. If `u` includes anything from that child subtree, connectivity forces the selection to cross edge $(u,v)$ and include `v`. The best available contribution is therefore `downward[v]`.

When that contribution is positive, attaching it improves `u`'s score. When it is zero or negative, omitting the entire child side is at least as good. Different child subtrees meet only at `u`, so all positive contributions can be included independently while preserving connectivity.

The loop `reversed(order[1:])` excludes the root because each processed node adds its completed value into its parent. After the pass, every `downward[u]` is the best anchored score available from the descendant side of `u`.

**Second pass: expose the parent side to each child**

Initially, `answer = downward[:]`. The root already has its full-tree answer because every other node lies in one of its descendant subtrees.

For a parent `u` and child `v`, `answer[u]` contains the best connected contribution around `u` from every useful direction. It may include `v`'s positive downward contribution. Before passing information back across edge $(u,v)$, that child contribution must be removed:

`parent_side = answer[u] - max(0, downward[v])`.

This subtraction prevents `v`'s own subtree from being counted twice. What remains is the best connected score containing `u` using the side of the cut edge outside `v`'s subtree: node `u` itself, a useful contribution received from `u`'s parent, and useful contributions from `v`'s siblings.

Child `v` may attach that outside component only through edge $(u,v)$. It is beneficial exactly when `parent_side` is positive, so the source performs

`answer[v] += max(0, parent_side)`.

Because `order` visits parents before children, `answer[u]` already includes its own parent-side information when it is used to update `v`. Information therefore flows outward from the original root during this pass.

**Understand the edge-cut decomposition**

Removing edge $(u,v)$ splits the tree into exactly two components. Any connected subgraph containing `v` can use:

- a connected selection on `v`'s side that contains `v`, represented by `downward[v]`;
- optionally, a connected selection on `u`'s side that contains `u`, represented by `parent_side`.

If the second part is used, the removed edge reconnects the two anchored pieces. There is no third route between the components because the graph is a tree.

The best total is therefore

$$
\texttt{downward}[v]+\max(0,\texttt{parent\_side}),
$$

which is exactly the update stored in `answer[v]`. Applying this relation to every parent-child edge gives the optimum for every possible required node.

**Trace a three-node chain**

For weights $[+1,-1,+1]$ on chain $0-1-2$, the bottom-up pass gives:

- `downward[2]=1`;
- `downward[1]=-1+max(0,1)=0`;
- `downward[0]=1+max(0,0)=1`.

The root answer is one. Passing from 0 to 1 gives parent-side value $1-0=1$, so `answer[1]=0+1=1`. Passing from 1 to 2 removes 2's positive downward value from `answer[1]`, leaving zero, so `answer[2]` remains one.

All three answers are one, matching the whole tree's score. Notice that a downward value of zero can become a positive full-tree answer after receiving information from above.

**Never discard the required node itself**

The `max(0, ...)` operation applies only to optional neighboring components. A node's own initial weight is never clamped away because every candidate for `answer[u]` must contain `u`.

If every node is bad, each downward value stays -1: attaching another negative branch would only lower the score. The second pass also rejects negative parent sides, so every answer is -1 rather than zero. This correctly reflects that at least the required bad node must be selected.

## Complexity detail

Building the adjacency list takes $O(N)$ time and stores $2(N-1)$ neighbor entries. Rooting the tree visits every node and edge once. The reversed downward pass and forward reroot pass also process each parent-child relation a constant number of times.

Total time is $O(N)$.

The adjacency list, `parent`, `order`, `downward`, and `answer` arrays each use $O(N)$ space, so total auxiliary space is $O(N)$. The iterative traversal avoids recursion-stack depth problems on a chain of up to $10^5$ nodes.

## Alternatives and edge cases

- **Run a fresh search for every required node:** Recomputing the best connected subgraph $N$ times can cost $O(N^2)$. Rerooting reuses both sides of every edge.
- **One bottom-up pass only:** `downward[u]` ignores useful nodes above `u`, so it is complete only for the chosen root.
- **Clamp the entire node score to zero:** The required node cannot be omitted. Only optional branch contributions are clamped.
- **Add every neighboring branch:** A negative anchored contribution lowers the score and should be excluded.
- **Forget to subtract the child contribution:** Passing `answer[u]` unchanged to child `v` would count `v`'s own downward component once in `answer[v]` and again through the parent side.
- **Use `downward[u]` instead of `answer[u]` in the second pass:** That loses information arriving from `u`'s parent and gives incorrect answers deeper in the tree.
- **All nodes good:** Every branch is positive, so every answer equals `N` and the whole tree is optimal.
- **All nodes bad:** Every answer is -1 because the required node must remain and all other nodes hurt.
- **Zero-valued anchored branch:** Including or excluding it ties; `max(0, ...)` safely contributes zero.
- **Leaf node:** Its downward value starts as its own weight, then the reroot pass may add a positive component from the rest of the tree.
- **Original root:** Its downward value already sees every incident direction, so `answer[0]` needs no parent-side addition.
- **Arbitrary root choice:** Rooting at zero changes intermediate parent/child labels but not the edge-cut recurrence or final answers.
- **Deep chain:** Iterative order construction avoids exceeding Python's recursion limit.
- **Valid-tree guarantee:** Skipping only the parent edge is safe because there are no cycles. A general graph would require visited tracking and a different connected-subgraph algorithm.
- **Multiple maximizing subgraphs:** The DP returns only the maximum score; it does not need to reconstruct which tied branches were chosen.
