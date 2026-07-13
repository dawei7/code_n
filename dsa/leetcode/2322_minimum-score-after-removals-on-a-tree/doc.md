# Minimum Score After Removals on a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2322 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-score-after-removals-on-a-tree](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/).

### Goal
Remove two edges from a node-valued tree, producing three components. Each component's value is the XOR of its node values. Minimize the difference between the largest and smallest component XOR.

### Function Contract
**Inputs**

- `nums`: values assigned to tree nodes.
- `edges`: undirected edges forming a tree.

**Return value**

The minimum possible spread among the three component XOR values.

### Examples
**Example 1**

- Input: `nums = [1, 5, 5, 4, 11]`, `edges = [[0, 1], [1, 2], [1, 3], [3, 4]]`
- Output: `9`

**Example 2**

- Input: `nums = [5, 5, 2, 4, 4, 2]`, `edges = [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 3]`, `edges = [[0, 1], [1, 2]]`
- Output: `2`

---

## Solution
### Approach
Root the tree and compute each subtree XOR together with DFS entry and exit times for ancestor tests. Every removed edge corresponds to detaching one non-root subtree. Enumerate pairs of detached subtree roots. If one is an ancestor of the other, derive the nested component XORs by subtraction through XOR; otherwise the two subtree XORs are separate components. The third value follows from the total tree XOR. Evaluate the spread for each pair.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
