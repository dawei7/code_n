# Find Leaves of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 366 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-leaves-of-binary-tree/) |

## Problem Description
### Goal
Given a binary tree, repeatedly collect all current leaves and remove them simultaneously. A leaf in a given round is a node with no remaining children at the start of that round; removing lower nodes can cause their parents to become leaves later.

Return one list of node values per removal round, from the original leaves through the final root. Values within a round may appear in any order, but every node must occur exactly once in the round when it becomes a leaf. An empty tree returns an empty outer list, while a one-node tree produces one round containing its root value.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, represented as level-order values in app cases and as `TreeNode` objects during execution

**Return value**

- A list of removal rounds from first to last. Values within one round may appear in any order.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5]`
- Output: `[[4,5,3],[2],[1]]`

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Replace repeated removal with height from the leaves**

A leaf disappears in round zero. A non-leaf can disappear only after both child subtrees are gone, so its round is one more than the later of its children's rounds. Define a missing child to have height `-1`; then every leaf receives $1 + \max(-1,-1) = 0$.

Compute this height with a postorder traversal. Once both child heights are known, calculate the current node's round and append its value to the result bucket at that index, creating a new bucket when this is the first node at that height.

**Why height matches simultaneous removal time**

After round zero removes all original leaves, each surviving node has effectively lost one layer beneath it. Inductively, a node with leaf-height `r` has at least one child subtree lasting through round $r - 1$, so it cannot be removed earlier; both child subtrees are gone after that round, so it is a leaf and is removed in round `r`. Thus grouping equal heights produces exactly the simultaneous removal rounds without mutating the tree.

**Trace the standard tree**

In `[1,2,3,4,5]`, nodes `4`, `5`, and `3` have height zero. Node `2` has height one because its children are leaves, and root `1` has height two. The buckets are therefore `[[4,5,3],[2],[1]]`.

#### Complexity detail

Each of the `n` nodes is visited once and performs constant work, so time is $O(n)$. The recursion stack uses $O(h)$ space for tree height `h`. Result buckets contain all `n` values and are required output space.

#### Alternatives and edge cases

- **Physically remove leaves round by round:** mirrors the statement but rescans surviving nodes and can take $O(n^2)$ on a chain.
- **Parent pointers plus remaining-child counts:** can process leaves as a topological queue in $O(n)$, but needs $O(n)$ auxiliary maps.
- **Breadth-first traversal by root depth:** groups distance from the root, which is not the same as removal time in an unbalanced tree.
- Values within one removal round are unordered, but the sequence of rounds is significant.
- An empty tree returns no rounds.
- Duplicate node values remain separate output entries.
- A one-sided chain produces one node per round, starting at the deepest node.

</details>
