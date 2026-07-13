# Binary Tree Level Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 102 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, return the level order traversal of its node values. The root forms the first level, its existing children form the second, and this grouping continues until every reachable node has been included.

Return a list containing one list per level, ordered from the root downward. Within each level, values must retain their natural left-to-right tree order, including across different parents. Missing children contribute no placeholder values, and an empty tree produces an empty outer list rather than a level containing `null`.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

A list of value lists, one left-to-right list for each tree depth.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [9, 20], [15, 7]]`

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

**Queue order matches increasing depth and left-to-right position**

Place the root in a queue. Breadth-first removal processes earlier-enqueued parents before their descendants. Enqueuing each parent's left child before its right child, while processing parents left to right, preserves horizontal order across the entire next level.

**Snapshot the queue length before children are appended**

At the start of a level, record `level_size = len(queue)`. Remove exactly that many nodes into one output list. Children appended during those removals belong to the next depth and must not increase the number processed in the current iteration.

Without the size snapshot, a loop that continues until the queue is empty would consume newly added descendants and collapse all depths into one output list.

**Each outer iteration owns one complete depth**

Before each outer iteration, the queue contains exactly the nodes of the next unreported depth in left-to-right order. After processing its fixed size, the appended children establish the same invariant for the following depth.

**Trace child enqueue order across two parents**

For `[3, 9, 20, null, null, 15, 7]`, the queue first yields `[3]`, then `[9, 20]`. Processing that second level enqueues `15` and `7`, producing the final level `[15, 7]` without reversing any level.

**A frozen queue size is exactly one tree depth**

At the start of an outer iteration, the queue contains all nodes of the next depth in left-to-right order. Freezing its size prevents children appended during processing from entering the same output level.

Removing those nodes visits the complete depth, and enqueueing each left child before its right child constructs the next depth in horizontal order. Repeating makes every node appear once in its correct level and position.

#### Complexity detail

Every one of the `n` nodes is enqueued and dequeued once, giving $O(n)$ time. The queue holds at most one level plus part of the next, bounded by tree width `w`, so auxiliary space is $O(w)$ excluding the output.

#### Alternatives and edge cases

- **Depth-first traversal with a depth index:** is also $O(n)$ time and uses $O(h)$ call-stack space, while appending into per-depth lists.
- **Repeatedly scan for each depth:** can revisit nodes and degrade to $O(nh)$ time.
- **Zigzag traversal:** reverses alternating levels and solves a different problem.
- Empty input returns no levels. A one-node tree produces one level containing the root.
- Use a real deque or indexed queue; removing index zero from a dynamic array can introduce linear shifting per node.

</details>
