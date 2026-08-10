## General

**Use the two-sweep property of trees**

The diameter is the longest simple path measured in edges. A standard tree property allows it to be found with two traversals:

1. Start from any node and find a farthest node \(a\).
2. Start from \(a\) and find the greatest distance to any node.

That second greatest distance is the diameter.

The exact source performs both traversals with recursive depth-first search.

**Build an undirected adjacency list**

For every edge `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Because the input is a tree, there are \(n-1\) edges and every node is reachable from node zero.

`defaultdict(list)` also handles the one-node tree: with no edges, asking for `g[0]` yields an empty neighbor list.

**What `dfs` records**

`dfs(i, fa, t)` visits node `i`, where:

- `fa` is the parent from which the traversal arrived;
- `t` is the number of edges from the traversal’s starting node to `i`.

For every neighbor other than the parent, recursion continues with distance `t + 1`. A separate visited set is unnecessary because an acyclic tree has no way to return to an earlier node except through the immediate parent.

After visiting descendants, the function compares `t` with global `ans`. If this distance is strictly larger, it updates `ans` and records `i` in global `a` as the farthest node seen.

Updating after child recursion rather than before does not affect the maximum; every node’s distance is eventually tested.

**First sweep**

`ans = a = 0` initializes the maximum distance and farthest node. `dfs(0, -1, 0)` explores the whole tree from node zero.

At completion, `a` is some node farthest from zero. When several nodes tie, strict `ans < t` keeps whichever one first established the maximum. Any farthest choice is sufficient.

**Why a farthest node is a diameter endpoint**

Let \(P\) be a longest path in the tree. From any starting node, consider unique paths to the endpoints of \(P\). Tree structure forces a farthest reachable branch to end at a peripheral leaf; one can show that at least one farthest node from an arbitrary start is an endpoint of some diameter.

Intuitively, if the first sweep stopped at an internal point while its path could continue farther away along a branch, that continuation would contradict maximal distance. In a tree, unique paths prevent shortcuts that complicate this property in general graphs.

**Second sweep**

The code calls `dfs(a, -1, 0)` from the discovered endpoint. The greatest distance from a diameter endpoint reaches the other endpoint, so it equals the diameter.

The source does not reset `ans` to zero before this sweep. That is still correct. The old value is the greatest distance from node zero. The tree diameter is at least that large, and the second traversal updates `ans` whenever it finds a larger distance. If the values happen to be equal, retaining the old value already equals the diameter.

The global `a` may be updated during the second traversal, but it is not used afterward.

**Following the second example**

From node zero, a farthest node is either 3 or 5. Suppose the first sweep records 3. Starting from 3, the unique path to 5 is `3-2-1-4-5`, containing four edges. No node is farther from 3, so the second sweep leaves `ans = 4`.

**Single-node tree**

With no edges, `dfs(0,-1,0)` sees no neighbors and does not update the strict comparison because `ans` is already zero. Both sweeps finish, and zero is returned, which is the correct diameter.


The DFS visits every node exactly once per sweep and supplies its exact distance from the sweep start because tree paths are unique. The first sweep chooses a farthest node \(a\), which is an endpoint of a diameter. The second sweep computes the maximum distance from \(a\), whose farthest endpoint completes a diameter. Therefore, the final maximum distance is the tree diameter.

## Complexity detail

Let \(n\) be the node count. Building the adjacency lists processes \(n-1\) edges. Each DFS visits all \(n\) nodes and examines both directions of every edge. Total time is \(O(n)\).

The adjacency list stores \(O(n)\) entries overall, and a chain-shaped tree produces recursion depth \(O(n)\). Auxiliary space is \(O(n)\).

With \(n\) up to 10,000, a standard Python recursion limit may be too low for a path-shaped tree unless the execution environment raises it. An iterative traversal avoids this portability risk.

## Alternatives and edge cases

- **Two breadth-first searches:** A queue computes the same farthest endpoints without recursion-limit risk and retains \(O(n)\) time and space.
- **One postorder DFS:** Track the two greatest child depths at every node and maximize their sum. It also runs in \(O(n)\) but has a different invariant.
- **Leaf peeling:** Remove leaves layer by layer to locate one or two centers, then derive diameter length. It is linear but more involved.
- **Single node:** No edge exists and the diameter is zero.
- **Chain tree:** The two ends are diameter endpoints; recursion reaches depth \(n\).
- **Star tree:** Any two leaves form a diameter of two edges.
- **Tied farthest nodes:** Choosing any one works for the second sweep.
- **Parent check versus visited set:** Parent-only avoidance is safe because the input is guaranteed acyclic.
- **Not resetting `ans`:** The old eccentricity cannot exceed the diameter, so retaining it does not corrupt the second maximum.
- **Recursion depth:** An explicit stack or BFS is safer at the maximum input size.
