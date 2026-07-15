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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Cut the tree at the red starting node.** Removing the node whose value is `x` separates every other node into at most three connected regions: the left subtree of `x`, the right subtree of `x`, and everything reached through the parent edge. Let their sizes be $L$, $R$, and $P = n-L-R-1$.

**Recognize the second player's only winning shape.** If one region contains more than half the tree, the second player can start on the neighbor of `x` leading into that region. The red player can never cross the already-blue boundary, so blue can eventually color that entire region and has a strict majority. Conversely, if all three regions contain at most $\lfloor n/2 \rfloor$ nodes, any blue starting node lies in one of them. Red can occupy the boundary at `x`, preventing blue from reaching either of the other regions, so blue cannot obtain a majority. Thus a winning move exists exactly when $\max(L,R,P) > \lfloor n/2 \rfloor$.

**Count both child regions during one traversal.** A postorder depth-first search returns each subtree's size. When it reaches the node valued `x`, retain the sizes returned by its left and right children. The overall traversal still counts every node once, and the remaining parent-side count follows from $P = n-L-R-1$ without another search.

#### Complexity detail

The postorder traversal visits each of the $n$ nodes once, giving $O(n)$ time. Its recursion stack contains at most one root-to-leaf path and therefore uses $O(h)$ auxiliary space.

#### Alternatives and edge cases

- **Repeated membership searches:** Testing every node separately to discover which side of `x` contains it is correct but can revisit the same subtrees and take $O(n^2)$ time.
- **Simulate the alternating turns:** Explicit game simulation explores irrelevant move orders; the three-component cut captures every possible territorial outcome directly.
- **First player chooses the root:** The parent-side region has size zero, but either child subtree can still give the second player a majority.
- **First player chooses a leaf:** Both child regions are empty, so the parent-side region has $n-1$ nodes and is winning whenever another node exists.
- **Single-node tree:** There is no distinct value available for `y`, and no region exceeds half the tree, so the answer is `false`.
- **Strict majority:** Because the winner must color more nodes, a region of exactly $\lfloor n/2 \rfloor$ nodes is insufficient.

</details>
