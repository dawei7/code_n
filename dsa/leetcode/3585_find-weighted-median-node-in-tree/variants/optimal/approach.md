## General

For query `(u,v)`, the answer is the first node encountered from `u` whose accumulated path weight is at least half the total. The source preprocesses:

- depth and root-distance;
- binary ancestors;
- lowest common ancestor queries.

It then locates the threshold node with weighted binary lifting.

**Rooted preprocessing**

An iterative stack roots the weighted tree at zero. For every node it records immediate parent, edge depth, and `distance[node]`, the weighted distance from root zero.

Skipping the passed parent is sufficient because the input is a tree. Iteration avoids recursion failure on a length-`10^5` chain.

`up[b][x]` is the ancestor `2^b` edges above `x`. Higher levels are built by composing two half-length jumps. Root ancestors remain root.

**Lowest common ancestor**

The LCA helper first lifts the deeper node until depths match. If nodes differ, it lifts both from largest power downward whenever proposed ancestors differ. Their common parent afterward is the LCA.

For query endpoints `first` and `second` with LCA `common`:

`first_weight = distance[first]-distance[common]`

is the upward path weight from first to LCA, while `second_weight` is the downward branch weight from LCA to second. Total path weight is their sum.

All comparisons double weights instead of dividing by two. Condition accumulated weight at least half becomes:

$$
2\cdot accumulated \ge total.
$$

This handles odd total weights exactly without floating point.

**Case 1: threshold occurs by the LCA**

If `2*first_weight >= total`, half is reached somewhere on the upward segment from first toward common.

The source starts `node=first` and searches for the farthest ancestor still strictly before the threshold. For a candidate ancestor, accumulated weight from the query start is:

`distance[first]-distance[candidate]`.

If twice this value is still less than total, candidate has not reached half and is safe to adopt. Trying jumps from largest to smallest moves `node` as far upward as possible while retaining strict inequality.

Afterward, `node` is the last path node before the threshold. Its parent `up[0][node]` is the first node whose accumulated weight is at least half, so that parent is returned.

Strict `<` is essential. If a node lands exactly at half, it is already the median and must not be skipped.

**Case 2: threshold lies after the LCA**

If `2*first_weight < total`, traversal reaches common without reaching half. The additional doubled distance needed down the second branch is:

`required = total - 2*first_weight`.

A node `x` on common-to-second reaches the threshold when:

`2*(distance[x]-distance[common]) >= required`.

The search starts at `second`, which certainly satisfies the condition, and lifts upward. It accepts a candidate only if:

- it does not climb above common, checked by depth;
- it still satisfies the threshold.

Largest-first jumps find the highest node on the downward branch that still reaches half. “Highest” here means closest to common and therefore first encountered while walking from first to second. That node is appended directly.

**Direction matters**

Weighted median is defined from `u` toward `v`. Reversing query endpoints can change the answer, especially when one heavy edge crosses half. The two-case search preserves the supplied `first` as traversal origin.

**Equal endpoints**

If both endpoints are the same node, path weight is zero and the first node already satisfies at least half of zero. The source returns it before LCA threshold logic.

## Complexity detail

Adjacency and iterative traversal take `O(n)` time. Building `O(\log n)` ancestor levels for all nodes takes `O(n\log n)`.

Each query performs one LCA and one weighted lifting search, both `O(\log n)`. Total time is `O((n+q)\log n)`.

The ancestor table uses `O(n\log n)` space; graph and other arrays use `O(n)`, and output uses `O(q)`. Auxiliary preprocessing space matches the manifest’s `O(n\log n)`.

## Alternatives and edge cases

- **Walk the path per query:** Parent-by-parent traversal can take `O(n)` per query and is too slow.
- **Heavy-light decomposition:** It can locate weighted prefix thresholds with segment structures and supports updates, but weights are static and binary lifting is simpler.
- **Floating half:** Comparing doubled integers avoids precision errors for large odd totals.
- **Exact half at a node:** Strict-before search returns that node as the first satisfying position.
- **Half inside an edge:** Nodes are the only candidates, so the endpoint reached after crossing that edge is returned.
- **Median at the LCA:** The upward case returns common when first-to-common is the first threshold-reaching distance.
- **Median on second branch:** The required-distance search chooses the closest qualifying descendant of common.
- **One-edge path:** The destination is returned in the query’s traversal direction.
- **Reversed query:** It is intentionally solved separately and may return the opposite endpoint.
- **Same node:** Returns itself with zero path weight.
- **Large edge weights:** Python integers and doubled comparisons avoid overflow.
- **Root LCA:** Depth guards and root self-ancestors keep jumps valid.
- **Tree guarantee:** Unique paths and parent-only traversal rely on acyclicity.
- **Iterative preprocessing:** Maximum-depth chains do not risk Python recursion errors.
