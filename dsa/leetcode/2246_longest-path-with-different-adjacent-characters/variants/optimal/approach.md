## General

**Root the path reasoning at a possible center**

Any simple path in a tree has a highest node relative to root zero. From that center, the path can extend into at most two child subtrees: one arm enters one child, and the other arm enters another child. A path cannot use three child branches because that would branch rather than remain a single path.

For each node, it is therefore enough to know the two longest downward chains that can connect through it while respecting different adjacent characters.

The exact implementation maintains those two values implicitly: `mx` stores the longest compatible child chain seen so far, and each new compatible chain `x` is combined with `mx` before `mx` is updated.

**Build directed child lists from `parent`**

For every node `i` from one onward, `parent[i]` is its unique parent. The code appends `i` to `g[parent[i]]`. This orients the rooted tree downward and lets DFS visit each node exactly once without needing a visited set.

The root has no parent and is not inserted as a child through `parent[0] = -1`.

**Meaning of the recursive return value**

`dfs(i)` returns the maximum number of edges in a valid downward chain that starts at node `i`. A leaf returns zero because a one-node chain contains zero edges.

For child `j`, the code first computes

`x = dfs(j) + 1`.

`dfs(j)` counts edges below `j`, and adding one includes edge `i-j`. This chain can connect to `i` only if `s[i] != s[j]`. If the characters match, the edge violates the rule and `x` is ignored for node `i`.

The recursive call still happens before that check because valid paths entirely inside `j`'s subtree must update the global answer even when they cannot extend through `i`.

**Combine two best compatible arms**

`mx` begins at zero. For each compatible child chain `x`, the code evaluates

`ans = max(ans, mx + x)`.

Before updating `mx`, it represents the longest compatible chain from previously processed children. Therefore, `mx + x` is a path that descends through one old child, passes through node `i`, and descends through current child `j`.

If no previous arm exists, `mx = 0` and the expression considers the one-arm path from `i` into `j`. This ensures purely downward paths are also recorded.

Then `mx = max(mx, x)` keeps the longest single arm for later children and for return to the parent. Processing all children this way is equivalent to retaining the largest and second-largest compatible chains, but needs only one local maximum.

**Why only one arm can be returned**

A parent connecting through node `i` can use only one downward continuation from `i`. Returning two arms would create a fork when the parent edge is added.

Thus, `dfs(i)` returns `mx`, the best single downward edge count. The two-arm combination is used only to update the global path answer centered at `i`.

**The global answer counts edges**

`ans` begins at zero, which represents a path containing one node and zero edges. Every update adds two downward edge counts through a center, so `ans` always stores a path length in edges.

The problem asks for number of nodes. A simple path with `e` edges contains `e + 1` nodes, so the method returns `ans + 1`.

This also handles `n = 1`: DFS returns zero, no update occurs, and the result is one.

**Why every recorded path is valid**

Each returned child chain is valid by recursion. It is accepted at node `i` only when the connecting edge has different endpoint characters. Two combined arms lie in different child subtrees, which are disjoint in a tree, and meet only at `i`. The resulting sequence is simple and every adjacent character differs.

**Why the longest path is found**

Take any optimal valid path and choose its highest node `i`. Its portions below `i` lie in at most two child subtrees. DFS computes chains at least as long as those portions, and their first edges are compatible because the path is valid.

When the latter of those two child chains is processed, `mx` is at least the other one's length, so `mx + x` reaches at least the optimal edge count. Since updates only describe valid paths, `ans` cannot exceed the true optimum. Equality follows.

**Recursion depth**

The recursive structure mirrors tree height. A chain-shaped tree can produce `O(n)` call depth. The exact solution relies on the execution environment's recursion capacity; an iterative bottom-up version can avoid that implementation concern without changing the recurrence.

## Complexity detail

Building child lists takes `O(n)` time and space. DFS visits every node once and processes every parent-child edge once, so traversal time is `O(n)`.

The adjacency structure stores `n - 1` child references. The recursion stack can reach `O(n)` depth, giving total auxiliary space `O(n)`.

Character comparisons and maximum updates are constant-time per edge.

## Alternatives and edge cases

- **Bottom-up leaf queue:** Process children before parents using child counts, maintaining two best chains per node. It achieves the same `O(n)` bounds without recursion.
- **Treat the tree as an arbitrary graph DFS:** A visited set works but is unnecessary because the parent array already gives a rooted acyclic direction.
- **Return two arms to the parent:** This would create a branching structure rather than a valid path; only one chain may extend upward.
- **Ignore matching-edge subtrees entirely:** Even when a child cannot connect to its parent, valid paths inside that child's subtree must still be explored.
- **Single node:** The answer is one.
- **All characters equal:** No edge is compatible, so the longest valid path contains one node.
- **Long compatible chain:** Each DFS return grows by one edge and the global result becomes the full node count.
- **Two strong child branches:** They combine through their parent if both first characters differ from the parent's.
- **Only one compatible child:** `mx + x` with initial zero records the one-arm path.
- **Tied chain lengths:** Either can be retained as `mx`; combining with another tie yields the same score.
- **Root-centered optimum:** It is evaluated during `dfs(0)` even though the root has no parent.
- **Deep tree:** Recursive depth may require an iterative implementation or environment stack adjustment in some Python runtimes.
