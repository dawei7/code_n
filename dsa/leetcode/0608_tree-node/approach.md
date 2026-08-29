## General

The table represents a tree using one row per node. A node’s own `p_id` tells whether it has a parent, while appearances of its `id` in other rows’ `p_id` values tell whether it has children.

The three categories form a priority-ordered classification:

1. `p_id IS NULL` means Root;
2. otherwise, appearing as some parent means Inner;
3. otherwise, the node has a parent but no child and is Leaf.

The `CASE` expression follows this order for every row.

**Identifying the root**

```sql
WHEN p_id IS NULL THEN 'Root'
```

The root is the only node without a parent in a valid tree. This test must come first. A one-node tree has no parent and no children; by the problem’s rule it is Root, not Leaf. First-match `CASE` semantics ensure the root classification wins before child checks.

**Identifying nodes with children**

```sql
WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
```

The subquery lists every parent reference used by any node. If current `id` appears there, at least one other row names it as parent, so it has at least one child.

Because the root was handled already, a remaining node that has children also has its own non-null parent and is exactly an Inner node.

The subquery includes the root row’s null `p_id`. SQL `IN` with a null-containing list has three-valued behavior: a matching non-null parent still yields true; a nonmatching ID may yield unknown rather than false. In a `WHEN` condition, unknown is not true, so execution falls to `ELSE`. The result remains correct. Filtering `WHERE p_id IS NOT NULL` would make the intent clearer and avoid this subtlety.

**Everything else is a leaf**

A row reaching:

```sql
ELSE 'Leaf'
```

is not root, so it has a parent. It did not match any parent reference, so it has no children. Those are exactly the leaf conditions.

For the sample, node 1 has null parent and is Root. Node 2 appears as `p_id` for nodes 4 and 5, so after failing the root test it is Inner. Nodes 3, 4, and 5 never appear as a parent and become Leaf.

**Why no joins or grouping are necessary**

The subquery is a membership test against the set/multiset of referenced parent IDs. Duplicate parent references do not affect `IN`: a node either appears at least once or it does not. The outer query retains one output row for each input node.

The selected `id` is unique by schema, so the result has exactly one classification per node. Any output order is accepted.

**Why the query is correct**

Take an arbitrary node. If its parent is null, validity of the tree makes it the root, and the first branch labels it Root.

Otherwise, it has a parent. If its ID occurs in the `p_id` column, at least one node is its child, so it is neither root nor leaf and the second branch labels it Inner. If its ID does not occur there, no row names it as parent, so it has no children and `ELSE` labels it Leaf.

These cases are exhaustive and mutually exclusive after priority is applied. Thus, every node receives exactly its defined type.

The valid-tree guarantee is essential context: it rules out multiple parentless roots, cycles, dangling parent references, and other graph structures for which the labels might require different interpretation.

## Complexity detail

Let $n$ be the number of nodes. A database can materialize/hash the `p_id` subquery in $O(n)$ expected time and space, then test each outer row in expected constant time, for expected $O(n)$ total work.

A sort-based membership/semijoin plan may take $O(n\log n)$ time, matching the manifest. Storing parent IDs or intermediate rows uses $O(n)$ space. Indexes on `p_id` can change the physical access strategy.

The output itself contains $n$ rows. SQL does not mandate which valid plan the engine chooses.

## Alternatives and edge cases

- **Left join to children and grouping:** Join each node to rows whose `p_id` equals its ID, then classify based on null parent and child count. Works but may multiply rows before grouping.
- **`EXISTS`:** `EXISTS (SELECT 1 FROM Tree child WHERE child.p_id = Tree.id)` directly tests for a child and avoids `IN` null semantics.
- **Three `UNION` branches:** Query roots, inner nodes, and leaves separately. More verbose and repeats table logic.
- **Root checked after parent membership:** Risky for a one-node tree or any root with children; root status must have priority.
- **One-node tree:** Null parent makes it Root even though it also has no children.
- **Root with children:** First branch still labels Root, not Inner.
- **Non-root with children:** Appears in `p_id` and becomes Inner.
- **Non-root without children:** Falls to Leaf.
- **Null inside `IN` subquery:** A nonmatch can be unknown; `CASE WHEN` treats it as not true and reaches Leaf. Filtering nulls is clearer.
- **Repeated parent IDs:** Merely mean multiple children and do not change membership.
- **Any output order:** No sort is required.
- **Valid-tree guarantee:** Ensures the categories cover the structure consistently.
