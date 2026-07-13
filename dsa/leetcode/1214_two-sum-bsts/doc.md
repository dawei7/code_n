# Two Sum BSTs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1214 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, Binary Search, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [two-sum-bsts](https://leetcode.com/problems/two-sum-bsts/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/two-sum-bsts/).

### Goal
Determine whether one node from the first binary search tree and one node from the second binary search tree can be chosen so their values sum to `target`.

### Function Contract
**Inputs**

- `root1: TreeNode` - Root of the first BST.
- `root2: TreeNode` - Root of the second BST.
- `target: int` - Desired sum.

**Return value**

`bool` - `True` if such a pair exists, otherwise `False`.

### Examples
**Example 1**

- Input: `root1 = [2, 1, 4], root2 = [1, 0, 3], target = 5`
- Output: `True`

**Example 2**

- Input: `root1 = [0, -10, 10], root2 = [5, 1, 7, 0, 2], target = 18`
- Output: `False`

**Example 3**

- Input: `root1 = [8, 3, 10], root2 = [6, 1, 9], target = 12`
- Output: `True`

---

## Solution
### Approach
Traverse one BST and store all of its values in a hash set. Then traverse the other BST and check whether `target - value` is already in the set. The BST ordering is not required for correctness in this direct approach, but the trees can be traversed with ordinary DFS.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `n` and `m` are the number of nodes in the two trees.
- **Space Complexity**: `O(n + h)`, where `n` values from the first tree are stored and `h` is recursion or stack depth while traversing.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
