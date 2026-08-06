## Examples

**Example 1**

```mermaid
graph TD
    accTitle: Three-node example tree
    accDescr: Node 0 is connected to nodes 1 and 2, so the path from 1 through 0 to 2 contains two edges.
    n0(("0")) --- n1(("1"))
    n0 --- n2(("2"))
```

- Input: `edges = [[0,1],[0,2]]`
- Output: `2`
- Explanation: The longest path is `1 - 0 - 2`, which contains two edges.

**Example 2**

```mermaid
graph TD
    accTitle: Six-node example tree
    accDescr: Node 1 connects to nodes 0, 2, and 4; node 2 connects to 3; and node 4 connects to 5. The longest path runs from 3 through 2, 1, and 4 to 5.
    n1(("1")) --- n0(("0"))
    n1 --- n2(("2"))
    n1 --- n4(("4"))
    n2 --- n3(("3"))
    n4 --- n5(("5"))
```

- Input: `edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]`
- Output: `4`
- Explanation: The longest path is `3 - 2 - 1 - 4 - 5`, which contains four edges.
