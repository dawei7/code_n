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
