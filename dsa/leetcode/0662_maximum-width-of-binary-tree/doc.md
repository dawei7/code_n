# Maximum Width of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 662 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, return its maximum width over all levels. The width of one level is the number of complete-tree positions from its leftmost non-null node through its rightmost non-null node, including null positions between those two end-nodes.

Do not count absent positions outside the two end-nodes. Evaluate every depth and return the greatest width found; sparse descendants can therefore create a width larger than the number of actual nodes on that level. The answer is guaranteed to fit in a signed 32-bit integer.

### Function Contract
**Inputs**

- `root`: the non-null root node of a binary tree

**Return value**

- The maximum positional width of any tree level

### Examples
**Example 1**

- Input: `root = [1, 3, 2, 5, 3, null, 9]`
- Output: `4`

**Example 2**

- Input: `root = [1, 3, 2, 5, null, null, 9, 6, null, 7]`
- Output: `7`

**Example 3**

- Input: `root = [1, 3, 2, 5]`
- Output: `2`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Give real nodes their complete-tree positions**

Label the root position zero. If a node has position `p`, label its left child `2p` and right child $2p + 1$ after normalizing the current level. These labels preserve exactly how many complete-tree slots separate any two real nodes, without enqueuing missing nodes.

**Measure each level by its endpoints**

Process nodes level by level. Subtract the first position on the level from every position before creating child labels. This keeps numbers small while preserving all within-level differences. The level width is `last_position - first_position + 1`; after normalization the first position is zero, so it is simply the final normalized position plus one.

**Why indices count internal gaps correctly**

Complete-tree indexing assigns consecutive positions to every conceptual slot on a level. Real nodes retain the same positions they would have if every missing ancestor slot were explicitly expanded. Therefore the inclusive difference between the outer real-node indices counts both endpoints and every internal null position required by the definition. Taking the maximum over all levels returns the desired width.

#### Complexity detail

Each of the `N` real nodes enters and leaves the queue once, so time is $O(N)$. The queue stores at most one level of real nodes and can contain $O(N)$ entries, giving $O(N)$ space.

#### Alternatives and edge cases

- **Depth-first search with the first index at each depth:** also runs in $O(N)$ time and uses $O(H)$ traversal state, but recursive depth may be a concern for skewed trees.
- **Materialize null placeholders:** mirrors the definition visually, but a sparse tree can create exponentially many conceptual slots relative to its real-node count.
- **Count only real nodes per level:** misses internal gaps and therefore does not implement positional width.
- A single-node tree has width one.
- A level with one real node has width one regardless of its conceptual position.
- Normalizing indices per level preserves widths and avoids unnecessarily large integers on deep trees.

</details>
