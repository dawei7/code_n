## General

**Every subtree has a forced net coin flow**

Each node ultimately needs one coin. For a subtree, compare initial coins with node count.

Their difference is its balance:

- positive means extra coins must leave through the parent edge;
- negative means coins must enter;
- zero means it balances internally.

DFS returns this balance.

**Base case**

An empty subtree has zero nodes and coins, so balance zero.

This lets a leaf combine two zero child balances naturally.

**Combine child balances**

Recursively obtain `left` and `right`.

Each child subtree's net balance must cross its connecting edge.

If left is three, three coins move upward. If minus three, three move downward. Either way exactly `abs(left)` moves use that edge.

The code adds `abs(left) + abs(right)` to `ans`.

**Return current balance**

Current subtree contains child balances plus `root.val` coins and needs one for the root.

Its balance is:

`left + right + root.val - 1`.

The parent later accounts for movement of this amount across their edge.

**Trace**

For `[3, 0, 0]`:

- Each empty child contributes zero.
- Each zero-valued leaf returns minus one.
- Root adds two edge moves.
- Root balance is `-1 - 1 + 3 - 1 = 0`.

One coin crosses each child edge.

For `[0, 3, 0]`:

- Left child returns two.
- Right child returns minus one.
- Root adds `2 + 1 = 3` moves.

Two coins cross from left to root, and one crosses to right.

**Why edge cost is unavoidable**

A subtree connects to the rest through exactly one parent edge.

If it has surplus `d`, those coins must cross out because every internal node keeps only one. If deficit `d`, that many must cross in.

Thus `abs(balance)` is a lower bound and an achievable flow for that edge.

**Why summing flows is globally optimal**

Every move traverses one edge and costs one. Required net flow across each edge is uniquely determined by the child subtree balance.

Summing absolute flows counts the minimum necessary moves across all edges. Tree paths can realize these flows, so the lower bound is achievable.

**Why root balance is zero**

The whole tree has `N` coins and `N` nodes, so total balance is zero.

No coins cross an imaginary edge above the root. The code calls DFS for its accumulated side effect and ignores the returned root balance.

**Why postorder is essential**

The current node cannot know a child's surplus or deficit until that subtree is analyzed. Children are processed before the parent calculation.

**Why direction does not affect cost**

Moving one coin parent-to-child and child-to-parent each count as one move. Absolute value discards flow direction while retaining exact number of crossings.

The signed balance is still returned because the parent must know whether it receives or supplies those coins.

**Why each edge is counted once**

The balance of a child is charged when its parent processes that child. No descendant charges the same parent edge, and no ancestor charges it again.

Therefore, adding both child absolute balances at every node partitions the total move count by unique tree edges.

**Conservation of coins inside a subtree**

Internal moves between two nodes of the same subtree do not change the subtree's total coin count. Only movement across its parent edge can change that total.

This conservation law proves the returned balance is unavoidable regardless of the detailed sequence of moves chosen inside the subtree.

**Why local balancing sequences are compatible**

After recursively arranging child subtrees so only their net surpluses or deficits remain, the current node can pass coins between child edges and its parent edge.

Because a tree has no cycles, these flows do not conflict. Processing from leaves upward supplies exactly the amounts demanded by every lower subtree.

**Moves versus coins**

One coin traveling across two edges costs two moves. The algorithm counts it once in the absolute balance of each crossed child edge.

This explains why summing edge crossings, rather than merely counting misplaced coins, produces the correct total.

**The node's own requirement**

Subtracting one in `root.val - 1` reserves exactly one coin for the current node. If the node begins empty, this contributes a deficit; if it has several coins, all but one contribute surplus.

Child balances are added because their excess or demand becomes part of the combined subtree's balance.

## Complexity detail

Let `N` be nodes and `H` height.

Each node is visited once with constant arithmetic, so time is `O(N)`.

Recursion stack uses `O(H)` space: `O(log N)` balanced and `O(N)` for a chain.

## Alternatives and edge cases

- **Simulate coins:** May repeat paths and obscure forced flow.
- **Store coins and nodes separately:** Their difference is sufficient.
- **Single node with one coin:** Zero moves.
- **Leaf with zero:** Returns minus one.
- **Leaf with surplus:** Returns positive excess.
- **Negative balance:** A demand, not invalid state.
- **Total coin guarantee:** Ensures feasibility and root balance zero.
- **Missing children:** Contribute zero.
- **Global `ans`:** Accumulates each edge once.
- **Deep tree:** Recursion may hit Python's limit.
