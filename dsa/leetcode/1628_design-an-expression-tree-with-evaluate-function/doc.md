# Design an Expression Tree With Evaluate Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1628 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Stack, Tree, Design, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) |

## Problem Description
### Goal
Design an expression-tree implementation for a valid postfix expression. Each token is either an integer operand or one of the binary operators `+`, `-`, `*`, and `/`. In postfix order, an operator follows the complete encodings of its left and right operands.

Implement a concrete subclass of the provided abstract `Node` interface. Calling `evaluate()` on the root must recursively compute the expression's integer value. Also implement `TreeBuilder.buildTree(postfix)`, which constructs and returns the root node. Division truncates toward zero, and every division in the valid input has a nonzero divisor.

### Function Contract
**Inputs**

- `postfix`: a nonempty array of $t$ tokens encoding one valid binary arithmetic expression in postfix notation, where $1 \le t < 100$ and $t$ is odd.
- Operand tokens are decimal integer strings; operator tokens are `"+"`, `"-"`, `"*"`, or `"/"`.
- Every operand is at most $10^5$, and all intermediate and final absolute values are at most $10^9$.
- Let $m$ be the number of operand tokens. A valid full binary expression has $t=2m-1$ tokens.

**Return value**

`TreeBuilder.buildTree(postfix)` returns a `Node` root whose `evaluate()` method returns the expression's integer value. The cOde(n) harness reports that observable evaluation result directly.

### Examples
**Example 1**

- Input: `postfix = ["3","4","+","2","*","7","/"]`
- Output: `2`

The tree represents `(3 + 4) * 2 / 7`.

**Example 2**

- Input: `postfix = ["4","5","2","7","+","-","*"]`
- Output: `-16`

The tree represents `4 * (5 - (7 + 2))`.

**Example 3**

- Input: `postfix = ["42"]`
- Output: `42`

A single operand becomes a leaf that evaluates to its own value.
