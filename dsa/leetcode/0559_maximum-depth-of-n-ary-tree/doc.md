# Maximum Depth of N-ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 559 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) |

## Problem Description
### Goal
Given the root of an N-ary tree, the depth of a node is the number of nodes on the path from the root to that node, including both endpoints. The root therefore has depth one, and every child level increases depth by one.

Return the maximum depth over all nodes, equivalently the number of nodes on the longest root-to-leaf path. An empty tree has depth zero, and a one-node tree has depth one. Children may be absent or numerous at different nodes; the function returns only the depth, not the deepest leaf or path.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- The tree's maximum depth as an integer

### Examples
**Example 1**

- Input tree: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `3`

**Example 2**

- Input tree: `[7, []]`
- Output: `1`

**Example 3**

- Input tree: `null`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Carry each node's depth with the traversal**

If the root exists, place it on a stack with depth one. Whenever a node is removed, compare its depth with the maximum seen so far.

**Advance one child at a time**

Each stack frame stores the next child index to visit. Push that child with `depth + 1`, finish its subtree, and then resume the parent frame. N-ary branching changes how many children are visited, but not the depth recurrence.

**Finish after every reachable node is visited**

A leaf schedules no further work. Once the stack is empty, every root-to-node path has contributed its endpoint depth, so the greatest recorded value is the maximum root-to-leaf depth.

**Why the maximum recorded depth is exact**

The root begins with its correct depth. If a popped node has the correct depth, each child receives exactly one more, so induction gives the correct depth to every node. Every deepest path ends at a node visited by the traversal, and no recorded depth can exceed its actual root path length. The maximum is therefore precisely the tree height.

#### Complexity detail

Each of the `n` nodes is pushed and popped once, giving $O(n)$ time. Because a frame schedules only one child at a time, the stack contains one frame per active ancestor and uses $O(h)$ space.

#### Alternatives and edge cases

- **Recursive depth-first search:** directly returns one plus the maximum child depth in $O(n)$ time, but a long chain can exceed recursion limits.
- **Breadth-first search:** counts complete levels in $O(n)$ time and uses space proportional to the widest level.
- **Recompute subtree height from every node:** is correct but revisits descendants and takes $O(n^2)$ time on a chain.
- **Empty tree:** has depth zero.
- **Single node:** is both root and leaf, so its depth is one.
- **Wide root:** all leaf children still give depth two regardless of their count.
- **Uneven branches:** only the longest root-to-leaf path determines the answer.

</details>
