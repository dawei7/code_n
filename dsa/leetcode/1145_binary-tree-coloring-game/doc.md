# Binary Tree Coloring Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1145 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [binary-tree-coloring-game](https://leetcode.com/problems/binary-tree-coloring-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/binary-tree-coloring-game/).

### Goal
In a two-player coloring game on a binary tree, the first player colors node `x`. The second player then chooses another node. Each player expands only from already colored nodes to adjacent uncolored nodes. Determine whether the second player can guarantee coloring more than half of the nodes.

### Function Contract
**Inputs**

- `root`: Root of the binary tree, represented in cOde(n) cases as a level-order list.
- `n`: Total number of nodes.
- `x`: Value of the node initially chosen by the first player.

**Return value**

Boolean indicating whether the second player has a winning choice.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3`
- Output: `true`

**Example 2**

- Input: `root = [1,2,3], n = 3, x = 1`
- Output: `false`

**Example 3**

- Input: `root = [1,2,3,4,5], n = 5, x = 2`
- Output: `true`

---

## Solution
### Approach
The first player's node `x` partitions the tree into three regions: `x`'s left subtree, `x`'s right subtree, and the rest of the tree above `x`. The second player can choose a node inside any one of these regions and capture that whole region if it contains more than half of all nodes.

Find `x`, count the sizes of its left and right subtrees, and compute the parent-side size as `n - left - right - 1`. The second player wins if the maximum of these three sizes is greater than `n / 2`.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
