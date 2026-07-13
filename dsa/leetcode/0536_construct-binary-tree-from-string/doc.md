# Construct Binary Tree from String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 536 |
| Difficulty | Medium |
| Topics | String, Stack, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-string/) |

## Problem Description
### Goal
Given a string representation of a binary tree, each node begins with its signed integer value, followed by zero, one, or two parenthesized child representations. Children occur in preorder: the first parenthesized subtree is left and the second is right.

Construct and return the represented binary tree. Empty parentheses may mark a missing left child when a right child must still be written, while an omitted trailing child is simply absent. Parse multi-digit and negative values, preserve the complete nesting structure, and consume the full string rather than stopping after one node or treating parentheses as ordinary characters.

### Function Contract
**Inputs**

- `s`: the tree encoding, containing signed decimal integers and balanced parentheses

**Return value**

- The root of the represented binary tree, or an empty tree when `s` is empty

### Examples
**Example 1**

- Input: `s = "4(2(3)(1))(6(5))"`
- Output tree: `[4, 2, 6, 3, 1, 5]`

**Example 2**

- Input: `s = "-4(2)(3)"`
- Output tree: `[-4, 2, 3]`

**Example 3**

- Input: `s = "4()(5)"`
- Output tree: `[4, null, 5]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Read complete signed integers**

When the cursor reaches a digit or minus sign, consume the optional sign and every following digit as one node value. Create the node immediately rather than searching ahead for its matching closing parenthesis.

**Track open ancestors and their next child slot**

Keep stack frames containing an open node and whether its next subtree belongs on the left or right. A newly parsed node attaches to the slot of the top frame, advances that parent's slot, and becomes the new top frame for any children of its own.

**Use parentheses to open and close subtree contexts**

An opening parenthesis announces a child representation. If it is immediately followed by `)`, advance the current parent's slot without attaching a node; this preserves a missing left child before a right child. Otherwise the next integer begins the child. A nonempty subtree's closing parenthesis pops its root frame, returning parsing context to the parent.

**Why the reconstructed structure is exact**

Preorder places each node before its children, so the current top frame is exactly the parent awaiting the next encoded subtree. Slot advancement assigns the first child expression left and the second right, including explicit empty expressions. Closing parentheses remove precisely the completed subtree context. Thus every encoded value and absence marker is attached at its unique prescribed position.

#### Complexity detail

The cursor advances monotonically and examines each of the `n` characters a constant number of times, giving $O(n)$ time. The stack holds one frame per open ancestor, so auxiliary space is $O(h)$ for tree height `h`, excluding the required nodes.

#### Alternatives and edge cases

- **Recursive parser with one shared cursor:** also runs in $O(n)$ time and mirrors the grammar directly, but a deeply skewed tree can exceed the call-stack limit.
- **Find matching parentheses and slice substrings:** is intuitive but repeatedly scans and copies nested suffixes, degrading to $O(n^2)$ on a skewed encoding.
- **Tokenize first:** separates lexical and structural parsing but stores $O(n)$ additional tokens.
- **Negative value:** consume the sign as part of the following integer.
- **Leaf node:** has no parentheses and remains on the stack only until its containing subtree closes.
- **Right child without left child:** the explicit `()` must advance the left slot before parsing the right subtree.
- **Empty string:** represents an empty tree.
- **Multi-digit values:** consume the entire digit run as one node.

</details>
