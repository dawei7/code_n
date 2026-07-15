# Distribute Coins in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 979 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/distribute-coins-in-binary-tree/) |

## Problem Description

### Goal

A binary tree has $N$ nodes, and each node's value states how many coins it currently holds. Across the whole tree there are exactly $N$ coins.

In one move, choose two adjacent nodes and transfer one coin across their connecting edge. The transfer may go from a parent to its child or from a child to its parent. Find the minimum number of moves needed to leave every node with exactly one coin. A coin crossing two edges counts as two moves, even if both transfers are part of the same route.

### Function Contract

**Inputs**

- `root`: the root of a non-empty binary tree containing $N$ nodes, where $1 \le N \le 100$.
- Every node value is between $0$ and $N$, and the sum of all node values is $N$.

Let $H$ denote the tree height. For a subtree rooted at node $u$, define its coin balance as

$$
B_u = \bigl(\text{coins in the subtree of }u\bigr)-\bigl(\text{nodes in that subtree}\bigr).
$$

**Return value**

- The minimum number of single-coin, single-edge moves required to give every node exactly one coin.

### Examples

**Example 1**

- Input: `root = [3, 0, 0]`
- Output: `2`
- Explanation: the root sends one coin to each child.

**Example 2**

- Input: `root = [0, 3, 0]`
- Output: `3`
- Explanation: the left child sends two coins to the root, after which the root sends one coin to the right child.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Measure what each subtree must exchange:** After every node inside a subtree has received its required one coin, a positive balance $B_u$ is the number of surplus coins that must leave through the edge to its parent. A negative balance is the number of coins that must enter through that edge. No other edge connects the subtree to the rest of the tree.

**Accumulate forced edge traffic in postorder:** Recursively compute the balances of the left and right children before their parent. A node keeps one of its own and received coins, so its balance is `node.val + left_balance + right_balance - 1`. Exactly `abs(left_balance)` coins must cross the left edge and `abs(right_balance)` must cross the right edge; add both quantities to the move count.

**Why this is minimal:** Every feasible final distribution must move at least $\lvert B_u\rvert$ coins across the unique parent edge of each non-root subtree, because that edge is its only connection to outside coins. The postorder flow realizes exactly that forced amount on every edge. Summing these independent lower bounds therefore gives an attainable minimum. The root's final balance is zero because the entire tree contains exactly as many coins as nodes.

#### Complexity detail

Each of the $N$ nodes is visited once, so time is $O(N)$. The recursive call stack contains at most one root-to-leaf path and uses $O(H)$ space; no collection proportional to all nodes is required.

#### Alternatives and edge cases

- **Recount every subtree:** Computing each edge balance by traversing its entire child subtree is correct but takes $O(N^2)$ time on a skewed tree.
- **Simulate individual coin routes:** Greedily moving named coins obscures the forced net flow and can repeat work; subtree balances aggregate all equivalent transfers.
- **Single node:** Its value must be one under the total-coin guarantee, so no move is required.
- **Coins concentrated at a leaf:** The surplus travels upward across several edges, and each crossing contributes separately.
- **Zero-coin subtree:** Its negative balance correctly counts every coin that must enter from its parent side.

</details>
