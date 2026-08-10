## General

**The current node alone is not enough state**

The path may revisit nodes and edges. Reaching node 3 after visiting only `{0,3}` is different from reaching node 3 after visiting `{0,1,2,3}`, because the remaining work differs.

A search state must therefore contain:

- the current node `i`;
- the set of nodes visited so far.

The solution encodes the visited set as a bitmask `st`. Bit `v` is one exactly when node `v` has appeared in the path.

**Bitmask operations**

The mask containing only start node `i` is `1 << i`.

When moving to neighbor `j`, the updated mask is:

`nst = st | (1 << j)`.

Bitwise OR sets `j`'s bit while preserving every previously set bit. Revisiting an already visited node leaves the mask unchanged, which is allowed.

The all-visited mask has its lowest `n` bits set:

`(1 << n) - 1`.

For example, when `n=4`, `1 << 4` is binary `10000` and subtracting one gives `1111`.

**Start from every node simultaneously**

The path may begin anywhere. Instead of running a separate BFS from every possible start, the solution initializes the same queue with all `n` singleton states:

`(i, 1 << i)` for every `i`.

All have distance zero. This multi-source BFS explores paths from every allowed starting point together. The first complete state found is therefore optimal across all starts.

The same states are inserted into `vis` immediately, preventing duplicate initial work.

**Why ordinary breadth-first search applies**

Every graph edge traversal adds exactly one to path length. State transitions are therefore unweighted.

BFS processes all states at distance `ans` before states at distance `ans+1`. The outer infinite loop represents levels, and:

`for _ in range(len(q))`

captures the number of states currently in one level before new states are appended.

After the complete level is processed, `ans` increases by one.

**The visited set uses both state components**

`vis` stores pairs `(node, mask)`, not just nodes.

Marking only a node visited would be wrong: returning to the same node with a larger set of visited vertices can be essential. Conversely, processing the exact same node and mask again cannot help, because BFS reached it at the shortest possible distance and its future options depend only on that pair.

Thus, `(j,nst)` is enqueued only on its first discovery.

**Stop at the first complete mask**

When a dequeued state has all bits set, its path has visited every graph node. BFS level order proves its distance `ans` is the smallest distance of any complete state from any allowed start, so the function returns immediately.

The graph is connected, so some complete walk always exists. The `while 1` loop will reach a return.

**Trace the star example**

For a star centered at 0 with leaves 1, 2, and 3, a shortest walk can start at leaf 1:

`1 -> 0 -> 2 -> 0 -> 3`.

The corresponding masks grow:

- start at 1: only bit 1;
- reach 0: bits 1 and 0;
- reach 2: bits 0, 1, and 2;
- revisit 0: same three bits but a different current node;
- reach 3: all four bits.

The final distance is four. Reusing node 0 and an edge is naturally represented because masks preserve visits without forbidding movement.

**Why the search is complete and optimal**

Every legal walk corresponds to a sequence of state transitions: current node follows a graph edge, and the destination bit is added. Multi-source initialization represents every possible first node.

Therefore, BFS can generate the state of every possible walk. It discards only repeated identical states reached no sooner than before; such repeats have the same future and cannot yield a shorter solution.

The first all-visited state is at the smallest transition count by BFS ordering, which is exactly the shortest path length requested.

## Complexity detail

There are `n` choices for current node and `2^n` possible visited masks, giving at most `n2^n` states. The queue and visited set therefore use `O(n2^n)` space.

Each state scans the adjacency list of its current node. Across all masks, total transition work is `O(E2^n)`, where `E` is the number of undirected edges. Since `E = O(n^2)` in the worst case, this is within the manifest bound:

$$
O(n^2 2^n).
$$

The small constraint `n <= 12` is what makes the exponential mask dimension practical.

## Alternatives and edge cases

- **BFS separately from every start:** It repeats much search work. Multi-source BFS finds the best start in one state graph traversal.

- **DFS with subset DP:** Memoize a recurrence over node and visited mask. It can solve the same state graph but shortest unweighted distance is especially natural with BFS.

- **Mark only nodes visited:** Incorrect, because the same current node with different masks represents different remaining tasks.

- **Forbid revisiting nodes:** Incorrect; trees and other graphs may require passing through a node again to reach all branches.

- **Single-node graph:** Its initial singleton mask already equals the full mask, so the answer is zero.

- **Complete graph:** A path visiting a new node on every step has length `n-1`.

- **Tree with branches:** Revisiting connector nodes is permitted and often necessary.

- **Duplicate state from different walks:** Only the first, shortest arrival is processed.

- **Any start allowed:** Every node appears as a distance-zero source.

- **Connected guarantee:** The infinite loop cannot exhaust without finding a complete mask under valid input.

- **No graph mutation:** Adjacency lists are only iterated.
