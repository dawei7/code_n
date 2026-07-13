# Height of Binary Tree After Subtree Removal Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2458 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [height-of-binary-tree-after-subtree-removal-queries](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/).

### Goal
Given a binary tree, we must process a series of queries. Each query specifies a node to be removed from the tree. After removing the subtree rooted at that node, we need to determine the height of the remaining tree (the maximum distance from the root to any leaf). The tree structure remains intact for subsequent queries.

### Function Contract
**Inputs**

- `root`: The root node of the binary tree.
- `queries`: A list of integers representing the values of the nodes whose subtrees are to be removed.

**Return value**

- A list of integers where each element corresponds to the height of the tree after the removal specified by the query.

### Examples
**Example 1**

- Input: `root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]`
- Output: `[2]`

**Example 2**

- Input: `root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]`
- Output: `[3,2,3,2]`

**Example 3**

- Input: `root = [1,null,5,3,null,2,4], queries = [3,5,4,2,4]`
- Output: `[1,0,3,3,3]`

---

## Solution
### Approach
The problem is solved using a Depth-First Search (DFS) approach to pre-calculate the height of every node and the maximum height reachable at each depth level. By tracking the two largest heights at each depth, we can determine the new tree height after removing a subtree: if the removed node was on the path of the tallest branch at its depth, the height becomes the second-tallest branch at that depth; otherwise, it remains the tallest.

### Complexity Analysis
- **Time Complexity**: `O(N + Q)`, where `N` is the number of nodes in the tree and `Q` is the number of queries. We traverse the tree once to compute heights and then process each query in constant time.
- **Space Complexity**: `O(N)`, required to store the height and depth information for each node, as well as the pre-calculated results for each depth level.

### Reference Implementations
<details>
<summary>python</summary>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, queries: list[int]) -> list[int]:
    node_height = {}

    def get_height(node):
        if not node:
            return -1

        h = 1 + max(get_height(node.left), get_height(node.right))
        node_height[node.val] = h
        return h

    get_height(root)

    ans = {}

    def compute_results(node, depth, best_without_subtree):
        if not node:
            return

        ans[node.val] = best_without_subtree

        left_h = node_height[node.left.val] if node.left else -1
        right_h = node_height[node.right.val] if node.right else -1

        compute_results(node.left, depth + 1, max(best_without_subtree, depth + 1 + right_h))
        compute_results(node.right, depth + 1, max(best_without_subtree, depth + 1 + left_h))

    compute_results(root, 0, 0)
    return [ans[q] for q in queries]
```
</details>
