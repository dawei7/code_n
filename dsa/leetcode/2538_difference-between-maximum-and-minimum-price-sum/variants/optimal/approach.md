## General

**Reduce the chosen-root cost to a path with one endpoint excluded**

All prices are positive. For a chosen root `r`, the minimum path sum among paths starting at `r` is the path containing only `r`, with sum `price[r]`.

The maximum path sum starts at `r` and ends at some node `u`. The cost is

$$
\operatorname{pathSum}(r,u)-\texttt{price}[r].
$$

Thus the global answer is the maximum price sum of any tree path when the price of one endpoint, the chosen root, is excluded.

The DP tracks whether the far endpoint price of a downward path is included or excluded.

**Define the two returned states**

For node `i` with parent `fa`, `dfs(i,fa)` returns `(a,b)`:

- `a` is the maximum sum of a downward path starting at `i` with its terminal endpoint's price included;
- `b` is the maximum sum of a downward path starting at `i` with its terminal endpoint's price excluded.

For the zero-edge path from `i` to itself:

- including the endpoint gives `price[i]`, so `a` starts there;
- excluding that same endpoint gives zero, so `b` starts at zero.

These base choices also allow a complete candidate path to use `i` itself as either endpoint.

**Extend a state through one child**

Suppose child `j` returns `(c,d)`.

A downward path from `i` through `j` that includes its far endpoint has sum

`price[i]+c`.

One that excludes its far endpoint has sum

`price[i]+d`.

The updates

`a=max(a,price[i]+c)`

and

`b=max(b,price[i]+d)`

retain the best downward paths among all processed children.

**Combine two branches through `i`**

Before incorporating child `j` into the running states, `a` and `b` describe either the trivial endpoint at `i` or a path through an earlier child.

A complete path passing through `i` can combine:

- prior branch with endpoint included, `a`, and new child branch with endpoint excluded, `d`;
- prior branch with endpoint excluded, `b`, and new child branch with endpoint included, `c`.

The candidates are `a+d` and `b+c`.

Exactly one of the two outer endpoints is excluded, matching the root-cost reduction. Node `i` is counted once: it belongs to the running branch state but not to child-return states `c` or `d`, which begin at child `j`.

**Why update answer before extending states**

If `a` were updated with child `c` first, combining it with `d` from the same child could incorrectly use one child subtree on both sides of a supposed path.

The source first evaluates cross-branch candidates using only previously processed branches, then merges the child into `a` and `b`. This enforces that the two halves of a path are disjoint except at `i`.

**Why all paths are considered**

Every simple tree path has a unique highest meeting node relative to the arbitrary DFS root zero. Its endpoints lie in two different child directions of that node, or one endpoint is the node itself.

When the second relevant branch is processed, the first is represented by running `a` or `b` and the second by child `c` or `d`. The appropriate included/excluded combination reaches `ans`.

Conversely, every combined candidate joins two valid downward paths through one node and forms a real simple path with exactly one endpoint price excluded.

Therefore, the maximum candidate equals the best cost over every possible chosen root.

**Trace the meaning of a simple chain**

On a three-node chain with prices 1, 1, 1, the full path sum is three. Excluding one endpoint gives two. The DP builds an included state down one side and an excluded state down the other, producing answer two, matching the sample.

**Graph construction and parent guard**

The adjacency list stores both directions of every undirected edge. Parameter `fa` prevents DFS from returning immediately to its parent. Because the input is a tree, that single guard is enough to visit each node once.

**Actual recursion versus manifest wording**

The manifest describes iterative postorder DP, but the protected source calls recursive `dfs`. On a path-shaped tree with $10^5$ nodes, Python's default recursion depth may be exceeded. The DP logic is linear and correct, but an iterative implementation would be safer at the maximum constraint.

## Complexity detail

Building adjacency takes $O(n)$ time and space for `n-1` edges. DFS visits each node once and examines each undirected edge twice, so time is $O(n)$.

The adjacency list uses $O(n)$ space. Recursive call depth can be $O(n)$, so total auxiliary space is $O(n)$.

The answer may sum up to $n$ prices and requires 64-bit arithmetic in fixed-width languages.

## Alternatives and edge cases

- **Iterative postorder:** Store parent and traversal order explicitly to avoid recursion-depth failure; this matches the manifest summary.
- **One node:** Only the zero-edge path exists, so maximum cost is zero.
- **Leaf state:** Included value is its price and excluded value is zero.
- **Positive prices:** They make the root-only path the minimum path sum.
- **Two child branches:** Combine before updating to avoid reusing the same child.
- **One endpoint at current node:** Initial `a` and `b` represent those cases.
- **Arbitrary DFS root:** It only organizes computation; all possible problem roots are still represented as excluded endpoints.
- **Parent guard:** It is sufficient because the graph is a tree.
- **Large sum:** Use a wide integer type.
- **Manifest mismatch:** The exact source is recursive, not iterative.
