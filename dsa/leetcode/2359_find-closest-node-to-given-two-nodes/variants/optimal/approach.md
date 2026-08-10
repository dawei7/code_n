## General

**Turn the optimization into distance data**

For a candidate node `i`, the score is

$$
\max(d_1(i),d_2(i)),
$$

where $d_1(i)$ is the shortest directed distance from `node1` and $d_2(i)$ is the shortest directed distance from `node2`. A node is eligible only if both distances are finite. Once both complete distance arrays are known, the remaining work is a simple scan: compute every node's score and keep the smallest one.

The graph has an unusually strong restriction: every node has at most one outgoing edge. Starting from a node, there is never a choice of which edge to follow. The reachable portion is a single directed path that may end at `-1` or eventually enter a cycle. This makes traversal simpler than in a general graph, although the exact solution still uses ordinary breadth-first search machinery.

**Building the adjacency representation**

The input `edges` stores one possible destination for each source index. The solution converts it to `g`, a `defaultdict(list)`. For every pair `(i, j)` produced by `enumerate(edges)`, it appends `j` to `g[i]` only when `j != -1`. Thus, each adjacency list has either zero or one neighbor.

This conversion is not strictly necessary—one could follow `edges[i]` directly—but it makes the traversal look like standard graph BFS. It also ensures that a node with no outgoing edge has an empty neighbor list when `g[i]` is accessed.

**Computing distances from one start**

The nested function `f(i)` creates a distance array filled with `inf`. Infinity is a sentinel meaning “not reached from this start.” It then assigns distance zero to the starting node and pushes that node into a deque.

While the queue is nonempty, it removes a node from the left and inspects its adjacency list. For a neighbor `j`, it assigns

```python
dist[j] = dist[i] + 1
```

and enqueues `j` only if `dist[j] == inf`. The test serves as the visited check. Once a node has a finite distance, it cannot enter the queue again.

This visited condition is vital when the reachable path enters a cycle. Without it, traversal would follow the cycle forever. With it, the edge back to an already reached node is ignored and the queue eventually empties.

Because every edge has unit length, discovering a node from a node at distance $d$ assigns distance $d+1$. Breadth-first search processes discoveries in non-decreasing distance order, so the first assigned distance is shortest. In this special outdegree-at-most-one graph, there is only one directed route that can be followed from the start before a repetition, making that conclusion even more direct.

The solution calls `f(node1)` to obtain `d1` and `f(node2)` to obtain `d2`. These traversals are independent; a node can be reachable from one start but not the other.

**Selecting the best common reachable node**

The scan initializes `ans = -1` and `d = inf`. It visits node indices in ascending order through:

```python
for i, (a, b) in enumerate(zip(d1, d2)):
```

Here, `a` and `b` are the two distances for node `i`. The score `t = max(a, b)` measures how far the farther of the two starts must travel. Minimizing this maximum balances the two reachability requirements exactly as the problem requests.

The answer changes only when `t < d`, using a strict inequality. Ascending scanning plus strict replacement implements the tie rule. The first node achieving a particular minimum score is the smallest index with that score; a later equal score does not replace it.

If a node is unreachable from either start, at least one distance is `inf`, so its maximum is `inf`. Since the best score starts at `inf` and the update requires strict improvement, such a node is never selected. If no node is reachable from both starts, every score is infinite, `ans` remains `-1`, and the required failure result is returned.

**A small trace**

For `edges = [2, 2, 3, -1]`, the first traversal from node `0` gives finite distances to `0, 2, 3`: respectively `0, 1, 2`. The second traversal from node `1` gives `0` at node `1`, `1` at node `2`, and `2` at node `3`. Nodes `0` and `1` are not mutually reachable, so each has an infinite score. Node `2` has score `max(1, 1) = 1`, while node `3` has score `max(2, 2) = 2`. The scan chooses node `2`.

If `node1 == node2`, that start has distance zero in both arrays. Its score is zero, the smallest possible value, so it must be returned. The general algorithm handles this without a special case.

**Why the complete method is correct**

Each call to `f` marks exactly the nodes reachable by repeatedly following outgoing edges from its start. For every marked node, the assigned number is the length of that path and hence its shortest directed distance. All other nodes retain `inf`.

Therefore, a finite `max(d1[i], d2[i])` exists exactly for common reachable nodes, and its value is exactly the objective associated with node `i`. The final loop examines every node. It records a node precisely when its score improves on every earlier score. After the scan, `d` is the global minimum finite score if one exists, and `ans` is its smallest-index achiever because equal scores never replace it. If no finite score exists, the unchanged `-1` is correct.

## Complexity detail

Let $n$ be the number of nodes. Constructing `g` inspects all $n$ entries of `edges` and stores at most one directed edge per node, so it takes $O(n)$ time and $O(n)$ space.

Each BFS reaches a node at most once and inspects at most one outgoing edge for every reached node. A traversal is therefore $O(n)$ in the worst case. Running it twice remains $O(n)$, and the final zipped scan is another $O(n)$. Total time is $O(n)$.

The two distance arrays use $O(n)$ space. The adjacency mapping also uses $O(n)$ space. Although a deque is used, the outdegree restriction means following a single start cannot generate multiple simultaneous branches, so its queue normally holds at most one pending node. All auxiliary storage together is nevertheless $O(n)$ because of the graph and distance arrays.

## Alternatives and edge cases

- **Follow `edges` directly:** Since every node has at most one outgoing edge, a simple while-loop can record distances without building adjacency lists or using a deque. It preserves $O(n)$ time and can reduce constants.
- **Recursive depth-first search:** DFS also follows the unique path correctly, but a path of length $n$ can exceed Python's recursion limit. The iterative traversal avoids that risk.
- **Search from both starts simultaneously:** A combined traversal is possible, but separate distance arrays keep reachability and objective calculation clearer and make tie handling straightforward.
- **Cycle reachable from a start:** The finite-distance test prevents revisiting a node, so traversal stops after visiting each cycle node once.
- **A path ending at `-1`:** No adjacency entry is appended for that edge, so the sink has no neighbor and the queue becomes empty normally.
- **Reachable from only one start:** One distance stays `inf`, making the maximum infinite and preventing selection.
- **No common reachable node:** No strict improvement over the initial infinite best score occurs, so the method returns `-1`.
- **Equal objective scores:** Nodes are scanned in increasing index order, and the strict `<` update retains the smallest index.
- **Identical start nodes:** The shared start has score zero and is immediately the unique best possible answer.
- **Merging paths:** Two different starting paths may enter the same node and then share all later nodes. The distance arrays preserve their possibly different arrival lengths, allowing the final maximum to choose the best meeting point.
