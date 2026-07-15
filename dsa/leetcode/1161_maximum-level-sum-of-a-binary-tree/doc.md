# Maximum Level Sum of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) |

## Problem Description

### Goal

You are given the root of a nonempty binary tree. The root is at level $1$, its children are at level $2$, and each subsequent child level increases the level number by one.

For every level, sum the values of all nodes on that level. Return the smallest level number $x$ whose sum is maximal among all tree levels. Node values may be negative, so the winning sum is not necessarily positive and the comparison must include every level.

### Function Contract

**Inputs**

- `root`: The root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$ and every node value lies between $-10^5$ and $10^5$.
- Let $w$ be the maximum number of nodes present on any one level of the tree.

**Return value**

- The smallest 1-indexed level whose node-value sum equals the maximum level sum.

### Examples

**Example 1**

- Input: `root = [1,7,0,7,-8,null,null]`
- Output: `2`

The first three level sums are $1$, $7$, and $-1$.

**Example 2**

- Input: `root = [989,null,10250,98693,-89388,null,null,null,-32127]`
- Output: `2`

**Example 3**

- Input: `root = [1]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Keep one complete level in the queue.** Initialize a breadth-first queue with `root`. At the start of each iteration, `len(queue)` is exactly the number of nodes on the current level. Remove that many nodes, add their values to `level_sum`, and enqueue each non-null child for the next iteration.

**Retain the earliest maximum.** Initialize `best_sum` below every possible level sum and record levels starting at $1$. After a level is fully summed, replace the answer only when `level_sum > best_sum`. A later equal sum does not update it, so the first—and therefore smallest—level among all maxima remains selected.

Breadth-first traversal visits levels in increasing order and assigns every node to exactly one level sum. Consequently, each computed sum is complete, every possible level is compared, and the strict update rule implements the required tie break. Negative-only trees are handled naturally because the initial best is negative infinity rather than zero.

#### Complexity detail

Every one of the $n$ nodes is enqueued once, dequeued once, and contributes to one addition, giving $O(n)$ time. The queue contains nodes from at most the current and emerging next level, bounded by the tree's maximum width $w$, so auxiliary space is $O(w)$.

#### Alternatives and edge cases

- **Depth-first accumulation:** Recording one running sum per depth is also $O(n)$ time, but it uses $O(h)$ recursion or stack space plus the level-sum array, where $h$ is the tree height.
- **Revisit the tree for every depth:** Computing each level separately is correct but can take $O(n^2)$ on a skewed tree.
- **Initialize the maximum to zero:** This fails when all level sums are negative.
- **Equal maximum sums:** Update only for a strictly larger sum so the smaller level number wins.
- **Single-node tree:** The root is the only level and the answer is $1$ regardless of its value.
- **Sparse levels:** Missing children contribute nothing; only existing nodes are enqueued and summed.

</details>
