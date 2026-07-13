# Ternary Expression Parser

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 439 |
| Difficulty | Medium |
| Topics | String, Stack, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/ternary-expression-parser/) |

## Problem Description
### Goal
Given a valid ternary expression made from single-character operands, `?`, and `:`, evaluate it under right associativity. Each condition is `T` or `F`; `T ? a : b` selects `a`, while `F ? a : b` selects `b`.

Expressions may nest in either branch, and a selected result may be a digit or Boolean letter. Return the final single-character value. Match each question mark with the correct colon rather than evaluating from left to right, and do not evaluate an unselected branch as though it could change the result. The input contains no parentheses or whitespace.

### Function Contract
**Inputs**

- `expression`: a valid expression composed of single-character operands, `?`, and `:`

**Return value**

- Return the single-character value selected by the nested ternary expression.

### Examples
**Example 1**

- Input: `expression = "T?2:3"`
- Output: `"2"`

**Example 2**

- Input: `expression = "F?1:T?4:5"`
- Output: `"4"`

**Example 3**

- Input: `expression = "T?T?F:5:3"`
- Output: `"F"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Process the right-associative expression from right to left**

The innermost or rightmost ternary must be resolved before a condition to its left can use its result. Scan characters in reverse and push ordinary operands and separators onto a stack.

**Reduce one complete ternary at its condition**

When the current character is `T` or `F` and the stack top is `?`, the stack already contains the complete true value, `:`, and false value in that order. Remove those markers and operands, choose the true or false value from the condition, and push the single chosen result back.

**Why every reduction respects nesting**

Reverse scanning reaches both branches of a right-associative ternary before its condition. Any ternary nested inside either branch has a condition farther right and is therefore already reduced to one operand. Thus each reduction consumes exactly one syntactically complete expression and leaves an equivalent single value for its parent. The final stack value equals the whole expression.

#### Complexity detail

Each of the `n` characters is pushed or removed a constant number of times, giving $O(n)$ time. The stack can hold $O(n)$ characters for a deeply nested expression.

#### Alternatives and edge cases

- **Recursive cursor parser:** parse both branches while returning the next unread index; this also takes $O(n)$ time and $O(n)$ recursion space.
- **Rescan for the matching colon:** recursively search each substring for its top-level separator; repeated scans and slices can take $O(n^2)$ on deep nesting.
- **Single operand:** return it without stack reduction.
- **Right associativity:** `a?b:c?d:e` groups the false branch as `c?d:e`.
- **Boolean terminal:** `T` or `F` may be a branch value as well as a condition.
- **Deep nesting:** an iterative stack avoids recursion-depth limits.

</details>
