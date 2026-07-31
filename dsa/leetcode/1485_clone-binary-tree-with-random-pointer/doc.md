# Clone Binary Tree With Random Pointer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1485 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) |

## Problem Description
### Goal

A binary tree node contains a value, ordinary `left` and `right` child pointers, and an additional `random` pointer. A random pointer may refer to any node in the same tree—including the node itself—or may be null. Random edges can cross subtrees or form cycles even though the child edges form a tree.

Return a deep copy whose nodes are all newly allocated. Every copied node must preserve its original node's value and child structure, while each copied random pointer must target the copy of the corresponding original target. No pointer in the returned structure may refer back to an original node.

### Function Contract
**Inputs**

Let $N$ be the number of non-null nodes.

- `root`: The root of a random-pointer binary tree of `Node` objects, or `null`.
- Each `Node` has `val`, `left`, `right`, and `random` fields.
- The tree contains $0 \le N \le 1000$ nodes.
- Every node value satisfies $1 \le \texttt{val} \le 10^6$.
- A `random` field is either null or refers to one of the $N$ tree nodes.

JSON cases encode `root` in level order. Each non-null position is `[value, random_index]`; null positions preserve missing child slots, and `random_index` identifies a position in that same level-order array. The runner reconstructs the object graph before calling `solve(root)`.

**Return value**

Return the root of a newly allocated `NodeCopy` graph with the same values and `left`, `right`, and `random` relationships as the original. Return null for an empty input tree. The runner verifies both the serialized relationships and that the result shares no node identity with the input graph.

### Examples
**Example 1**

- Input: `root = [[1,null],null,[4,3],[7,0]]`
- Output: `[[1,null],null,[4,3],[7,0]]`
- Explanation: The node with value `4` points randomly to the node at position three, while the node with value `7` points back to the root at position zero.

**Example 2**

- Input: `root = [[1,4],null,[1,0],null,[1,5],[1,5]]`
- Output: `[[1,4],null,[1,0],null,[1,5],[1,5]]`
- Explanation: Equal values do not identify nodes. Random targets are positional identities, and a node may point to itself.

**Example 3**

- Input: `nodes = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]`
- Output: `[[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]`
- Explanation: Random edges pair positions from opposite ends, including edges between different subtrees.
