## Examples

**Example 1**

- **Input:** `root = [1,2,3]`, `from_value = 2`, `to_value = 3`
- **Output:** `[1,null,3]`
- **Explanation:** Node 2 is the invalid node (its right child points to 3 on the same level). Node 2 and its subtree are removed.

**Example 2**

- **Input:** `root = [8,3,1,7,null,9,4,2,null,null,null,5,6]`, `from_value = 7`, `to_value = 4`
- **Output:** `[8,3,1,null,null,9,4,null,null,5,6]`
- **Explanation:** Node 7 is the invalid node (its right child points to 4 on the same level). Node 7 and its child 2 are removed.

**Example 3**

- **Input:** A single-branch tree where an internal node's right pointer points horizontally to an existing same-level right node.
- **Output:** The tree with that internal node and its left/right subtrees removed.
- **Explanation:** Removing the invalid node detaches its entire subtree.
