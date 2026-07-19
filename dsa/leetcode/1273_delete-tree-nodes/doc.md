# Delete Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1273 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-tree-nodes/) |

## Problem Description

### Goal

A valid tree with `nodes` vertices is rooted at node $0$. Array `parent` describes its edges: `parent[i]` is the parent of node $i$, while `parent[0] = -1`. Array `value` assigns an integer value to each corresponding node.

Delete every subtree whose node values sum to zero. Deleting a subtree removes its root and every descendant, so none of those nodes can remain independently. After all zero-sum subtrees have been removed, return the number of nodes still present in the rooted tree.

### Function Contract

**Inputs**

- `nodes`: the node count $n$, where $1 \le n \le 10^4$.
- `parent`: a length-$n$ parent array defining a valid tree rooted at $0$, with `parent[0] = -1`.
- `value`: a length-$n$ array with $-10^5 \le \texttt{value[i]} \le 10^5$.

**Return value**

- Return the number of nodes remaining after every zero-sum subtree is deleted.

### Examples

**Example 1**

- Input: `nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]`
- Output: `2`

**Example 2**

- Input: `nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]`
- Output: `6`

**Example 3**

- Input: `nodes = 1, parent = [-1], value = [0]`
- Output: `0`
