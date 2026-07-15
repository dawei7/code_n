# Sum of Root To Leaf Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1022 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) |

## Problem Description

### Goal

You are given the root of a binary tree in which every node value is `0` or `1`. Each root-to-leaf path spells a binary number from its most-significant bit at the root to its least-significant bit at the leaf.

Interpret every such path as a base-2 integer and return their sum over all leaves. Leading zeroes are allowed on a path and do not change its numeric value. The test data guarantees that the final sum fits in a 32-bit integer.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree with $N$ nodes, where $1\le N\le1000$ and every `Node.val` is `0` or `1`.

Let $H$ denote the tree height, measured as the maximum number of nodes on a root-to-leaf path.

**Return value**

- The sum of the binary integers represented by all root-to-leaf paths.

### Examples

**Example 1**

- Input: `root = [1, 0, 1, 0, 1, 0, 1]`
- Output: `22`
- Explanation: The paths represent `100`, `101`, `110`, and `111`, whose values sum to `22`.

**Example 2**

- Input: `root = [0]`
- Output: `0`

**Example 3**

- Input: `root = [1, 1]`
- Output: `3`
- Explanation: The only path represents binary `11`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Carry the prefix value down the tree:** At a node, append its bit to the binary prefix with `current = current * 2 + node.val`. Pass that value to both children rather than storing the path as characters.

**Contribute only at leaves:** If a node has neither child, the current prefix is one complete root-to-leaf number, so return it. Otherwise recursively sum the contributions of the existing left and right subtrees.

**Why prefixes can be shared:** Both child paths have exactly the same bits through their parent. Computing that prefix once and extending it independently avoids rebuilding common path segments for each leaf.

By induction on path length, `current` at every node equals the binary value from the root through that node. Each leaf is visited exactly once and contributes its represented number, so the accumulated total is precisely the requested sum.

#### Complexity detail

The traversal visits each of the $N$ nodes once and performs constant work per node, giving $O(N)$ time. Recursion follows one root-to-leaf path at a time and uses $O(H)$ call-stack space.

#### Alternatives and edge cases

- **Find every leaf path independently:** Searching again from the root for each leaf repeats shared traversal work and can take $O(N^2)$ time.
- **Iterative stack:** Storing `(node, prefix)` pairs avoids recursion while retaining $O(N)$ time and $O(H)$ space on a depth-first traversal.
- **Single node:** Its bit is the only path value.
- **Leading zero:** It contributes no extra value but remains part of the path structure.
- **Missing child:** Continue only through existing nodes; a node is a leaf only when both children are absent.

</details>
