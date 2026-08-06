## Examples

**Example 1**

```mermaid
flowchart TD
    accTitle: Example 1 binary tree
    accDescr: Root 1 has left child 2 and right child 3.
    one["1"] -->|left| two["2"]
    one -->|right| three["3"]
```

- **Input:** `root = [1,2,3]`
- **Output:** `2`
- **Explanation:** The longest consecutive path is `[1,2]` in increasing order, or the same edge traversed as
  `[2,1]` in decreasing order.

**Example 2**

```mermaid
flowchart TD
    accTitle: Example 2 binary tree
    accDescr: Root 2 has left child 1 and right child 3, forming a consecutive path through the root.
    two["2"] -->|left| one["1"]
    two -->|right| three["3"]
```

- **Input:** `root = [2,1,3]`
- **Output:** `3`
- **Explanation:** The child-parent-child traversal `[1,2,3]` is increasing and consecutive. Traversing the same
  nodes in reverse gives the equally valid decreasing path `[3,2,1]`.
