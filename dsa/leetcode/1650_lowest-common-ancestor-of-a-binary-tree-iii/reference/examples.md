## Examples

**Example 1**

```mermaid
flowchart TD
    accTitle: Binary Tree for LCA Example 1
    accDescr: Binary tree with root 3, left subtree headed by 5, right subtree headed by 1. Nodes p=5 and q=1 meet at root 3.
    N3(("3")) --- N5(("5"))
    N3 --- N1(("1"))
    N5 --- N6(("6"))
    N5 --- N2(("2"))
    N1 --- N0(("0"))
    N1 --- N8(("8"))
    N2 --- N7(("7"))
    N2 --- N4(("4"))
```

- **Input:** `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1`
- **Output:** `3`
- **Explanation:** The lowest common ancestor of nodes 5 and 1 is node 3.

**Example 2**

```mermaid
flowchart TD
    accTitle: Binary Tree for LCA Example 2
    accDescr: Binary tree with root 3 and node 5 as parent of node 4. Since node 5 is an ancestor of node 4 and also ancestor of itself, LCA is 5.
    N3(("3")) --- N5(("5"))
    N3 --- N1(("1"))
    N5 --- N6(("6"))
    N5 --- N2(("2"))
    N1 --- N0(("0"))
    N1 --- N8(("8"))
    N2 --- N7(("7"))
    N2 --- N4(("4"))
```

- **Input:** `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4`
- **Output:** `5`
- **Explanation:** Node 5 is an ancestor of node 4 and is also its own ancestor, so the LCA of nodes 5 and 4 is node 5.

**Example 3**

- **Input:** `root = [1, 2], p = 1, q = 2`
- **Output:** `1`
- **Explanation:** Node 1 is the parent of node 2, so the lowest common ancestor is node 1.
