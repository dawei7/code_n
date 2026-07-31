## General

The tree's child pointers support downward movement, but infection also moves upward. Record the missing parent edge for every node, then the tree can be traversed as an undirected graph without constructing separate adjacency lists.

**Discover parents and the source.** Traverse the tree once from the root. Store each node's parent and retain the node whose value equals `start`. An iterative queue avoids recursion-depth failure on a legal tree shaped like a chain.

**Spread one layer per minute.** Begin a second breadth-first search at the starting node. From each infected node, consider its left child, right child, and recorded parent. A visited set prevents crossing the same tree edge back and forth. Every queue layer contains exactly the nodes whose shortest distance from the start is the current minute.

The final processed layer is therefore the greatest shortest-path distance from the starting node to any node in the tree. Infection crosses one edge per minute and spreads simultaneously, so no node can be reached earlier than its distance, while breadth-first search proves every node is reached at exactly that time. The last layer index is the required total.

## Complexity detail

Let $n$ be the number of nodes. The parent-building traversal and infection traversal each visit every node once, for $O(n)$ time. Parent records, the queue, and the visited set use $O(n)$ space.

## Alternatives and edge cases

- **Explicit adjacency list:** Add both directions of every tree edge and run BFS. This is also $O(n)$ but stores more containers than a parent map.
- **Single recursive DFS:** A postorder traversal can combine subtree depths and the path from `start`, but its state is less direct and recursion may overflow on a $10^5$-node chain.
- **Repeated full-tree infection scans:** Simulating each minute by rescanning all nodes is correct but can take $O(n^2)$ time on a chain.
- **Single node:** The starting node is the whole tree, so the answer is zero.
- **Start at a leaf:** Infection must be able to travel upward through parent links.
- **Simultaneous spread:** All nodes at one distance are infected in the same minute; processing a BFS layer preserves that timing.
