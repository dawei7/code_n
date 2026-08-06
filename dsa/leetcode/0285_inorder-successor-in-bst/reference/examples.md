## Examples

**Example 1**

- Input: `root = [2,1,3], p = 1`
- Output: `2`
- Explanation: Node `2` is the first node after `p` in inorder order. Both `p` and the native return value are `TreeNode` objects, even though the example displays their values.

```mermaid
flowchart TB
    accTitle: Example 1 binary search tree
    accDescr: Root 2 has target node 1 as its left child and node 3 as its right child.
    N2["2"] --> N1["1 (p)"]
    N2 --> N3["3"]
```

**Example 2**

- Input: `root = [5,3,6,2,4,null,null,1], p = 6`
- Output: `null`
- Explanation: Node `6` is the greatest node in the tree, so there is no inorder successor.

```mermaid
flowchart TB
    accTitle: Example 2 binary search tree
    accDescr: Root 5 has children 3 and target node 6. Node 3 has children 2 and 4, and node 2 has left child 1.
    N5["5"] --> N3["3"]
    N5 --> N6["6 (p)"]
    N3 --> N2["2"]
    N3 --> N4["4"]
    N2 --> N1["1"]
```
