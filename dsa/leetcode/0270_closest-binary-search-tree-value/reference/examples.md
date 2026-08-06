## Examples

**Example 1**

- Input: `root = [4,2,5,1,3], target = 3.714286`

The level-order input represents this BST:

```mermaid
flowchart TB
    accTitle: Example 1 binary search tree
    accDescr: Root 4 has left child 2 and right child 5. Node 2 has left child 1 and right child 3.
    n4["4"] --> n2["2"]
    n4 --> n5["5"]
    n2 --> n1["1"]
    n2 --> n3["3"]
```

- Output: `4`

**Example 2**

- Input: `root = [1], target = 4.428571`
- Output: `1`
