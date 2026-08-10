## General

**Remove edges that can never be worth traversing**

A closed walk in a tree must traverse every used edge an even number of times: once to enter a branch and once to leave it, because there is no alternate route back.

The goal is therefore to identify the smallest remaining subtree whose edges genuinely need traversal. Every edge in that core costs two moves. The solution finds the core through pruning.

**Build mutable adjacency sets**

`g[node]` is a set of currently remaining neighbors. Sets support removing a pruned neighbor and checking the updated degree.

Clearing a removed node's set marks it as absent from the working tree. The original `edges` list remains available for final counting.

**First phase: prune coinless leaves repeatedly**

A leaf with no coin is useless. Entering its branch cannot collect a coin there or beyond it, because it has no children in the current tree. Any route using that edge can omit the round trip and become shorter.

The initial queue contains all degree-one nodes with `coins[i] == 0`. When one is removed, its neighbor may become a new coinless leaf, so that neighbor is enqueued. This repeats until every remaining leaf has a coin.

This phase removes entire branches containing no coin, not just their original outermost nodes.

**Why coinless internal nodes may remain**

A zero-coin node can connect paths to coins in different branches. It should not be removed merely because it has no coin. Only when pruning reduces it to a leaf with no coin does its branch become unnecessary.

The degree test captures this distinction.

**Second phase: remove two boundary layers**

After useless branches are gone, every remaining leaf carries a coin. The collector can collect coins within distance two without walking all the way to their nodes.

Therefore the outermost coin-leaf layer does not require traversal, and neither does the next layer behind it. The code performs exactly two rounds:

1. take a snapshot of every current degree-one node;
2. remove all those nodes and their incident edges.

Using a snapshot per round is crucial. Newly created leaves must wait until the next round; otherwise one loop could peel arbitrarily many layers instead of exactly two.

**Why two layers correspond to collection radius two**

Suppose the route visits a node in the remaining core. Any original coin sitting on a node removed in the last two boundary rounds is at distance at most two from that visited core, so it can be collected without traversing its final one or two edges.

Coins farther inward determine the core that must actually be visited. Removing more than two layers could leave a coin at distance greater than two from every visited position and would be invalid.

If all nodes disappear, some starting vertex can collect all relevant coins without moving, so the correct cost is zero.

**Why every remaining edge must be crossed**

After both pruning stages, consider a remaining edge. Removing it divides the core into two nonempty sides, each connected to coin obligations that cannot all be collected from the other side within radius two; otherwise one side would have been peeled away.

A route collecting all coins must visit positions on both sides, so it must cross the edge. Because the route returns to its starting vertex and a tree offers no alternate cycle, it must cross back. Each core edge costs exactly two traversals.

A depth-first tour of the remaining core achieves this bound by walking every edge once in each direction, while collecting all coins within distance two along the way.

**Count surviving original edges**

After pruning, a surviving node has a nonempty adjacency set. The final generator examines every original edge `[a,b]` and counts it when both endpoints still have positive degree.

Multiplying by two converts surviving edge count into closed-walk traversals.

Removed nodes have cleared sets, so edges incident to them fail the test.

**Trace a path**

For coins at both ends of a six-node path, no coinless leaf is pruned initially. Removing the first leaf layer deletes both coin endpoints. Removing the second deletes their immediate neighbors. The remaining core is the middle edge.

Traversing that edge out and back costs two. From its endpoints, the original end coins are within distance two and can be collected, matching the example.

## Complexity detail

Let $n$ be the number of nodes. Building adjacency takes $O(n)$ time and space. During repeated coinless pruning, each node is queued at most once and each edge is removed at most once. Each of the two layer rounds scans all nodes and removes boundary edges, still $O(n)$ total. Final edge counting is $O(n)$.

Overall time is $O(n)$ and adjacency plus queues use $O(n)$ space. The input arrays are not modified.

## Alternatives and edge cases

- **Tree dynamic programming:** States can describe coin distances and return costs, but pruning gives a simpler structural solution.
- **Traverse the minimal coin subtree fully:** This ignores the free distance-two collection radius and overcounts its outer two layers.
- **Prune all zero-coin nodes:** Internal zero nodes may be necessary connectors and cannot be removed blindly.
- **No coins:** Coinless-leaf pruning removes the whole tree and the answer is zero.
- **One coin:** After two free layers no traversal is required; start within distance two.
- **Snapshot layers:** Sequential cascading inside one round would remove more than the allowed two layers.
- **Single-node tree:** It has degree zero, no edges survive, and the answer is zero.
- **Return requirement:** It forces every used core edge to be traversed twice rather than once.
- **Mutable sets:** Neighbor removal keeps current degrees accurate throughout pruning.
