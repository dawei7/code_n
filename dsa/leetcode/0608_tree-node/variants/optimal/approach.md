## General
**Recognize the root from its own row**

A null `p_id` directly identifies the root. Test this condition first because the root may also appear as a parent and must still be labeled `Root`.

**Collect all actual parent identifiers**

Select distinct non-null `p_id` values. Any nonroot node whose `id` occurs in this set has at least one child and is therefore an inner node.

**Classify everything else as a leaf**

Left join every tree row to the parent-ID set. After the root case, a match means `Inner`; a missing match means the node has no children and is `Leaf`.

**Why the three labels are exact**

Every node either has a null parent or does not, separating the root from all others. Among nonroots, appearing in another row's `p_id` column is exactly the definition of having a child. That condition partitions the remaining nodes into inner nodes and leaves, so each row receives one correct label.

## Complexity detail
For `n` rows, deduplicating parent IDs, joining them, and ordering output generally take $O(n \log n)$ time and $O(n)$ working space. Indexes on `id` and `p_id` can reduce join costs.

## Alternatives and edge cases
- **Uncorrelated `IN` subquery:** test whether each nonroot ID belongs to the set of non-null parent IDs; it has the same semantic structure.
- **Correlated child existence:** is direct, but without an index it may rescan the tree for every node and take $O(n^2)$ time.
- **Root with children:** remains `Root`, not `Inner`.
- **Single-node tree:** the only node is the root.
- **Nonroot with one or two children:** is `Inner`.
- **Nonroot with no children:** is `Leaf`.
- **Nonconsecutive identifiers:** do not affect parent relationships.
- **Input order:** does not affect classification.
