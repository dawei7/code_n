# Count Nodes Equal to Average of Subtree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2265 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) |

## Problem Description

### Goal

Given the root of a binary tree, examine every node together with all of its
descendants. Those nodes form that node's subtree, including the node itself.

For a subtree containing $k$ nodes with total value $S$, its average is
$\left\lfloor S/k\right\rfloor$: divide the sum by the number of nodes and
round the result down to the nearest integer. Count how many nodes have a value
equal to the average of their own subtree.

### Function Contract

**Inputs**

- `root`: The root of a nonempty binary tree containing $n$ nodes.

The tree contains $1\le n\le1000$ nodes, and every node value is an integer in
the range $0\le\texttt{Node.val}\le1000$.

**Return value**

Return the number of nodes whose value equals the floor of the sum of all
values in their subtree divided by the number of nodes in that subtree.

### Examples

**Example 1**

- Input: `root = [4,8,5,0,1,null,6]`
- Output: `5`

The root's subtree has sum $24$ and six nodes, so its average is $4$. The
nodes with values `5`, `0`, `1`, and `6` also match their respective subtree
averages.

**Example 2**

- Input: `root = [1]`
- Output: `1`

The only node is also the only member of its subtree.
