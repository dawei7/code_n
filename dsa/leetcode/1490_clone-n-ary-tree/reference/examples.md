## Examples

**Example 1**

- **Input:** `root = [1,null,3,2,4,null,5,6]`

```mermaid
flowchart TD
    accTitle: Example 1 N-ary tree
    accDescr: Root node 1 has three children 3, 2, and 4. Node 3 has two children 5 and 6.
    n1["1 (root)"] --> n3["3"]
    n1 --> n2["2"]
    n1 --> n4["4"]
    n3 --> n5["5"]
    n3 --> n6["6"]
```

- **Output:** `[1,null,3,2,4,null,5,6]`
- **Explanation:** The cloned tree reproduces the root's child order `3, 2, 4` and the child nodes `5, 6` under node `3`, with every node object independently allocated.

**Example 2**

- **Input:** `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`

```mermaid
flowchart TD
    accTitle: Example 2 N-ary tree
    accDescr: Multi-level N-ary tree rooted at 1 with four main subtrees rooted at 2, 3, 4, and 5.
    n1["1 (root)"] --> n2["2"]
    n1 --> n3["3"]
    n1 --> n4["4"]
    n1 --> n5["5"]
    n3 --> n6["6"]
    n3 --> n7["7"]
    n7 --> n11["11"]
    n11 --> n14["14"]
    n4 --> n8["8"]
    n8 --> n12["12"]
    n5 --> n9["9"]
    n5 --> n10["10"]
    n9 --> n13["13"]
```

- **Output:** `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- **Explanation:** Subtrees with varying depths and branching factors are cloned in exact structural order.

**Example 3**

- **Input:** `root = []`
- **Output:** `[]`
