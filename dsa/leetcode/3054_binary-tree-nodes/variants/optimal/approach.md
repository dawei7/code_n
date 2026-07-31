## General

**Recognize the root from its own row.** A node with `P IS NULL` has no parent,
so it is the root. This check must come first: a singleton root also has no
children, but the contract labels it `Root`, not `Leaf`.

**Recognize inner nodes from other rows.** Collect the non-null values stored
in `P`. If a non-root node's `N` belongs to that set, at least one row names it
as a parent, so it has a child and is `Inner`. Filtering null from the subquery
keeps SQL's three-valued `IN` semantics from contaminating membership tests.

Every remaining node has a parent but is never itself referenced as a parent,
which is exactly the definition of `Leaf`. The three CASE branches are
mutually exclusive and exhaustive. Finally, order by `N` ascending.

## Complexity detail

Let $n$ be the number of nodes. With a hashed or indexed parent-membership
set, building the set and classifying rows take expected $O(n)$ time. Sorting
all output rows costs $O(n\log n)$, which determines the total bound. The
parent set uses $O(n)$ auxiliary space. Physical SQL plans may implement the
membership subquery as a semi-join with equivalent asymptotic behavior.

## Alternatives and edge cases

- **Self-join and group:** Left joining each node to its children is correct, but aggregation is unnecessary when only child existence matters.
- **Correlated `EXISTS`:** This states child existence directly and performs well with an index on `P`, but may rescan without one.
- **Infer roles from numeric values:** Node identifiers can be sparse and carry no structural ordering information.
- The root check precedes child membership so a one-node tree is `Root`.
- Null parent values must be excluded from `IN` membership.
- An inner node needs at least one child; the number or side of its children is irrelevant.
- Output ordering is numeric by `N`, not insertion order.
