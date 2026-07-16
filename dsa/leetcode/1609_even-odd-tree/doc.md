# Even Odd Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1609 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/even-odd-tree/) |

## Problem Description
### Goal
A binary tree's root is on level 0, its children are on level 1, and each later generation increases the level index by one. The tree is Even-Odd only when every level obeys rules determined by that index's parity.

On each even-indexed level, every node value must be odd and the values must be strictly increasing from left to right. On each odd-indexed level, every value must be even and the values must be strictly decreasing from left to right. Return whether the entire tree satisfies both the parity and ordering requirements at every level.

### Function Contract
**Inputs**

- `root`: the non-null root of a binary tree containing between 1 and $10^5$ nodes.
- Every node value is an integer from 1 through $10^6$.

**Return value**

Return `true` if all even-indexed and odd-indexed levels satisfy their respective value parity and strict left-to-right order; otherwise return `false`.

### Examples
**Example 1**

- Input: `root = [1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2]`
- Output: `true`
- Explanation: Levels `[1]` and `[3, 7, 9]` are odd and increasing, while `[10, 4]` and `[12, 8, 6, 2]` are even and decreasing.

**Example 2**

- Input: `root = [5, 4, 2, 3, 3, 7]`
- Output: `false`
- Explanation: The duplicate 3 values on level 2 violate strict increase.

**Example 3**

- Input: `root = [5, 9, 1, 3, 5, 7]`
- Output: `false`
- Explanation: Level 1 contains odd values, but an odd-indexed level requires even values.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

Let $n$ be the number of nodes and $w$ the maximum number of nodes on one level.

**Process one complete level at a time.** Breadth-first search keeps the current frontier in a queue. At the start of each iteration, its length is exactly the number of nodes on the next level to validate. Remove precisely that many nodes before changing the level parity, appending their children for the following iteration.

**Combine parity and strict-order checks.** On an even-indexed level, initialize the previous value below every legal node value and require each new value to be odd and greater than its predecessor. On an odd-indexed level, initialize above every legal value and require each new value to be even and smaller. Reject immediately when either condition fails.

The queue yields nodes in left-to-right order, so every adjacent comparison is made in the contract's order. Strict increase or decrease is transitive; validating each adjacent pair proves the full level order. Checking every node's parity proves the other level condition. If all queue frontiers pass, every node belongs to a validated level and the tree is Even-Odd.

#### Complexity detail

Each node enters and leaves the queue once and undergoes constant work, giving $O(n)$ time. The queue stores at most one level plus children being accumulated for the next level, bounded by $O(w)$ space.

#### Alternatives and edge cases

- **Depth-first traversal with per-level state:** Recording the previous value for each depth while visiting left before right is also $O(n)$ and correct, but breadth-first search mirrors the level rules more directly.
- **Collect and sort every level:** Sorting can check whether values can be ordered, but the contract concerns their existing left-to-right order; sorting destroys that evidence and adds unnecessary work.
- **Compare every pair on a level:** This correctly proves strict ordering but takes $O(w^2)$ work on a wide level when adjacent comparisons suffice.
- A single node is valid exactly when its value is odd, because the root is on even-indexed level 0.
- Equal adjacent values violate strict ordering even when their parity is correct.
- Correct ordering does not compensate for incorrect parity, and correct parity does not compensate for reversed ordering.
- Sparse levels retain the natural left-to-right order induced by their parents and child positions; missing children are not values to compare.

</details>
