## Examples

**Example 1**

```mermaid
flowchart TD
    accTitle: Binary Tree for LCA IV Example 1
    accDescr: Binary tree with root 3. Targets 4 and 7 are children of node 2, so LCA is 2.
    N3(("3")) --- N5(("5"))
    N3 --- N1(("1"))
    N5 --- N6(("6"))
    N5 --- N2(("2"))
    N1 --- N0(("0"))
    N1 --- N8(("8"))
    N2 --- N7(("7"))
    N2 --- N4(("4"))
```

- **Input:** `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], nodes = [4, 7]`
- **Output:** `2`
- **Explanation:** The lowest common ancestor of nodes 4 and 7 is node 2.

**Example 2**

```mermaid
flowchart TD
    accTitle: Binary Tree for LCA IV Example 2
    accDescr: Binary tree with root 3 and single target node 1. Node 1 is its own ancestor.
    N3(("3")) --- N5(("5"))
    N3 --- N1(("1"))
    N5 --- N6(("6"))
    N5 --- N2(("2"))
    N1 --- N0(("0"))
    N1 --- N8(("8"))
    N2 --- N7(("7"))
    N2 --- N4(("4"))
```

- **Input:** `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], nodes = [1]`
- **Output:** `1`
- **Explanation:** Node 1 is the sole target, so it is its own lowest common ancestor.

**Example 3**

```mermaid
flowchart TD
    accTitle: Binary Tree for LCA IV Example 3
    accDescr: Binary tree with root 3. Targets 7, 6, 2, and 4 all reside in the left subtree headed by node 5.
    N3(("3")) --- N5(("5"))
    N3 --- N1(("1"))
    N5 --- N6(("6"))
    N5 --- N2(("2"))
    N1 --- N0(("0"))
    N1 --- N8(("8"))
    N2 --- N7(("7"))
    N2 --- N4(("4"))
```

- **Input:** `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], nodes = [7, 6, 2, 4]`
- **Output:** `5`
- **Explanation:** All four target nodes (7, 6, 2, 4) reside in the subtree rooted at node 5, so node 5 is the LCA.
