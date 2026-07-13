# Convert Binary Search Tree to Sorted Doubly Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 426 |
| Difficulty | Medium |
| Topics | Linked List, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) |

## Problem Description
### Goal
Given the root of a binary search tree, convert its existing nodes into a sorted circular doubly linked list. Binary-search inorder order determines the ascending sequence, and node `left` and `right` pointers become previous and next links respectively.

Return the smallest node as the list head. Following `right` must visit every node once in ascending order before returning to the head; following `left` must traverse the reverse order. Join the largest and smallest nodes in both directions, reuse every original node exactly once, and return `null` for an empty tree.

### Function Contract
**Inputs**

- `root`: the root node of a binary search tree, or `None` for an empty tree

**Return value**

- Return the smallest node; following `right` visits values in ascending order and following `left` visits them in descending order, with both ends joined circularly. Example outputs show one complete forward traversal.

### Examples
**Example 1**

- Input: `root = [4, 2, 5, 1, 3]`
- Output: `[1, 2, 3, 4, 5]`

**Example 2**

- Input: `root = [2, 1, 3]`
- Output: `[1, 2, 3]`

**Example 3**

- Input: `root = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Use inorder traversal as the sorted order**

An inorder traversal of a binary search tree visits nodes from smallest to largest. Keep `previous`, the most recently visited node, and `first`, the smallest node encountered. When visiting a node, connect `previous.right` to it and its `left` back to `previous`; the first visit initializes `first` instead.

**Preserve the unvisited right subtree**

The traversal processes the original left subtree before rewiring the current node's left link. Its original right link is not replaced until a later node connects back as the successor, so recursively visiting the right subtree immediately after linking the current node remains safe.

**Close both ends after traversal**

After inorder traversal, `first` is the minimum and `previous` is the maximum. Set `first.left = previous` and `previous.right = first`. These two assignments turn the already sorted bidirectional chain into the required cycle.

**Why every link is correct**

Each adjacent pair in inorder order is linked exactly when the later node is visited, in both directions. No node is skipped or created. The final two assignments provide the only missing predecessor and successor links, so every node has exactly its sorted predecessor on the left and sorted successor on the right, including wraparound.

#### Complexity detail

Every node is visited and linked once, giving $O(n)$ time. Recursive calls follow one root-to-leaf path at a time, so auxiliary space is $O(h)$, where `h` is the tree height.

#### Alternatives and edge cases

- **Iterative inorder traversal:** uses an explicit $O(h)$ stack and links nodes in the same order.
- **Collect all nodes first:** simplifies linking but uses $O(n)$ auxiliary space; repeatedly searching that list for each node can further degrade to $O(n^2)$ time.
- **Empty tree:** return `None` without attempting endpoint links.
- **Single node:** both `left` and `right` must point back to that node.
- **Skewed tree:** recursion uses $O(n)$ stack space in the worst case.

</details>
