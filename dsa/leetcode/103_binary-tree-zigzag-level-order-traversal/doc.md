# Binary Tree Zigzag Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 103 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, return the zigzag level order traversal of its node values. The root level is read from left to right, the next level from right to left, and all following levels continue this alternating pattern.

Return one list for each level, ordered from the root toward the leaves. Reversing a level changes only the order in which its values appear; it does not change parent-child relationships or the order used to discover the following level. Omit missing children entirely, and return an empty list when the tree has no root.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

A list of value lists in alternating zigzag level order.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [20, 9], [15, 7]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Keep discovery order ordinary even when display order alternates**

Use the same breadth-first queue and frozen level size as ordinary level order. Always enqueue children left before right, regardless of the current display direction. This keeps the next level's structural order correct and confines zigzag behavior to output formatting.

**A deque reverses one level without reversing tree discovery**

For a left-to-right level, append each value to the right end of a temporary deque. For a right-to-left level, append each encountered value to the left end. Convert that deque to the level result and toggle direction exactly once after the whole level.

Changing child enqueue order instead is possible with a two-stack design, but mixing that technique with a single FIFO queue can scramble later levels.

**Direction changes presentation, not parent-child reachability**

At the start of each outer iteration, the queue contains exactly the next depth in left-to-right order. The direction flag states how those nodes must appear in the output without changing the order used to discover their children.

**Trace a reversed level whose children stay ordered**

For `[3, 9, 20, null, null, 15, 7]`, depth zero yields `[3]`. Depth one is read in reverse as `[20, 9]`, while its children still enter the queue left first. Depth two therefore becomes `[15, 7]` when direction switches back.

**Reverse only the level output, not child discovery**

Breadth-first processing still groups nodes by unique depth and discovers every level left to right. On a forward level, appending values preserves that order; on a reverse level, inserting them at the opposite deque end yields right-to-left output without disturbing child enqueue order.

Children therefore form the next queue correctly regardless of display direction. Toggling once after the complete level alternates the emitted orientation at every depth.

#### Complexity detail

Every node is enqueued, dequeued, and inserted into a level once, giving $O(n)$ time. The queue and current level hold at most $O(w)$ nodes, where `w` is maximum tree width, excluding the returned output.

#### Alternatives and edge cases

- **Collect then reverse alternate levels:** is also $O(n)$ but performs an extra pass over those level lists.
- **Two stacks:** naturally alternate direction but require more state than one queue and a flag.
- **Ordinary level order:** never reverses levels and solves Problem 102 instead.
- The root level is left to right by definition. Empty input produces no levels and requires no direction toggle.
- Prepending to an ordinary immutable string or array can be costly; a deque provides constant-time insertion at both ends.

</details>
