# Maximum Level Sum of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-level-sum-of-a-binary-tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/).

### Goal
Given a binary tree, return the smallest 1-indexed level whose node values have the maximum sum.

### Function Contract
**Inputs**

- `root`: Root of a binary tree.

**Return value**

Level number with the largest level sum.

### Examples
**Example 1**

- Input: `root = [1,7,0,7,-8,null,null]`
- Output: `2`

**Example 2**

- Input: `root = [989,null,10250,98693,-89388,null,null,null,-32127]`
- Output: `2`

**Example 3**

- Input: `root = [1]`
- Output: `1`

---

## Solution
### Approach
Traverse the tree level by level with a queue. For each level, sum all node values and update the best level only when the sum is strictly larger than the previous best. Keeping the first maximum automatically gives the smallest level number.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(w)`, where `w` is the maximum width of the tree.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
