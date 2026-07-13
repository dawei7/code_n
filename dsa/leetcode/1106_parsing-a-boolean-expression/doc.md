# Parsing A Boolean Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1106 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [parsing-a-boolean-expression](https://leetcode.com/problems/parsing-a-boolean-expression/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/parsing-a-boolean-expression/).

### Goal
Evaluate a boolean expression containing literals `t` and `f`, unary not `!`, conjunction `&`, disjunction `|`, parentheses, and commas.

### Function Contract
**Inputs**

- `expression`: Boolean expression string.

**Return value**

Boolean result of evaluating the expression.

### Examples
**Example 1**

- Input: `expression = "!(f)"`
- Output: `true`

**Example 2**

- Input: `expression = "|(f,t)"`
- Output: `true`

**Example 3**

- Input: `expression = "&(t,f)"`
- Output: `false`

---

## Solution
### Approach
Parse recursively. A literal evaluates directly. For an operator, skip the opening parenthesis, recursively evaluate each comma-separated child expression, and combine the child values according to the operator.

A stack-based parser works as well: collect values until a closing parenthesis, then reduce the collected group using the operator before the group.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the expression length.
- **Space Complexity**: `O(n)` for recursion or stack state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
