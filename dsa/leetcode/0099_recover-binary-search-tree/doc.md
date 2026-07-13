# Recover Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 99 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/recover-binary-search-tree/) |

## Problem Description
### Goal
You are given a binary search tree whose structure is intact but whose values were corrupted by swapping exactly two nodes. As a result, its inorder values are no longer strictly increasing in the proper positions.

Restore the binary search tree by swapping those two values back. Modify the existing tree in place, preserve every parent-child link, and return no value in the native contract. The misplaced nodes may be adjacent or far apart in inorder order, including the root or leaves.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`None`; mutate the `TreeNode` values in place so the original root represents the recovered BST.

### Examples
**Example 1**

- Input: `root = [1, 3, null, null, 2]`
- Output tree: `[3, 1, null, null, 2]`

**Example 2**

- Input: `root = [3, 1, 4, null, null, 2]`
- Output tree: `[2, 1, 4, null, null, 3]`

**Example 3**

- Input: `root = [2, 3, 1]`
- Output tree: `[2, 1, 3]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A two-value swap leaves a characteristic inversion pattern**

An inorder traversal of a valid strict BST is increasing. If two adjacent inorder values are swapped, the sequence contains one descent. If separated values are swapped, the larger misplaced value creates the first descent and the smaller misplaced value creates a later descent. No other values need to change.

**First excessive predecessor and last too-small successor are the swap pair**

Whenever `previous.val > current.val`, record `previous` as `first` only if this is the first inversion, and assign `current` to `second` on every inversion. For an adjacent swap, both candidates come from the single descent. For a separated swap, retaining the first predecessor and updating to the second descent's current node selects the two distant misplaced values rather than either middle neighbor.

**Morris threads provide inorder order without stack space**

If a node has no left child, visit it immediately and move right. Otherwise find its inorder predecessor: the rightmost node in its left subtree. On the first encounter, set `predecessor.right` to the current node and descend left. On the second encounter, that pointer already returns to current; remove it, visit current, and move right.

The temporary thread replaces the return address a recursion stack would have stored. Every created pointer is removed before traversal advances beyond its owner, restoring the original tree structure even though node values are later swapped.

**Inversion detection is independent of traversal storage**

Before each inorder visit, `previous` is the immediately preceding node in inorder sequence, completed Morris threads have been removed, and `first`/`second` summarize every descent seen so far. Thread creation does not count as a visit and therefore cannot disturb sequence comparisons.

**Trace adjacent and separated swaps**

Sequence `1,3,2,4` has one inversion $3 > 2$, selecting nodes `3` and `2`. Sequence `1,4,3,2,5` has descents $4 > 3$ and $3 > 2$; the first predecessor is `4` and the last current node is `2`. Swapping those endpoints restores both sequences.

**Inorder inversion endpoints identify the swapped nodes**

A valid BST's inorder values are strictly increasing. Swapping two values creates either one adjacent descent or two separated descents. In both cases, the predecessor at the first descent is the larger misplaced value, while the current node at the last descent is the smaller misplaced value.

No other value is out of its relative position because only those two nodes were swapped. Exchanging the identified endpoints restores strict inorder order, which is equivalent to the BST ordering property, without changing the tree structure.

#### Complexity detail

Each tree edge is followed a constant number of times during Morris traversal, so total time is $O(n)$. Only a fixed number of node pointers is stored, giving $O(1)$ auxiliary space; temporary threads are removed before returning.

#### Alternatives and edge cases

- **Explicit inorder stack:** is simpler and remains $O(n)$ time, but uses $O(h)$ auxiliary space.
- **Store and sort all nodes:** uses $O(n)$ extra space and $O(n \log n)$ time.
- **Compare only parent and child values:** misses violations between a node and a distant ancestor.
- The problem guarantees exactly two swapped values, so both candidates exist. A defensive general-purpose repair API would need to handle an already valid tree separately.
- Morris traversal temporarily mutates right pointers; early returns before all threads are removed would corrupt the structure.

</details>
