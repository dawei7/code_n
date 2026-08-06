## Examples

**Example 1**

- Input: `s = "4(2(3)(1))(6(5))"`
- Output: `[4,2,6,3,1,5]`

The source diagram has the following tree structure:

```mermaid
flowchart TB
    accTitle: Binary tree constructed in Example 1
    accDescr: Root 4 has children 2 and 6. Node 2 has children 3 and 1. Node 6 has left child 5 and no right child.
    n4(("4")) --> n2(("2"))
    n4 --> n6(("6"))
    n2 --> n3(("3"))
    n2 --> n1(("1"))
    n6 --> n5(("5"))
```

**Example 2**

- Input: `s = "4(2(3)(1))(6(5)(7))"`
- Output: `[4,2,6,3,1,5,7]`

**Example 3**

- Input: `s = "-4(2(3)(1))(6(5)(7))"`
- Output: `[-4,2,6,3,1,5,7]`
