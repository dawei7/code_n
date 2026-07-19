## General
**Root the tree at the starting vertex.** Build an adjacency list, then traverse states containing a vertex, its parent, elapsed time, and the probability of reaching it. The parent is the only previously visited neighbor because an undirected tree has one unique path from vertex `1` to every vertex.

For a state at `node`, its available choices are the adjacent vertices other than `parent`. If there are `k` such children, each receives `probability / k` one second later. When the target is reached, its probability is valid if the elapsed time is exactly `t`, or if it has no children and the frog can remain there for all unused time. If the target is reached early with a child available, its final probability is zero because the frog must leave.

The tree has a unique root-to-target path. Multiplying the reciprocal choice counts along that path gives exactly the probability carried by the traversal, and the timing rule above determines whether that path leaves the frog at the target at second `t`.

## Complexity detail
Constructing the adjacency list and visiting each relevant tree vertex at most once take $O(n)$ time. The adjacency lists and explicit traversal stack use $O(n)$ space.

## Alternatives and edge cases
- **Second-by-second probability simulation:** Propagate a full probability distribution for all `t` seconds. It is correct but may revisit stationary leaf states and do more work than the single tree traversal.
- **Rescan the raw edges:** Discover every node's neighbors by examining all edges each time, which raises the traversal to $O(n^2)$ time.
- **Target reached too early:** An internal target has probability zero at a later time because the frog must continue to an unvisited child.
- **Leaf reached early:** A leaf retains its arrival probability for every remaining second.
- **Insufficient time:** If the target depth exceeds `t`, the frog cannot reach it.
- **Starting vertex:** Vertex `1` has probability one after positive time only when it has no child; otherwise the frog leaves after the first second.
- **Uniform choice:** Divide only by unvisited children, never by the parent edge.
