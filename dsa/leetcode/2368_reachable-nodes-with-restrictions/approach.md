## General

**Restricted nodes behave like removed vertices**

The input graph is a tree: it is connected, has $n-1$ undirected edges, and contains no cycles. To reach a node from `0`, there is exactly one simple path. A node is allowed precisely when that unique path contains no restricted vertex.

This means we can conceptually remove every restricted node and its incident edges. The answer is then the size of the connected component containing node `0`. The exact solution computes that component with recursive depth-first search.

**Build both directions of every edge**

Each pair `[a, b]` describes an undirected edge. The adjacency mapping `g` must therefore receive both:

```python
g[a].append(b)
g[b].append(a)
```

If only one direction were stored, reachability would incorrectly depend on the arbitrary order of endpoints in the input. A `defaultdict(list)` supplies an empty neighbor list for a node without an existing dictionary entry.

Across the whole tree, the adjacency lists contain $2(n-1)$ entries because every edge is represented from both endpoints.

**Use one set for restrictions and visitation**

The solution initializes:

```python
vis = set(restricted)
```

Normally, a visited set starts empty. Preloading restricted nodes is a useful unification: the DFS condition already refuses to enter anything in `vis`, so treating restricted nodes as “already visited” blocks them without a separate restriction test.

Node `0` is guaranteed not to be restricted, so calling `dfs(0)` is always valid. When DFS actually enters an allowed node `i`, it immediately adds `i` to `vis`. This prevents the search from walking straight back to its parent through the reverse adjacency entry.

Although the source graph is a tree and contains no cycles, undirected representation makes every edge look like a two-step cycle `parent -> child -> parent` to a traversal. The visited check is therefore still essential.

**Count the reachable component recursively**

The helper returns the number of reachable nodes in the region explored from `i`:

```python
return 1 + sum(j not in vis and dfs(j) for j in g[i])
```

The leading `1` counts node `i` itself. For each neighbor `j`, the generator evaluates `j not in vis and dfs(j)`:

- If `j` is already visited or restricted, the left side is false. Python short-circuits the `and`, does not call `dfs(j)`, and contributes Boolean `False`, numerically zero, to `sum`.
- If `j` is unvisited and allowed, the left side is true, DFS explores that neighbor, and the expression evaluates to the integer count returned by the recursive call.

Adding those child counts to one gives the total number reached through `i`. The use of Boolean false as zero is compact Python behavior; logically, it means blocked neighbors contribute no nodes.

**Trace a restriction that cuts off a subtree**

In the first example, node `5` is restricted. Node `6` itself is not restricted, but the unique path from `0` to `6` is `0 -> 5 -> 6`. When DFS examines neighbor `5` from `0`, `5 in vis` is already true. The recursive call is skipped, so neither `5` nor anything beyond it is counted.

Node `4` is blocked in the same way. The traversal can still enter `1` and then its allowed neighbors `2` and `3`. The recursive totals combine to count exactly `0, 1, 2, 3`.

This illustrates why it is not enough merely to subtract the number of restricted nodes from $n$. An unrestricted node may become unreachable because a restricted ancestor separates it from the root.

**Why the recursive count is correct**

When `dfs(i)` begins, `i` is reachable by an allowed path: the initial node is allowed, and recursive calls occur only across an edge to an unvisited, non-restricted neighbor. The helper counts `i` once.

For each neighbor, there are two cases. A restricted neighbor cannot belong to any permitted path and correctly contributes zero. A previously visited neighbor has already been counted; in a tree, this is normally the parent, so skipping it prevents duplication. Every other neighbor begins a disjoint child-side component whose nodes are reachable through `i`, and recursion counts that component.

Removing an edge from a tree separates its sides, so different unvisited neighbor subtrees cannot overlap. Summing their counts neither misses nor double-counts any reachable node. By induction from leaf calls upward, `dfs(i)` returns exactly the number of allowed nodes reachable through its subtree. Applied to `0`, it returns the requested component size.

The word “maximum” in the question does not require selecting among paths. All nodes in the allowed component can be reached through separate walks from `0`; the task asks for how many are reachable, not for one route visiting them without repetition.

## Complexity detail

Let $n$ be the number of nodes. Building adjacency lists reads $n-1$ edges and stores two entries for each, taking $O(n)$ time and space. Constructing the restricted/visited set takes $O(r)$ for $r$ restricted nodes.

DFS enters each reachable allowed node once. Across those calls, it scans each incident adjacency entry at most once from that node. Since the tree has $O(n)$ total adjacency entries, traversal time is $O(n)$ in the worst case. Set membership and insertion are expected $O(1)$.

Adjacency storage, `vis`, and the recursive call stack can each grow to $O(n)$. Peak auxiliary space is $O(n)$. A path-shaped tree can create recursion depth $O(n)$, which is a practical Python concern even though the asymptotic analysis is valid.

## Alternatives and edge cases

- **Iterative DFS:** Use a list as an explicit stack. It has the same $O(n)$ bounds and avoids Python recursion-depth failures on a chain of up to $10^5$ nodes.
- **Breadth-first search:** A deque can explore the same allowed component and count popped nodes. Layer order is unnecessary, but BFS is equally correct.
- **Disjoint set union:** Union edges whose endpoints are both unrestricted, then return the size of node `0`'s component. This works but is more machinery than one traversal.
- **Restricted direct neighbor of `0`:** It is preloaded in `vis` and blocks its entire side of the tree.
- **Unrestricted descendant behind a restriction:** It remains uncounted because its unique root path crosses the blocked node.
- **All non-root nodes restricted:** DFS counts only node `0` and returns one.
- **No danger that root is blocked:** The contract explicitly excludes `0` from `restricted`.
- **Undirected parent edge:** Marking a node before exploring neighbors prevents immediate recursion back to its parent.
- **Long chain:** Correctness is unchanged, but recursive depth may exceed Python's default limit; iterative traversal is the robust alternative.
