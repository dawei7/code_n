## General

**Removing a node creates one component per neighbor direction**

For a node in the rooted tree, removing it separates:

- each child subtree into its own component;
- all nodes outside the removed node's subtree into one parent-side component, unless that size is zero.

The score is the product of the sizes of these nonempty components. A postorder traversal is ideal because child subtree sizes are exactly the values needed for the product.

**Build child adjacency from the parent array**

For every node `i` from one through `n-1`, the source appends `i` to `g[parents[i]]`. The resulting adjacency lists point only from parent to child.

Although `dfs` accepts a `fa` parameter and checks `j != fa`, a child-only list never contains the parent. That check is redundant for this exact graph representation but harmless.

**Compute subtree size and child-component factors**

At node `i`, `cnt=1` initially counts the node itself, and `score=1` is the multiplicative identity.

For every child `j`, recursive `dfs(j,i)` returns child-subtree size `t`. If node `i` is removed, those `t` nodes form one component, so the source multiplies `score *= t`.

It also adds `t` to `cnt`. After all children are processed, `cnt` is the complete subtree size rooted at `i`.

**Compute the parent-side component**

There are `n-cnt` nodes outside node `i`'s subtree. When `i` is removed, they remain connected through the original parent direction and form one component.

If `n-cnt` is positive, the source multiplies it into the score. If it is zero, `i` is the root and no outside component exists. Skipping the zero factor is essential because the definition multiplies only nonempty subtree sizes; multiplying by zero would destroy the root's score.

**Trace a leaf**

A leaf starts with `cnt=1` and has no child factors. Unless it is the root of a one-node tree, the outside component has size `n-1`.

Its score is therefore `n-1`, matching the fact that removing a leaf leaves the rest of the tree as one connected component.

**Trace an internal node**

If a node has child subtree sizes two and three in a ten-node tree, then `cnt=1+2+3=6`. Removing it creates components of sizes two, three, and four, where four is the outside part.

The source calculates score `2 * 3 * 4 = 24` and returns subtree size six to the parent.

**Update the global maximum and count**

`mx` stores the greatest score completed so far, and `ans` stores how many processed nodes have that score.

If `score > mx`, a new maximum has been found, so `mx` is replaced and `ans` resets to one. If `score == mx`, the node ties the maximum and `ans` increments. Smaller scores make no change.

These variables are declared `nonlocal` so every recursive frame updates the same aggregate state.

**Why postorder produces correct scores**

Assume every child call returns its exact subtree size. Child subtrees are disjoint, and together with the current node they form the current subtree, so summing their sizes plus one gives exact `cnt`.

Removing the current node disconnects each child subtree from every other child subtree. All remaining nodes not in the current subtree lie on the parent side and stay connected. These are exactly all nonempty components, so multiplying their sizes gives the exact score.

Leaves establish the induction base. Thus every call computes both the correct subtree size and score.

**Why the final count is correct**

The DFS reaches every node once. The maximum-tracking logic maintains the count of nodes equal to the greatest score among all nodes processed so far.

After the root call finishes, “processed so far” is the entire tree. `ans` is consequently the number of nodes having the global highest score.

**Binary-tree degree is not required by the arithmetic**

The description guarantees a binary tree, but the loop works for any number of children. It simply multiplies one component size per child. The complexity and proof remain the same for a general rooted tree.

## Complexity detail

Let $N$ be the number of nodes. Building child lists takes $O(N)$ time. DFS visits each node once and scans each parent-child edge once, so total time is $O(N)$.

The adjacency lists use $O(N)$ space. Subtree recursion can reach depth $O(N)$ for a skewed tree, and therefore uses $O(N)$ call-stack space in the abstract bound.

In standard Python, a depth near the allowed $10^5$ nodes exceeds the default recursion limit and can raise `RecursionError` unless the environment adjusts the limit or the traversal is rewritten iteratively. This is a practical risk in the exact source despite its correct asymptotic algorithm.

## Alternatives and edge cases

- **Iterative postorder:** Build a traversal order and process it backward, avoiding Python recursion-depth failure.
- **Recompute components per node:** Removing every node and traversing components would cost $O(N^2)$.
- **Root node:** Has no parent-side factor because `n-cnt=0`.
- **Leaf node:** Its only component has size `n-1`.
- **One child:** Score multiplies that child subtree and the optional outside component.
- **Two children:** Each child size is a separate factor.
- **Equal highest scores:** `ans` increments for every tie.
- **New larger score:** The previous tie count is discarded and reset to one.
- **Large products:** Python integers grow automatically and do not overflow fixed-width arithmetic.
- **Directed child lists:** The `fa` check is unnecessary but harmless.
- **Skewed tree:** Produces linear recursion depth and the exact-source runtime risk.
- **Input preservation:** `parents` is read to build a separate graph.
