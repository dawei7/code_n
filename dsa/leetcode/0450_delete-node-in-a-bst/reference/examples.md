## Examples

**Example 1**

- Input: `root = [5,3,6,2,4,null,7], key = 3`
- Output: `[5,4,6,2,null,null,7]`

- **Explanation:** The node with value `3` is present, so it is removed. Replacing it with `4` produces one valid result:

```mermaid
flowchart LR
    accTitle: Deleting node 3 using its inorder successor
    accDescr: The original BST rooted at 5 has node 3 with children 2 and 4. After deleting 3, node 4 takes its place and keeps child 2, while the right subtree rooted at 6 is unchanged.
    subgraph Before[Before deletion]
        b5((5)) --> b3((3))
        b5 --> b6((6))
        b3 --> b2((2))
        b3 --> b4((4))
        b6 --> b7((7))
    end
    subgraph After[After deletion]
        a5((5)) --> a4((4))
        a5 --> a6((6))
        a4 --> a2((2))
        a6 --> a7((7))
    end
    Before -. delete 3 .-> After
```

The BST shape is not unique. Promoting `2` instead gives the equally valid result `[5,2,6,null,4,null,7]`:

```mermaid
flowchart TD
    accTitle: Alternative valid tree after deleting node 3
    accDescr: The tree remains rooted at 5. Its left child is 2, whose right child is 4. Its right child is 6, whose right child is 7.
    n5((5)) --> n2((2))
    n5 --> n6((6))
    n2 --> n4((4))
    n6 --> n7((7))
```

**Example 2**

- Input: `root = [5,3,6,2,4,null,7], key = 0`
- Output: `[5,3,6,2,4,null,7]`

- **Explanation:** No node contains `0`, so there is nothing to delete.

**Example 3**

- Input: `root = [], key = 0`
- Output: `[]`
