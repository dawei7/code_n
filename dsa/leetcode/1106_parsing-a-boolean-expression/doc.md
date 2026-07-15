# Parsing A Boolean Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1106 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/parsing-a-boolean-expression/) |

## Problem Description

### Goal

A boolean expression evaluates to either `true` or `false`. The literal `t` is true and `f` is false. An expression `!(subExpr)` applies logical NOT to one inner expression.

An expression `&(subExpr1, subExpr2, ..., subExprN)` applies logical AND to one or more comma-separated inner expressions, while `|(subExpr1, subExpr2, ..., subExprN)` applies logical OR. Inner expressions may themselves contain any valid form. Given a guaranteed-valid expression, return its boolean evaluation.

### Function Contract

**Inputs**

- `expression`: a valid boolean expression of length $n$, where $1 \leq n \leq 2 \cdot 10^4$ and each character is `(`, `)`, `&`, `|`, `!`, `t`, `f`, or `,`.

**Return value**

`True` when the complete expression evaluates to true; otherwise `False`.

### Examples

**Example 1**

- Input: `expression = "&(|(f))"`
- Output: `False`

**Example 2**

- Input: `expression = "|(f,f,f,t)"`
- Output: `True`

**Example 3**

- Input: `expression = "!(&(f,t))"`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep unresolved syntax on a stack.** Scan left to right. Push literals, operators, and opening parentheses; commas only separate operands and do not need storage. Before a closing parenthesis arrives, every nested group inside it has already been reduced to one literal.

**Reduce one complete group at `)`.** Pop `t` and `f` operands until reaching `(`, remove that parenthesis, then pop the operator immediately before it. NOT flips its sole operand. AND is true only if every popped value is true, while OR is true if at least one is true. Push the resulting `t` or `f` back as one operand for an enclosing group.

**Read the remaining literal.** A valid complete expression leaves exactly one reduced truth literal on the stack. It is also possible for the original expression to be the single literal `t` or `f`, which follows the same final check.

The stack always represents the scanned prefix with each completed subexpression replaced by its correct literal value. A closing parenthesis exposes exactly the operands and operator of one valid innermost group, and the reduction applies that operator's definition. Induction over closing parentheses preserves the invariant until the entire expression is reduced correctly.

#### Complexity detail

Each of the $n$ characters is pushed, ignored, or popped a constant number of times, so evaluation takes $O(n)$ time. In the deepest nesting or widest operand list, the stack stores $O(n)$ unresolved symbols.

#### Alternatives and edge cases

- **Recursive descent:** Parse one expression and advance a shared index through its children; this is also $O(n)$ but deep valid nesting can exceed a language's recursion limit.
- **Repeated textual replacement:** Evaluating an innermost group and rebuilding the whole expression is correct but can take $O(n^2)$ time.
- **Literal expression:** `t` and `f` require no parentheses or operator.
- **Single-operand AND or OR:** Their result equals their only operand, as allowed by the grammar.
- **Nested NOT:** Each unary layer must flip the already-evaluated inner result exactly once.
- **Short-circuit semantics:** The parser still must consume all characters even when an AND is already false or an OR is already true.

</details>
