# Check Completeness of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 958 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [check-completeness-of-a-binary-tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) |

## Problem Description

### Goal

Given the `root` of a binary tree, determine whether the tree is complete. In a complete binary tree, every level before the last is completely filled.

The last level may contain fewer nodes, but its nodes must occupy the leftmost available positions without any gap before a later node. Equivalently, a level-order listing that includes missing child positions may contain no non-null node after the first missing position. Return whether the supplied tree satisfies this structure.

### Function Contract

Let $N$ be the number of nodes in the tree.

**Inputs**

- `root`: the non-null root of a binary tree containing $1 \le N \le 100$ nodes.
- Every node value is between 1 and 1000; values do not affect completeness.

**Return value**

Return `true` if the tree is complete; otherwise return `false`.

### Examples

**Example 1**

- Input: `root = [1,2,3,4,5,6]`
- Output: `true`
- Explanation: Earlier levels are full, and nodes 4, 5, and 6 occupy the leftmost last-level positions.

**Example 2**

- Input: `root = [1,2,3,4,5,null,7]`
- Output: `false`
- Explanation: Node 7 occurs after an empty position on the last level.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Traverse real and missing positions in level order.** Initialize a queue with the root. Whenever a real node is removed, append both child references, including `None` for a missing child. This produces the conceptual array order of a binary heap without materializing entire empty levels.

**Remember the first gap.** When a `None` entry is removed, set a flag indicating that a missing position has appeared. Every later queue entry in a complete tree must also be `None`; encountering a real node after the flag is set proves that some available position to its left was skipped.

**Accept only a contiguous prefix of nodes.** If traversal finishes without such a later real node, all occupied level-order positions form a contiguous prefix. That condition means all earlier levels are full and the final level is filled from left to right, exactly matching completeness. Conversely, any incomplete placement has a first missing position followed by a real node, which the scan rejects.

#### Complexity detail

Each of the $N$ nodes is removed once and contributes two child references. Queue work is $O(N)$ time, and the queue may contain $O(N)$ entries at the widest level, using $O(N)$ space.

#### Alternatives and edge cases

- **Heap-index characterization:** Give the root index 1 and children indices `2 * index` and `2 * index + 1`; the tree is complete exactly when the maximum index equals $N$. This is also linear when the maximum is tracked incrementally.
- **Repeated index maximum:** Recomputing the maximum over all collected heap indices after every visited node remains correct but costs $O(N^2)$ time.
- **Level-width bookkeeping:** Verify full widths before the last level and left-packed children within the last. This works but requires more boundary cases than the gap flag.
- **Single node:** A root with no children is complete.
- **Right child without left child:** The right child appears after a missing left position and must be rejected.
- **Gap above the last occupied level:** Any descendants after that gap likewise make the tree incomplete.

</details>
