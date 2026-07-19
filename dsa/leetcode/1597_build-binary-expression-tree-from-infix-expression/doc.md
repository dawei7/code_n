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
