# Two Sum BSTs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1214 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, Binary Search, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-bsts/) |

## Problem Description

### Goal

You are given the roots `root1` and `root2` of two binary search trees, together with an integer `target`. A valid choice must take one node from the first tree and one node from the second tree; two nodes from the same tree do not form a candidate.

Return `true` if and only if some cross-tree pair has values whose sum equals `target`. Return `false` when no such pair exists. Node values and the target may be negative, zero, or positive.

### Function Contract

**Inputs**

- `root1`: The root of the first nonempty binary search tree, which contains $n$ nodes.
- `root2`: The root of the second nonempty binary search tree, which contains $m$ nodes.
- `target`: The required sum.

The bounds are $1\le n,m\le5000$. Every node value and `target` lies between $-10^9$ and $10^9$, inclusive.

**Return value**

- `true` when one node from each tree sums to `target`; otherwise `false`.

### Examples

**Example 1**

- Input: `root1 = [2,1,4]`, `root2 = [1,0,3]`, `target = 5`
- Output: `true`

The first tree's `2` and the second tree's `3` form a valid pair.

**Example 2**

- Input: `root1 = [0,-10,10]`, `root2 = [5,1,7,0,2]`, `target = 18`
- Output: `false`

**Example 3**

- Input: `root1 = [8,3,10]`, `root2 = [6,1,9]`, `target = 12`
- Output: `true`

### Required Complexity

- **Time:** $O(n+m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Materialize one side as complements can query it.** Traverse the first tree and insert every node value into a hash set. The traversal may be iterative, avoiding recursion-depth concerns for a skewed tree.

**Probe with every node from the other tree.** Traverse the second tree. For a node value `x`, compute `target - x` and test whether that complement is in the first tree's set. If so, the set value comes from `root1` and `x` comes from `root2`, so the required cross-tree pair exists.

**Why exhausting the second tree proves failure.** Every possible pair contains exactly one second-tree node. When that node is visited, the hash lookup tests the only first-tree value that could complete its sum. If all $m$ probes fail, no pair among the $nm$ possibilities can equal `target`.

The binary-search-tree ordering is not needed for this hash formulation, but the method remains linear and handles positive and negative values uniformly.

#### Complexity detail

The first traversal visits $n$ nodes and the second visits at most $m$, with expected $O(1)$ hash insertion and lookup, giving $O(n+m)$ expected time. The value set stores $O(n)$ entries, and iterative traversal stacks can hold $O(n+m)$ nodes in the broad stated bound.

#### Alternatives and edge cases

- **Two inorder arrays and two pointers:** Sorted traversals followed by opposite-direction pointers also take $O(n+m)$ time and $O(n+m)$ space.
- **Two lazy BST iterators:** An ascending iterator for the first tree and descending iterator for the second achieves $O(n+m)$ time with $O(h_1+h_2)$ space.
- **Compare every cross-tree pair:** This is correct but takes $O(nm)$ time.
- **Binary-search the second tree per first node:** It uses BST order but takes $O(nh_2)$ time, which becomes quadratic for a skewed tree.
- **Single-node trees:** Their two values are a valid pair because the nodes belong to different trees.
- **Equal values across trees:** They may be paired; cross-tree identity, not value distinctness, is required.
- **Negative target:** Complement arithmetic works without a special case.
- **Skewed trees:** Iterative traversal avoids call-stack overflow.

</details>
