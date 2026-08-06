## Examples

**Example 1**

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `leaf = 7`
- **Output:** `[7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]`
- **Explanation:** Node 7 becomes the new root. Node 2 becomes its left child, 5 becomes 2's left child, 3 becomes 5's left child.

**Example 2**

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `leaf = 0`
- **Output:** `[0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]`
- **Explanation:** Node 0 becomes the new root of the tree.
