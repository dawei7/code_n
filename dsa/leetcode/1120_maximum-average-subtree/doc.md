# Maximum Average Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-average-subtree](https://leetcode.com/problems/maximum-average-subtree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-average-subtree/).

### Goal
For every subtree in a binary tree, compute the average value of nodes in that subtree. Return the largest average.

### Function Contract
**Inputs**

- `root`: Root of a binary tree, represented in cOde(n) cases as a level-order list.

**Return value**

Maximum subtree average as a floating-point number.

### Examples
**Example 1**

- Input: `root = [5, 6, 1]`
- Output: `6.0`

**Example 2**

- Input: `root = [0, null, 1]`
- Output: `1.0`

**Example 3**

- Input: `root = [3]`
- Output: `3.0`

---

## Solution
### Approach
Use postorder DFS. For each node, compute the sum and count of its subtree from its children. The average for that subtree is `sum / count`; update a global best value with it.

Returning `(sum, count)` from each recursive call lets every subtree average be evaluated exactly once.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
