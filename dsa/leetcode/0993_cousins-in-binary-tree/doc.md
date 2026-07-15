# Cousins in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 993 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/cousins-in-binary-tree/) |

## Problem Description

### Goal

You are given the root of a binary tree whose node values are unique, together with the values `x` and `y` of two different nodes that both occur in the tree. Two nodes are cousins when they have the same depth but different parents.

The root has depth $0$, and every child of a node at depth $d$ has depth $d+1$. Return `true` when the nodes identified by `x` and `y` satisfy both cousin conditions, and return `false` otherwise.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes, where $2\le N\le100$; every node value is unique and lies from $1$ through $100$.
- `x` and `y`: different values of nodes present in the tree.

**Return value**

- `true` if the two selected nodes have the same depth and different parents; otherwise, `false`.

### Examples

**Example 1**

- Input: `root = [1, 2, 3, 4], x = 4, y = 3`
- Output: `false`
- Explanation: Node $4$ is deeper than node $3$.

**Example 2**

- Input: `root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4`
- Output: `true`
- Explanation: The selected nodes share a depth and have different parents.

**Example 3**

- Input: `root = [1, 2, 3, null, 4], x = 2, y = 3`
- Output: `false`
- Explanation: Nodes $2$ and $3$ are siblings, so their parent is the same.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Carry each node's parent through a level traversal:** Begin a breadth-first traversal with the root paired with no parent. All entries processed in one outer iteration have the same depth. For that level, record the parent whenever a node's value equals `x` or `y`, and enqueue every child together with its current node.

**Decide as soon as a relevant level ends:** If both values were found in the same level, they are cousins exactly when their recorded parent objects differ. If only one was found, the other node must occur at another depth, so the answer is immediately `false`. If neither appears, continue to the next level.

Because both selected values are guaranteed to exist and node values are unique, encountering both nodes at one level with distinct parents is sufficient and no later tree structure can change the result.

#### Complexity detail

Each of the $N$ nodes enters and leaves the queue at most once, giving $O(N)$ time. The widest tree level can contain $O(N)$ nodes, so the queue uses $O(N)$ space.

#### Alternatives and edge cases

- **Depth-first search with parent and depth records:** One traversal can locate both nodes and compare the same two attributes; recursion may use $O(N)$ call-stack space in a skewed tree.
- **Materialize every root-to-node path:** Comparing paths reveals depth and parent information, but repeatedly copying long paths can take $O(N^2)$ time on deep trees.
- **Siblings:** Nodes at the same depth are not cousins when their parent is identical.
- **Different depths:** Different parents alone are insufficient; both nodes must also share a depth.
- **Root selected:** The root cannot be a cousin of another node because no other node has depth $0$.

</details>
