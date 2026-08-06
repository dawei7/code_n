## Examples

**Example 1**

- Input: `tree = [2,1,3], node = 1`
- Output: `2`
- **Explanation:** The node whose value is `2` immediately follows the selected node whose value is `1` in inorder
  order. Both the input and the returned result are `Node` objects.

The first source diagram has the following tree structure:

```mermaid
flowchart TB
    accTitle: Three-node BST for Example 1
    accDescr: Root 2 has left child 1, the selected node, and right child 3. Node 2 is the successor of node 1.
    n2(("2<br/>successor")) --> n1(("1<br/>node"))
    n2 --> n3(("3"))
```

**Example 2**

- Input: `tree = [5,3,6,2,4,null,null,1], node = 6`
- Output: `null`
- **Explanation:** The selected node whose value is `6` is last in inorder order, so it has no successor.

The second source diagram has the following tree structure:

```mermaid
flowchart TB
    accTitle: BST for Example 2
    accDescr: Root 5 has children 3 and 6. Node 3 has children 2 and 4, and node 2 has left child 1. Node 6 is selected.
    n5(("5")) --> n3(("3"))
    n5 --> n6(("6<br/>node"))
    n3 --> n2(("2"))
    n3 --> n4(("4"))
    n2 --> n1(("1"))
```
