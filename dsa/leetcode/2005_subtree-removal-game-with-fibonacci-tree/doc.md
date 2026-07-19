# Subtree Removal Game with Fibonacci Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2005 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Tree, Binary Tree, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/) |

## Problem Description

### Goal

A Fibonacci tree is defined by its order. `order(0)` is empty, and `order(1)` contains one node. For $n\ge2$, `order(n)` has a new root whose left subtree is `order(n - 2)` and whose right subtree is `order(n - 1)`.

Alice and Bob play on `order(n)`, with Alice moving first. A move selects one node and removes that node together with all of its descendants. Eventually a player has no safe choice and is forced to delete the original root; that player loses. Assuming optimal play from both sides, determine whether Alice wins.

### Function Contract

**Inputs**

- `n`: the Fibonacci-tree order, where $1 \le n \le 100$.

**Return value**

Return `true` when the initial position is winning for Alice under optimal play, and `false` when Bob can force Alice to remove the root.

### Examples

**Example 1**

- Input: `n = 3`
- Output: `true`
- Explanation: Alice can remove one leaf so that after the remaining safe removals, Bob is the player forced to take the root.

**Example 2**

- Input: `n = 1`
- Output: `false`
- Explanation: The tree contains only the root, so Alice loses immediately.

**Example 3**

- Input: `n = 2`
- Output: `true`
- Explanation: Alice removes the only non-root node, leaving Bob with the losing root move.
