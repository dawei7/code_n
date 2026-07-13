# Sum of Root To Leaf Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1022 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-root-to-leaf-binary-numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/).

### Goal
Each root-to-leaf path in a binary tree forms a binary number by reading node values from root to leaf. Return the sum of all such numbers.

### Function Contract
**Inputs**

- `root`: Root node of a binary tree whose node values are `0` or `1`, represented in cOde(n) cases as a level-order list.

**Return value**

Integer sum of every root-to-leaf binary value.

### Examples
**Example 1**

- Input: `root = [1, 0, 1, 0, 1, 0, 1]`
- Output: `22`

**Example 2**

- Input: `root = [0]`
- Output: `0`

**Example 3**

- Input: `root = [1, 1]`
- Output: `3`

---

## Solution
### Approach
Run DFS while carrying the numeric value represented by the current path. When visiting a node, shift the accumulated value left by one bit and add the node's bit. If the node is a leaf, add that path value to the answer; otherwise continue into its children.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(h)` for recursion depth, where `h` is the tree height.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
