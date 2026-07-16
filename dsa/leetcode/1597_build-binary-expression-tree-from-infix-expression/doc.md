# Build Binary Expression Tree From Infix Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1597 |
| Difficulty | Hard |
| Topics | String, Stack, Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/) |

## Problem Description
### Goal
Given a syntactically valid infix arithmetic expression `s`, construct its binary expression tree. Each operand is a single decimal digit, and the available binary operators are `+`, `-`, `*`, and `/`. Parentheses may override the usual precedence rules. Without parentheses, multiplication and division bind more tightly than addition and subtraction, and operators of equal precedence associate from left to right.

Every leaf of the returned tree represents an operand. Every internal node represents an operator whose left and right subtrees are that operator's two operands. The tree must encode the same grouping and evaluation order as the original expression; parentheses affect the structure but do not become nodes themselves.

### Function Contract
**Inputs**

- `s`: a valid infix expression containing single-digit operands, binary operators from `{'+', '-', '*', '/'}`, and balanced parentheses.

**Return value**

Return the root node of the binary expression tree. Each node has `val`, `left`, and `right` attributes; operand nodes have no children.

### Examples
**Example 1**

- Input: `s = "3*4-2*5"`
- Output: a tree rooted at `'-'`, with `3*4` as its left subtree and `2*5` as its right subtree.

**Example 2**

- Input: `s = "2-3/(5*2)+1"`
- Output: a tree representing `(2 - (3 / (5 * 2))) + 1`.

**Example 3**

- Input: `s = "1+2+3+4+5"`
- Output: a left-associated addition tree representing `((((1+2)+3)+4)+5)`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Let $n = \lvert s \rvert$.

**Separate unfinished operators from completed subtrees.** Scan the expression once. An operand immediately becomes a one-node tree on a node stack. Operators wait on a second stack until the parser knows that their right operand has ended. Combining an operator pops its right subtree and then its left subtree, creates the operator node, and pushes the completed larger tree back.

**Use precedence to decide when an operator is ready.** Before pushing a new operator, combine every waiting non-parenthesis operator with greater or equal precedence. Greater precedence must bind first; equal precedence must also bind first because all four operators are left-associative. An opening parenthesis acts as a barrier. A closing parenthesis combines everything back to that barrier and then removes the parenthesis without creating a node.

At each scan position, the node stack contains exactly the completed operand trees in the parsed prefix, while the operator stack contains precisely the operators whose right operand is not yet closed. The precedence rule combines an operator at the first moment no future token can belong inside either of its operands. Balanced parentheses enforce their explicit grouping. After the scan, combining the remaining operators therefore leaves one tree whose inorder expression has exactly the contract's precedence, associativity, and parenthesized structure.

#### Complexity detail

Each token is pushed once and popped at most once. Each operator creates exactly one internal node, so total time is $O(n)$. The two stacks and the returned tree each contain at most $O(n)$ elements; excluding the required output tree, the auxiliary space is also $O(n)$ in the worst case.

#### Alternatives and edge cases

- **Recursive lowest-precedence search:** Repeatedly scan a substring for its root operator and recurse on both sides. It is intuitive, but a long left-associated chain can cause $O(n^2)$ repeated scanning.
- **Postfix conversion followed by tree construction:** Shunting-yard can first produce a postfix token list and then build the tree in a second pass. This remains $O(n)$ but stores an additional full representation.
- Equal-precedence subtraction and division must associate leftward; choosing the wrong stack comparison changes expressions such as `8/4/2`.
- Parentheses can force a lower-precedence operator below a multiplication or division node, as in `(1+2)*3`.
- A single digit produces one leaf node and requires no operator combination.
- Parentheses are control tokens only and never appear as node values.

</details>
