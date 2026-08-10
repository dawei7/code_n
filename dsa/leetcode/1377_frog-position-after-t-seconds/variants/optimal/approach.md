## General

**Build the tree in both directions**

The edge list is undirected, so each pair `[u, v]` is inserted into both `g[u]` and `g[v]`. The frog begins at vertex one, and `vis[1] = True` records that the root has already been visited. When a vertex is processed, only neighbors whose visited flag is false are legal destinations; this enforces the rule that the frog never jumps back.

Because the graph is a tree, every non-root vertex reached by the search has exactly one already visited neighbor: its parent. All other adjacent vertices are unvisited children. This tree property is central to both the probability calculation and the compact child count.

**What one queue entry represents**

The queue begins with `(1, 1.0)`. A pair `(u, p)` at the current breadth-first layer means that after the number of seconds already processed, the frog is at vertex `u` with probability `p`.

Breadth-first layers correspond exactly to seconds because every jump consumes one second. The inner loop processes `len(q)` entries captured at the beginning of the layer. Children appended during that loop wait for the next outer iteration, so positions after different elapsed times never mix.

The variable `t` is used as remaining time rather than as a fixed input. At the initial root layer, all requested seconds remain. After processing one layer and generating the next-second positions, `t -= 1`. Therefore, when a queued vertex is inspected, the current `t` tells how many more jumps must occur before the requested observation time.

**Counting legal choices**

For the root, every neighbor is initially unvisited, so the legal choice count is `len(g[1])`. For any other reached vertex, exactly one neighbor is its visited parent, so the number of unvisited children is `len(g[u]) - 1`.

The code combines these cases as

`cnt = len(g[u]) - int(u != 1)`.

For the root, `u != 1` is false and contributes zero. For every non-root vertex it is true and contributes one. This shortcut depends on the input being a tree; in a general graph, there could be several previously visited neighbors.

When there are `cnt` legal children, the frog chooses each uniformly, so a state with probability `p` gives every child probability `p / cnt`. Since a tree has a unique path from vertex one to any vertex, a child is discovered from exactly one parent and its probability does not need to be added to another route.

**Why the target check includes both time and leaf status**

Reaching `target` at an intermediate second does not always mean the frog will still be there after all $t$ seconds. If unvisited children exist and time remains, the rules force it to jump away on the next second. It can never return because visited vertices are forbidden.

The exact return condition is

`p if cnt * t == 0 else 0`.

The product is zero precisely when `cnt == 0` or `t == 0`:

- If `t == 0`, the observation time is now, so probability `p` is the answer even if the frog could jump later.
- If `cnt == 0`, the target has no unvisited child. The frog stays there forever, so `p` remains valid for any remaining time.
- If both values are positive, the frog must leave before the requested time, so the answer is zero.

Returning immediately is safe because the tree supplies only one route to the target. No different queue entry can later contribute additional probability to the same vertex.

**Why leaves do not cause division by zero**

If a non-target vertex has `cnt == 0`, all its neighbors are already visited and the child loop enqueues nothing. Although the expression `p / cnt` appears inside that loop, it is never evaluated because no unvisited `v` exists. If the leaf is the target, the earlier target condition returns `p`.

**Why the algorithm is correct**

Initially the queue correctly describes the frog at vertex one with probability one. Assume a layer correctly contains the probability of every possible current position. For each non-target state with legal children, uniform division assigns exactly its probability mass across all allowed next positions. A leaf retains its mass at that vertex; it need not be re-enqueued because the method only needs a queried target and handles target persistence when encountered. Thus each generated layer correctly represents the next second.

When the target is encountered, the remaining-time test distinguishes exactly whether its current probability stays there until the observation time. If the traversal reaches the requested layer without the target, or exhausts all moving states, the target probability is zero. Hence the returned value is correct.

## Complexity detail

Let $n$ be the number of vertices. Building the undirected adjacency list uses $2(n-1)$ entries. Each vertex is marked visited at most once, enqueued at most once, and has its adjacency list scanned once. Total time is $O(n)$.

The graph, visited array, and queue each use $O(n)$ space in the worst case, matching the manifest. Probability arithmetic and the remaining-time counter use constant additional state.

## Alternatives and edge cases

- **Recursive DFS with depth:** Multiply probabilities down the unique root-to-target path and accept only when depth equals $t$ or the target is a leaf. It is also $O(n)$ but recursion depth may be a concern.
- **Path-first calculation:** Find the unique path to the target, multiply reciprocal child counts, then check the arrival-time and leaf condition. This can be concise but needs a separate path search.
- **General probability simulation:** Carry probability for every vertex at every second. It handles arbitrary graphs but wastes work and storage for a tree with no revisits.
- **Target is the root:** If the root has children and time remains, the frog must leave and the answer is zero. If the one-node tree has no child, it stays with probability one.
- **Target reached before time expires:** Its probability survives only if it has no unvisited child.
- **Target reached exactly at time `t`:** The remaining counter is zero, so the method returns its current probability regardless of children.
- **Target deeper than `t`:** Its BFS layer is never processed at remaining time zero, so the result is zero.
- **Leaf that is not the target:** Its probability stops moving, but it cannot later become the target; omitting it from future layers is safe for this single-target query.
- **Uniform branching:** Dividing by `cnt` is correct because all unvisited adjacent choices are equally likely.
- **Unique path:** Probabilities never need merging because a tree has only one root-to-vertex path.
- **Visited timing:** Marking a child when enqueued prevents its parent edge from being used on the next layer.
- **Final extra expansion:** When `t == 0` and the current vertex is not the target, the code may enqueue one unused next layer before decrementing to $-1$; this does not change the result or asymptotic bound.
- **Required imports:** `defaultdict` and `deque` must be available from `collections`.
