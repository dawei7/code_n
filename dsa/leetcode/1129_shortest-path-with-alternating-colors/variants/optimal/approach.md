## General
**Make the last color part of the state.** Reaching the same node after red and after blue edges creates different futures: the first state may take only blue next, while the second may take only red. Build separate red and blue adjacency lists and run breadth-first search over states `(node, last_color)`.

**Allow either first color.** Put both `(0, red)` and `(0, blue)` into the queue at distance zero. These are conceptual starting states, not actual incoming edges. Expanding `(node, last_color)` follows only adjacency edges of the opposite color and produces states carrying that new color.

**Visit each color state once.** Breadth-first search processes states in nondecreasing path length. Therefore, the first time `(neighbor, next_color)` is reached, its distance is the shortest alternating distance for that exact state; later visits cannot improve it. The answer for a node is the smaller distance among its two color states, or `-1` if neither was reached. This state graph represents every alternating path and only alternating paths, so its BFS distances are exactly the required values.

## Complexity detail
There are $2n$ color states. Each state is enqueued at most once, and each red or blue adjacency list is scanned only from the compatible state, so traversal takes $O(n + r + b)$ time. The adjacency lists, two-state distance table, and queue use $O(n + r + b)$ space.

## Alternatives and edge cases
- **Repeated relaxation:** Bellman-Ford-style updates on the two-color state graph are correct, but scanning all edges for up to $2n$ rounds costs $O(n(r+b))$ time.
- **Visited nodes without color:** Marking only a node as visited can discard a later arrival with the opposite last color even though it enables a necessary continuation.
- **Self-edge:** It may change the last color while remaining at the same node, but only an unvisited color state needs to be enqueued.
- **Parallel edges:** Duplicate same-color edges do not change distances; the visited-state check prevents repeated work.
- **No outgoing path from zero:** The result is `0` for node `0` and `-1` for every other node.
