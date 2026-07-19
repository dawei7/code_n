# Binary Tree Coloring Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1145 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-tree-coloring-game/) |

## Problem Description

### Goal

Two players play a turn-based game on a binary tree containing an odd number `n` of nodes. Every node has a distinct value from `1` through `n`. The first player names `x`, the second player names a different value `y`, and the corresponding nodes are colored red and blue, respectively.

Starting with the first player, each turn colors one uncolored neighbor of a node already bearing that player's color. A neighbor may be the node's left child, right child, or parent. A player must pass exactly when no such move is available. The game ends after both players pass, and whoever colored more nodes wins. Acting as the second player, return whether some initial choice of `y` guarantees a win after the first player has selected `x`.

### Function Contract

**Inputs**

- `root`: the root of a binary tree with exactly $n$ nodes, represented in cOde(n) cases by a level-order list.
- `n`: the odd number of nodes, where $1 \le n \le 100$.
- `x`: the first player's chosen node value, where $1 \le x \le n$.
- Every node value lies from $1$ through $n$, and all node values are unique.
- Let $h$ denote the height of the tree.

**Return value**

`true` if the second player can choose a distinct value `y` that guarantees coloring more nodes; otherwise `false`.

### Examples

**Example 1**

- Input: `root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3`
- Output: `true`
- Explanation: Choosing the node with value `2` lets the second player secure a winning number of nodes.

**Example 2**

- Input: `root = [1,2,3], n = 3, x = 1`
- Output: `false`
