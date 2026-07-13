# Path In Zigzag Labelled Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1104 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [path-in-zigzag-labelled-binary-tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/).

### Goal
In a perfect binary tree, labels are assigned level by level, but every other level is labelled right-to-left. Given a label, return the path of labels from the root to that node.

### Function Contract
**Inputs**

- `label`: Positive node label in the zigzag-labelled tree.

**Return value**

List of labels on the path from root to `label`.

### Examples
**Example 1**

- Input: `label = 14`
- Output: `[1, 3, 4, 14]`

**Example 2**

- Input: `label = 26`
- Output: `[1, 2, 6, 10, 26]`

**Example 3**

- Input: `label = 1`
- Output: `[1]`

---

## Solution
### Approach
Work upward from `label` to the root. For a normal labelled tree, the parent would be `label // 2`. In zigzag labelling, first map the current label to its mirror position within the level, move to the parent in the normal tree, then continue.

For a level with labels from `start` to `end`, the mirrored label is `start + end - label`. Repeating this computation produces the path in reverse, which is then reversed for the answer.

### Complexity Analysis
- **Time Complexity**: `O(log label)`.
- **Space Complexity**: `O(log label)` for the path.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
