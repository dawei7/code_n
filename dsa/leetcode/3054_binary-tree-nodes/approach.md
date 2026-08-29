## General

**Classify root status from the node's own row.** In `Tree`, column `P` stores a node's parent. A null parent means the node is the root. The outer `IF` checks `t1.P IS NULL` first and returns `'Root'`.

This priority matters because the root can also have children. Its child status must not cause it to be labeled inner.

**Discover children with a self left join.** Alias `t1` represents the node being classified. Alias `t2` represents a potential child. The join condition is

`t1.N = t2.P`.

Whenever another row names `t1.N` as its parent, that row joins as a child. If no such row exists, the left join still preserves `t1` and supplies null values for `t2`.

**Distinguish leaf from inner using join presence.** For a non-root:

- if `t2.P IS NULL`, no child row matched, so the node is `'Leaf'`;
- otherwise at least one child exists, so it is `'Inner'`.

On a real match, `t2.P` equals `t1.N`. Node values are genuine identifiers, so that parent field is non-null. On a missing match, it is null because of left-join extension. The test therefore doubles as a match-existence check.

**Collapse multiple child matches.** A binary-tree inner node can have two children. The self-join would then produce two identical output classifications for `t1.N`. `SELECT DISTINCT` removes those duplicates so every node appears once.

The query selects both node value and label. Every duplicate child row for one parent yields the same label, making `DISTINCT` safe.

**Sort by node value.** `ORDER BY 1` refers to the first selected column, `N`, and orders it ascending by default.

**Trace the example tree.** Node 5 has null parent, so it is Root even though nodes 2 and 8 join as children. Node 2 has parent 5 and child rows 1 and 3, so the inner `IF` sees a non-null joined parent and labels it Inner; `DISTINCT` merges the two joined rows. Node 1 has parent 2 but no row whose `P` equals 1, so the left join is unmatched and it becomes Leaf.

**Why the categories are exhaustive.** A node either has null parent or not. The first case is root. A non-root either appears as some other row's parent or it does not. Those cases are inner and leaf respectively. The join and nested `IF` implement exactly this decision tree.

**Why a left join is required.** An inner join would discard nodes with no children, precisely the leaves that must be reported. The left join preserves them and uses null extension as evidence of absence.

## Complexity detail

Let $R$ be the number of nodes. With an index on parent column `P`, matching children can be found efficiently; ordering and duplicate elimination commonly lead to an $O(R\log R)$ logical upper bound. Without a useful index, a naive nested-loop self-join could degrade toward $O(R^2)$.

The joined relation has at most two child matches per node for a valid binary tree, so it remains $O(R)$ rows before duplicate elimination. Sorting or distinct processing may require $O(R)$ temporary space.

Database complexity is plan-dependent; the manifest's $O(R\log R)$ time and $O(R)$ space describe a reasonable indexed execution with final ordering.

## Alternatives and edge cases

- **`EXISTS` correlated subquery:** Check whether any row has `P=t1.N`. It avoids duplicate child rows and therefore removes the need for `DISTINCT`.
- **Parent-value set CTE:** Materialize distinct non-null parents, then left join that set to nodes. This makes child existence explicit.
- **Inner join:** It is incorrect because leaves would vanish from the result.
- **Root with children:** The outer root check takes priority and returns Root.
- **Root with no children:** A one-node tree is still Root, not Leaf, because null parent is checked first.
- **Node with two children:** Join duplication is collapsed by `DISTINCT`.
- **Non-root with no children:** Null-extended `t2.P` yields Leaf.
- **Non-root with a child:** At least one match yields Inner.
- **Ascending order:** `ORDER BY 1` sorts by node value `N`.
- **Valid-tree assumption:** The classification assumes the table represents a tree; cycles or multiple roots would be labeled mechanically from the same rules.
- **Why checking `t2.P` signals a match:** On a genuine child row, the join predicate makes `t2.P=t1.N`, so it is non-null for a valid node identifier. On no match, left-join null extension makes it null. A dedicated child ID test would communicate this more directly but behave the same.
- **Distinct cost is caused by the join shape:** Without `DISTINCT`, a parent appears once per child. A valid binary tree limits this to two, but the required result still needs exactly one row per node.
- **Node values need not be consecutive:** Classification uses equality relationships, not arithmetic on `N`. Sparse, negative, or large identifiers would work identically if allowed by the table.
- **Ordering after deduplication:** The final sort acts on the one-row-per-node result, ensuring duplicate child matches do not disturb the ascending node sequence.
