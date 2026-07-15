# Flip Binary Tree To Match Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 971 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [flip-binary-tree-to-match-preorder-traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) |

## Problem Description

### Goal

You are given a binary tree whose $N$ node values are unique and a length-$N$ sequence `voyage`. The desired sequence is a preorder traversal: visit a node first, then its left subtree, then its right subtree.

You may flip any node by swapping its entire left and right subtrees. Use the fewest node flips needed to make the resulting preorder traversal equal `voyage`, and return the values of the flipped nodes in any order. If no sequence of flips can produce the voyage, return `[-1]`.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ uniquely valued nodes.
- `voyage`: a permutation of the $N$ node values describing the required preorder traversal.
- The size satisfies $1 \le N \le 100$, and every value is between $1$ and $N$.
- Serialized trees use level order and `null` for a missing child.

**Return value**

Return the values of a minimum-cardinality set of nodes to flip, in any order, or `[-1]` when the voyage is impossible.

### Examples

**Example 1**

- Input: `root = [1,2], voyage = [2,1]`
- Output: `[-1]`

**Example 2**

- Input: `root = [1,2,3], voyage = [1,3,2]`
- Output: `[1]`

**Example 3**

- Input: `root = [1,2,3], voyage = [1,2,3]`
- Output: `[]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Match preorder one node at a time.** Keep an index into `voyage` and traverse the effective tree in preorder with a stack. When a popped node does not equal the next voyage value, no flip at that node or below can change which node is visited now, so return `[-1]`.

**The next value forces every flip.** After matching a node, preorder must enter its first non-null child. If a left child exists but its value is not the next voyage value, the only possible correction is to flip the current node and visit its right subtree first. Record the current node's value. Otherwise keep the normal left-before-right order.

**Push children in effective reverse order.** Because the stack is last-in, first-out, push the later subtree first. Without a flip, push right then left; after a flip, push left then right. This simulates the changed traversal without mutating the tree.

**Why the flip count is minimum.** A mismatch between the required next value and an existing left child forces a flip: no operation below the current node can replace that first subtree root. Conversely, when the next value already matches the left child, flipping would immediately contradict the voyage. Every recorded choice is therefore necessary, and the complete successful traversal uses the unique minimum set.

#### Complexity detail

Each of the $N$ nodes is pushed, popped, and compared once, so the running time is $O(N)$. The traversal stack and returned flip list use $O(N)$ space in the worst case.

#### Alternatives and edge cases

- **Recursive preorder:** Carry a shared voyage index and recurse into children in the forced order. This has the same bounds but depends on the call stack.
- **Try both orders at every node:** Backtracking over flip and no-flip choices is correct but can explore exponentially many configurations even though the next voyage value already determines the choice.
- **Repeated suffix searches:** Scan the unconsumed voyage to locate child values at every node. It adds no useful information and can take $O(N^2)$ time.
- **Root mismatch:** Return `[-1]` immediately because flips never change the root.
- **One child:** A flip can change whether that subtree is visited as left or right, but cannot change its root value or preorder position.
- **Already matching:** Return an empty list when the original preorder equals `voyage`.

</details>
