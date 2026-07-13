# Average of Levels in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 637 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, compute the average value of the nodes on each level. The root forms the first level, its existing children form the next level, and so on from top to bottom.

Return an array of floating-point averages in level order. For each depth, sum only the values of nodes actually present at that level and divide by that level's node count; missing children are not zero-valued nodes. Answers within $10^{-5}$ of the exact average are accepted.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, represented by a level-order list with null markers in app cases

**Return value**

- A list of floating-point averages, one for each tree level in top-to-bottom order

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[3.0,14.5,11.0]`

**Example 2**

- Input: `root = [1]`
- Output: `[1.0]`

**Example 3**

- Input: `root = [1,2,3,4,5,6,7]`
- Output: `[1.0,2.5,5.5]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(W)$

<details>
<summary>Approach</summary>

#### General

**Use the queue boundary as a level boundary**

Begin a breadth-first traversal with the root in a queue. At the start of each iteration, the queue contains exactly the nodes of the next unprocessed level, so its current length fixes how many nodes belong to that average.

**Accumulate before enqueuing descendants**

Remove exactly that many nodes, add their values to a level sum, and enqueue each non-null child. Children enter behind all remaining nodes of the current level and therefore form the complete queue for the following iteration.

**Divide by the captured level size**

After processing the fixed batch, divide its sum by the saved node count and append the result. Capturing the count before adding children prevents nodes from adjacent depths from entering the same average.

**Why every average contains exactly one depth**

The queue initially contains only depth zero. If an iteration starts with precisely depth `d`, removing its fixed batch visits every node at that depth once, and enqueuing their children produces precisely depth $d + 1$. Induction preserves the level boundary until the queue empties, so every reported sum and count belongs to exactly one depth.

#### Complexity detail

Every one of the `N` nodes is enqueued and dequeued once, giving $O(N)$ time. The queue holds at most the maximum level width `W`, so auxiliary space is $O(W)$; the returned list contains one value per tree level.

#### Alternatives and edge cases

- **Depth-first sum and count arrays:** accumulate two values per depth during one traversal; it also takes $O(N)$ time but uses recursion or an explicit depth stack.
- **Collect every level's values first:** simplifies the final averaging step but stores all `N` values instead of only the active frontier.
- **Search separately for each depth:** repeatedly traverse from the root to collect one level; it is correct but can take $O(NH)$ time for height `H`.
- A single-node tree returns that node's value as its only average.
- Sparse levels divide by their actual node count, not the width of a complete-tree layout.
- Negative values and fractional averages require ordinary signed floating-point division.
- Large level sums should be accumulated in a sufficiently wide numeric type before division.

</details>
