## Examples

**Example 1**

```mermaid
flowchart TB
    accTitle: Example 1 binary tree
    accDescr: Root node 1 has leaf 3 as its left child and leaf 2 as its right child.
    N1["1"] --> N3["3"]
    N1 --> N2["2"]
```

- Input: `root = [1,3,2], k = 1`
- Output: `2`
- Explanation: Leaves `2` and `3` are equally near the target node `1`, so either value is valid.

**Example 2**

```mermaid
flowchart TB
    accTitle: Example 2 single-node binary tree
    accDescr: The tree contains only node 1, which is both the root and a leaf.
    N1["1"]
```

- Input: `root = [1], k = 1`
- Output: `1`
- Explanation: The root is itself the nearest leaf.

**Example 3**

```mermaid
flowchart TB
    accTitle: Example 3 binary tree
    accDescr: Root 1 has children 2 and leaf 3. Node 2 has left child 4, node 4 has left child 5, and node 5 has left child leaf 6.
    N1["1"] --> N2["2"]
    N1 --> N3["3"]
    N2 --> N4["4"]
    N4 --> N5["5"]
    N5 --> N6["6"]
```

- Input: `root = [1,2,3,4,null,null,null,5,null,6], k = 2`
- Output: `3`
- Explanation: Leaf `3`, rather than leaf `6`, has the smaller edge distance from node `2`.
