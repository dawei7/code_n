## Examples

**Example 1**

- **Input:** `root = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 4, q = 1`
- **Output:** `[[1, [2, 3, 4]], [2, [5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]]`
- **Explanation:** Node 4 leaves node 2 and becomes node 1's last child, carrying nodes 7 and 8 with it.

**Example 2**

- **Input:** `root = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 7, q = 4`
- **Output:** the same tree
- **Explanation:** Node 7 is already a direct child of node 4, so no reordering occurs.

**Example 3**

- **Input:** `tree = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 1, q = 8`
- **Output:** `[[8, [1]], [1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7]], [5, []], [6, []], [7, []]]`
- **Explanation:** Because node 8 starts below node 1, node 8 is detached first, becomes the root, and receives node 1 as its last child.
