# Lowest Common Ancestor of a Binary Tree III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1650 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) |

## Problem Description
### Goal
Two distinct nodes `p` and `q` belong to the same binary tree. Every node contains a `parent` pointer in addition to its value and child pointers, so either starting node can be followed upward without receiving the root separately.

Return the lowest common ancestor of `p` and `q`: the deepest node that is an ancestor of both. A node counts as its own ancestor, so if one input node lies on the other's path to the root, return that input node.

### Function Contract
**Inputs**

- `p`: one node in a parent-linked binary tree.
- `q`: a different node in the same tree.

The tree contains between 2 and $10^5$ nodes, all node values are unique, and both inputs are guaranteed to exist. Let $h$ be the tree height.

**Return value**

Return the node object that is the lowest common ancestor of `p` and `q`.

### Examples
**Example 1**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1`
- Output: `3`

The two upward paths first share the root node with value 3.

**Example 2**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4`
- Output: `5`

Node 5 is an ancestor of node 4 and is also its own ancestor.

**Example 3**

- Input: `root = [1, 2], p = 1, q = 2`
- Output: `1`

### Required Complexity
- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View the parent paths as intersecting linked lists.** Starting at `p` and repeatedly following `parent` produces a singly linked path ending after the root. The same is true for `q`. From their lowest common ancestor upward, the two paths are the same sequence of node objects. The task is therefore equivalent to finding the first shared node of two linked lists with possibly different prefix lengths.

**Make both walkers cover both prefix lengths.** Move one pointer upward from `p` and the other from `q`. When the first pointer passes the root, redirect it to `q`; when the second passes the root, redirect it to `p`. Each pointer then traverses the two path lengths in opposite order. If the distances from `p` and `q` to their first shared ancestor differ, switching paths cancels that offset without explicitly computing either depth.

**Stop on object identity.** After both walkers have covered the same combined distance, they meet at the first node in the shared suffix, which is exactly the lowest common ancestor. Comparing node identity is essential: the contract asks for the shared node object, not merely an equal value. The same logic also handles the case where one input is already an ancestor of the other.

#### Complexity detail

Each pointer traverses at most the path from each input to the root once, so the total work is $O(h)$. The algorithm stores only two node pointers and uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Ancestor hash set:** Store every ancestor of `p`, then climb from `q` until finding a stored node. This also takes $O(h)$ time but uses $O(h)$ space.
- **Compute and align depths:** Measure both distances to the root, advance the deeper node by their difference, and then climb together. This achieves the same $O(h)$ time and $O(1)$ space with two explicit depth passes.
- **Repeated ancestor searches:** For each ancestor of `p`, scanning the full ancestor path of `q` can take $O(h^2)$ time on a skewed tree.
- If `p` is an ancestor of `q`, the walkers meet at `p`; the symmetric case returns `q`.
- Sibling nodes meet at their parent.
- Nodes in different root subtrees meet at the root.
- The guarantee that both nodes belong to one tree ensures a shared ancestor exists, so the walkers meet no later than their redirected traversals reach the common root path.
- Unique values make examples unambiguous, but correctness relies on node identity and parent links rather than value ordering.

</details>
