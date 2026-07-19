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
