# Maximum Binary Tree II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 998 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-binary-tree-ii/) |

## Problem Description

### Goal

A maximum tree is a binary tree in which each node's value is greater than every other value in its subtree. The given `root` was constructed from an unknown list `a`: choose the largest list element as the root, recursively construct the left child from the elements before that maximum, and recursively construct the right child from the elements after it.

Create `b` by appending `val` to the end of `a`. All values in `b` are guaranteed to be unique. Although `a` itself is unavailable, return the maximum tree that the same recursive construction would produce from `b`.

### Function Contract

**Inputs**

- `root`: the root of a maximum binary tree with $N$ unique nodes, where $1\le N\le100$ and every node value lies from $1$ through $100$.
- `val`: a value from $1$ through $100$ that does not occur in the tree.

Let $H$ be the height of the tree's right spine.

**Return value**

- The root of the maximum tree obtained after appending `val` to the source list.

### Examples

**Example 1**

- Input: `root = [4, 1, 3, null, null, 2], val = 5`
- Output: `[5, 4, null, 1, 3, null, null, 2]`
- Explanation: Appending $5$ makes it the maximum of the entire sequence, so the old tree becomes its left subtree.

**Example 2**

- Input: `root = [5, 2, 4, null, 1], val = 3`
- Output: `[5, 2, 4, null, 1, null, 3]`

**Example 3**

- Input: `root = [5, 2, 3, null, 1], val = 4`
- Output: `[5, 2, 4, null, 1, 3]`

### Required Complexity

- **Time:** $O(H)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only the right spine can change:** Inorder traversal of a maximum tree recovers its source list. Because `val` is appended at the list's end, it lies to the right of every existing element. Therefore its position in the reconstructed tree can affect only ancestors reached by following right-child links from the root.

**Find the first smaller right-spine node:** If `val` exceeds the root, create a new root and attach the entire old tree as its left child. Otherwise, walk down the right spine while the next node's value remains greater than `val`. Create the new node at the first break: its left child becomes the smaller right subtree that used to occupy that link, and the preceding node's right child becomes the new node.

All nodes above the insertion point remain greater than `val`, so their maximum-tree relationships stay valid. Every node moved under the new node is smaller than `val`, and its inorder positions still precede the appended value. The resulting tree therefore has exactly the inorder sequence `a` followed by `val` and preserves the maximum-tree construction.

#### Complexity detail

The algorithm examines at most the $H$ nodes on the right spine, giving $O(H)$ time. It creates one node and uses a constant number of pointers, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recover the full list and rebuild:** Inorder traversal followed by maximum-tree reconstruction is correct but touches every node and can take $O(N^2)$ time with repeated maximum searches.
- **Recursive right-spine insertion:** This expresses the same recurrence in $O(H)$ time but uses $O(H)$ call-stack space.
- **New global maximum:** When `val > root.val`, the returned node is a new root whose left child is the old root.
- **New smallest suffix value:** The insertion reaches the end of the right spine and attaches a leaf.
- **Middle insertion:** A smaller right subtree becomes the new node's left subtree rather than being discarded.

</details>
