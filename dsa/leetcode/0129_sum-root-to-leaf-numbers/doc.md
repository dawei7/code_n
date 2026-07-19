# Sum Root to Leaf Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/) |

## Problem Description
### Goal
Given a binary tree whose node values are decimal digits from `0` through `9`, interpret every complete root-to-leaf path as one base-ten number. Reading downward supplies the digits from most significant to least significant, so the path $1 \to 2 \to 3$ represents `123`.

Return the sum of the numbers represented by all root-to-leaf paths. Shared prefixes contribute independently to every path that continues from them, and only leaves terminate numbers; an internal prefix is not an additional value. Leading zero digits are valid and simply do not change the numeric value. An empty tree contributes no paths and returns `0`.

### Function Contract
**Inputs**

- `root`: a `TreeNode` whose values are digits `0..9`, encoded as a level-order list in app cases

**Return value**

The sum of the numbers represented by every root-to-leaf path.

### Examples
**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `25`

**Example 2**

- Input: `root = [4, 9, 0, 5, 1]`
- Output: `1026`

**Example 3**

- Input: `root = [0]`
- Output: `0`
