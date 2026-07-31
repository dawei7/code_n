## General

A level sum cannot be finalized until every node at that depth has been included. Breadth-first search exposes exactly that boundary: at the start of an iteration, the queue contains all and only the nodes of the current level.

Record the queue length, remove exactly that many nodes, and add their values. Each removed node contributes its non-null children to the queue, which therefore becomes the complete next level after the fixed-size loop. This preserves the level-boundary property from the root through the entire tree.

After computing a level's sum, compare it with the smallest sum seen so far. Replace both the best sum and answer level only when the new sum is **strictly** smaller. Levels are processed in increasing numerical order, so refusing to update on equality retains the smallest level number required by the tie rule.

Every node is enqueued once from its unique parent and processed once at its unique level. Thus each level sum is exact, every level is considered, and the stored answer is the earliest level attaining the global minimum.

## Complexity detail

Let $n$ be the number of nodes and let $w$ be the maximum number of nodes on one level. Every node enters and leaves the queue once, so the running time is $O(n)$.

The queue holds at most $O(w)$ nodes. Since $w \le n$, the required worst-case auxiliary-space bound is $O(n)$. Level sums may reach $10^{14}$, so fixed-width implementations must use 64-bit integers.

## Alternatives and edge cases

- **Depth-first accumulation:** A DFS can add each value into an array indexed by depth and then scan for the first minimum. It is also $O(n)$ time, but stores all level sums and recursive DFS may overflow the call stack on a $10^5$-node chain.
- **Repeated traversal by depth:** Computing level $1$, then restarting at the root for level $2$, and so on is correct, but takes $O(n^2)$ time on a skewed tree.
- **Two queues:** Keeping separate current- and next-level queues makes boundaries explicit, but the fixed queue-length loop provides the same invariant with one deque.
- Update only on a strictly smaller sum; using `<=` incorrectly returns the deepest tied level.
- The root is level $1$, not level $0$.
- Sparse nodes do not split a level: all nodes at the same distance from the root contribute to one sum.
- A one-node tree necessarily returns level $1$.
- Use wide integer arithmetic because one level may contain many values near $10^9$.

