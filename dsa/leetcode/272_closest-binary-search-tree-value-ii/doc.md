# Closest Binary Search Tree Value II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 272 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, Stack, Tree, Depth-First Search, Binary Search Tree, Heap (Priority Queue), Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) |

## Problem Description
### Goal
Given a nonempty binary search tree, a floating-point target, and a valid count `k`, select exactly `k` distinct tree nodes whose values have the smallest absolute differences from the target. The target need not occur in the tree or be an integer.

Return the selected node values in any order. Every tree node can contribute at most once, and values outside the selected set must not be closer than a retained value under the problem's guarantee. Use the tree's sorted structure to avoid treating it as an unrelated unsorted collection; the function returns values only, not distances or node references.

### Function Contract
**Inputs**

- `root`: the nonempty root of a binary search tree
- `target`: the value to approximate
- `k`: the number of values to return

**Return value**

The `k` closest tree values in any order.

### Examples
**Example 1**

- Input: `root = [4,2,5,1,3], target = 3.714286, k = 2`
- Output: `[3,4]`

**Example 2**

- Input: `root = [1], target = 0.0, k = 1`
- Output: `[1]`

**Example 3**

- Input: `root = [4,2,6,1,3,5,7], target = 4.5, k = 3`
- Output: `[3,4,5]`

### Required Complexity

- **Time:** $O(h + k)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Initialize lazy predecessor and successor iterators**

Follow BST search paths to initialize a predecessor stack containing values at most the target and a successor stack containing values greater than it. Each stack can advance to its next ordered value by exploring one subtree spine.

**Merge the two ordered sides by distance**

For each of `k` selections, compare the current predecessor and successor distances. Pop the nearer value, then advance only that iterator.

The stack tops are respectively the largest unchosen value at most the target and the smallest unchosen value above it. All other unchosen values on either side are no closer than that side's top.

**One of the two stack tops is always globally closest**

Within the predecessor side, values become no closer as they decrease away from the target; within the successor side, they become no closer as they increase. Each side's top is therefore its best remaining candidate, and the globally closest unchosen value must be one of those two. Selecting the nearer top and advancing only that iterator restores the same condition for the next choice.

#### Complexity detail

Initialization follows two root-to-leaf paths. Every selected node is pushed and popped through a bounded iterator traversal, giving $O(h + k)$ time and $O(h)$ stack space.

#### Alternatives and edge cases

- **Traverse and sort all nodes:** costs $O(n \log n)$ and ignores BST ordering.
- **Keep a size-`k` heap during full traversal:** costs $O(n \log k)$.
- One iterator may empty first; the remaining values then come from the other side.

</details>
