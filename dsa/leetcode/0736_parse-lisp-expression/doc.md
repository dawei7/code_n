# Parse Lisp Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 736 |
| Difficulty | Hard |
| Topics | Hash Table, String, Stack, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/parse-lisp-expression/) |

## Problem Description
### Goal
Given one valid Lisp-like expression, evaluate it to an integer. An expression may be an integer, a variable, `(add e1 e2)`, `(mult e1 e2)`, or a `let` expression containing variable-expression bindings followed by one result expression.

Evaluate `let` bindings sequentially from left to right in a new lexical scope, so later bindings and the final expression can use earlier values. Inner bindings may shadow an outer variable only within their scope, and variable lookup uses the nearest active binding. Return the value of the complete expression.

### Function Contract
**Inputs**

- `expression`: one valid expression using integers, variable names, `(add e1 e2)`, `(mult e1 e2)`, or `(let v1 e1 ... vn en result)`

**Return value**

- The integer value of the complete expression under the language's lexical scoping rules

### Examples
**Example 1**

- Input: `expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"`
- Output: `14`

**Example 2**

- Input: `expression = "(let x 3 x 2 x)"`
- Output: `2`

**Example 3**

- Input: `expression = "(let x 1 y 2 x (add x y) (add x y))"`
- Output: `5`
