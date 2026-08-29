## General

A valid path may travel from a child up through a parent and down into another child. Therefore one downward length per node is not enough: the algorithm must know how far a consecutive chain can approach the node in each numeric direction.

For each subtree root, `dfs` returns two lengths:

- `incr`: the longest downward-branch path that ends at this root with values increasing by one while moving from the descendant toward the root;
- `decr`: the longest such path that ends at this root with values decreasing by one toward the root.

Both begin at one because the current node alone is a valid path of one node.

For `None`, DFS returns `[0, 0]` so an absent child contributes no branch.

**Process both child subtrees first.** The calls return `i1, d1` for the left child and `i2, d2` for the right child. These child results describe the best branches ending at those child nodes.

**Extend an increasing-toward-root branch.** If:

`root.left.val + 1 == root.val`,

then the left child's value is one less than the root. A branch increasing toward the left child can append the root and remain consecutive increasing, so:

`incr = i1 + 1`.

The right child is checked the same way, using `max(incr, i2 + 1)` because only one child branch can be returned upward through this node.

**Extend a decreasing-toward-root branch.** If:

`root.left.val - 1 == root.val`,

then the left child is one greater than the root. A branch decreasing toward that child can append the root, so `decr = d1 + 1`. The right child may provide a longer alternative and is combined with `max`.

A child whose value differs by anything other than one cannot extend either branch, even if its subtree contains a long consecutive path internally. That internal path has already updated the global answer during its own DFS.

**Join opposite-direction arms through the current node.** A full consecutive path can approach the root along an increasing arm from a lower-valued descendant and leave along the reverse of a decreasing-toward-root arm toward a higher-valued descendant. Its length is:

`incr + decr - 1`.

The root belongs to both arm lengths, so subtracting one prevents counting it twice.

For tree `[2,1,3]`, the left child extends `incr` to two because one plus one equals two. The right child extends `decr` to two because three minus one equals two. Combining gives `2 + 2 - 1 = 3`, representing path `[1,2,3]`.

For `[1,2,3]`, both children are larger than the root. They compete for the same `decr` direction, so `max` selects an arm of length two rather than adding both. The two-child path `[2,1,3]` is not consecutive because its changes are minus one then plus two. The answer is correctly two.

**Why same-direction child branches cannot both be joined.** A simple path through a node may use two children, but to remain globally increasing or decreasing, one side must approach the node in one direction and the other must leave in the complementary direction. Joining two children both one greater than the root would create a valley such as `2,1,3` whose endpoint difference across the second edge is not the continuation of one-step monotonic order.

**Why the returned pair is sufficient for the parent.** A path extended through the parent can use only one downward branch from the current node. Among all branches with the same direction, only the longest can ever be better. Internal two-arm paths cannot be extended upward as simple paths without branching, so they belong only in `ans`.

**Why every valid path is considered.** Any simple tree path has a highest node relative to the root. If it uses two sides there, one arm must supply the increasing-toward-node direction and the other the decreasing-toward-node direction for the whole sequence to stay monotonic. The algorithm computes the longest eligible arm of each kind and evaluates their combination at every node. One-sided paths are included because the other length remains one.

The shared `ans` records the best path anywhere. Node values may be negative; only differences of exactly one matter.

## Complexity detail

Let $n$ be the node count and $h$ the height. Each node is visited once and performs constant comparisons and arithmetic, so time is $O(n)$.

The recursion stack contains at most $O(h)$ frames. Each frame stores a constant number of lengths, giving $O(h)$ auxiliary space, matching the manifest.

No path lists or per-node tables are retained.

## Alternatives and edge cases

- **Start a search from every node:** It repeatedly explores the same subtrees and can take $O(n^2)$ time.
- **Return only one longest chain:** It loses the distinction between increasing and decreasing arms needed for child-parent-child paths.
- **Join two same-direction arms:** This creates a turn in numeric direction and may not be a valid consecutive sequence.
- **Single node:** Both lengths are one and the answer becomes one.
- **Only one compatible child:** One arm extends and the other remains one, so the one-sided path is counted.
- **Difference greater than one:** That edge cannot extend either direction.
- **Longest path below the root:** Descendant calls update the shared answer before returning.
- **Negative values:** Plus/minus-one comparisons behave identically.
- **Equal adjacent values:** Difference zero is not consecutive and does not extend a branch.
- **Skewed tree:** Time remains linear, while recursion space becomes $O(n)$.
- **Root guaranteed nonempty:** The initial answer zero is replaced during the traversal.
