# Binary Tree Cameras

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 968 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [binary-tree-cameras](https://leetcode.com/problems/binary-tree-cameras/) |

## Problem Description

### Goal

You may install cameras on nodes of a binary tree. A camera monitors the node holding it, that node's parent, and its immediate left and right children. It does not monitor more distant ancestors or descendants.

Choose camera locations so that every node in the tree is monitored, then return the minimum possible number of cameras. Node values carry no information for placement; every node value is `0`, and only the tree structure determines the answer.

### Function Contract

**Inputs**

- `root`: the root of a binary tree with $N$ nodes and height $H$.
- The tree contains between $1$ and $1000$ nodes, inclusive.
- Every node has value `0`.
- Serialized cases use level order, with `null` for a missing child.

**Return value**

Return the minimum number of cameras needed to monitor all $N$ nodes.

### Examples

**Example 1**

- Input: `root = [0,0,null,0,0]`
- Output: `1`

**Example 2**

- Input: `root = [0,0,null,0,null,0,null,null,0]`
- Output: `2`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Let children determine their parent's state.** Process the tree in postorder and assign each node one of three states: `uncovered`, `camera`, or `covered`. A missing child is `covered`; it needs no camera and should not force one at its parent.

**Place a camera only when a child needs it.** If either child is `uncovered`, the current node is the lowest location that can monitor that child while also covering itself and its parent. Install a camera here and return `camera`. Delaying the camera upward would leave the child too far away, while placing it lower offers no additional benefit over the current node.

**Propagate coverage upward.** If no child is uncovered but at least one child has a camera, the current node is `covered`. If both children are merely covered, the current node remains `uncovered`; its parent can optimally cover it. After postorder finishes, add one final camera if the root is still uncovered because it has no parent to handle it.

**Why the greedy choice is minimal.** Every uncovered child requires a camera at itself or its parent. Choosing the parent covers at least everything a camera on that child would cover toward the unprocessed part of the tree, so the replacement never uses more cameras. Postorder makes this forced choice only after both subtrees are already optimally resolved, yielding a global minimum.

#### Complexity detail

An explicit postorder stack visits each node a constant number of times, giving $O(N)$ time. The stack and stored state for each node use $O(N)$ auxiliary space; a recursive implementation instead uses $O(H)$ call-stack space.

#### Alternatives and edge cases

- **Three-cost tree dynamic programming:** For each node, compute minimum costs when it has a camera, is covered without one, or expects coverage from its parent. This is also linear but requires more careful impossible-state handling.
- **Enumerate camera subsets:** Try every subset of nodes and test coverage. This is exact but exponential in $N$.
- **Repeated subtree accounting:** Recount a node's entire subtree while performing the same postorder decisions. It stays correct but takes $O(N^2)$ time on a chain.
- **Single node:** The root needs one camera because it has neither a parent nor a child camera.
- **Leaf children:** One camera on their parent monitors both leaves and the parent.
- **Uncovered root:** The final root check is essential; no later ancestor can cover it.

</details>
