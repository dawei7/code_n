# Binary Tree Longest Consecutive Sequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 549 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) |

## Problem Description
### Goal
Given a binary tree, choose a path of connected nodes without revisiting any node. The path may move from a child up through its parent and down into another child, but adjacent values along the complete path must change by exactly one in one consistent direction: strictly increasing or strictly decreasing.

Return the maximum number of nodes in such a consecutive path. The path may start and end anywhere and need not include the root. A turn through a parent can join one increasing branch with one decreasing branch when their values align, but a sequence that reverses numerical direction partway through its traversal is invalid.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- The length of the longest increasing or decreasing consecutive path

### Examples
**Example 1**

- Input tree: `[1, 2, 3]`
- Output: `2`

**Example 2**

- Input tree: `[2, 1, 3]`
- Output: `3`

**Example 3**

- Input tree: `[1]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Return two directional arms from every subtree**

For each node, compute an increasing arm that starts at the node and descends through values one larger at each step, and a decreasing arm that descends through values one smaller. Both lengths begin at one for the node itself.

**Use child states only when the edge continues the sequence**

After a child has returned its two lengths, a child value of `node.val + 1` can extend the node's increasing arm with the child's increasing arm. A child value of `node.val - 1` similarly extends the decreasing arm. Any other difference cannot contribute across that edge.

**Join opposite arms at their highest node**

A complete path may approach the current node along a decreasing downward arm read in reverse and leave along an increasing downward arm. Its length is `decreasing + increasing - 1`, subtracting the shared current node. Taking this candidate at every node covers paths contained in either one subtree and paths that cross between children.

**Evaluate children before their parent**

An explicit postorder stack stores traversal phase plus the returned pair from each child. This supplies both arms before the parent is finalized while avoiding recursion-depth failure on a long chain.

**Why every valid path is measured**

Every valid path has a unique highest node in the rooted tree. From that node, each used side must move consistently by `+1` or `-1`; if two sides are used, they are opposite directional arms of one globally consecutive sequence. The postorder state records the longest possible arm of each type, so their combination at that highest node is at least as long as the path. Every combined pair also describes an actual simple consecutive path, making the maximum exact.

#### Complexity detail

Every node is pushed, finalized, and combined with at most two child results once, giving $O(n)$ time. The explicit stack contains one frame per level and therefore uses $O(h)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive postorder:** uses the same two-arm recurrence in $O(n)$ time and $O(h)$ call-stack space, but a skewed tree can exceed recursion limits.
- **Recompute both arms from every node:** is correct but revisits descendants and takes $O(n^2)$ time on a consecutive chain.
- **Parent-to-child-only tracking:** misses paths that turn at a parent and continue into the other subtree.
- **Single node:** forms a consecutive path of length one.
- **Equal adjacent values:** do not extend either arm because the difference must be exactly one.
- **One-sided chain:** one arm may contain the whole answer while the other remains length one.
- **Turn at a node:** the two arms can come from different children, but two increasing or two decreasing arms cannot be joined into one monotone sequence.

</details>
