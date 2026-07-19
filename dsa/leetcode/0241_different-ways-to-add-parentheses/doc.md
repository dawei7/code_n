# Different Ways to Add Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 241 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Recursion, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/) |

## Problem Description
### Goal
Given a valid expression containing nonnegative decimal integers and the binary operators `+`, `-`, and `*`, insert parentheses in every possible way that fully determines the order of operations. The input contains no existing parentheses, and multi-digit numbers remain indivisible operands.

Return one integer result for every structurally distinct full parenthesization. Different evaluation structures must be retained even when they produce the same numeric value, so duplicate results are meaningful and must not be removed. Return the results in any order. Apply each operator to the complete result sets of its left and right subexpressions rather than assuming ordinary multiplication precedence.

### Function Contract
**Inputs**

- `expression`: a valid operator-separated arithmetic expression without existing parentheses

**Return value**

A list containing one result for every full parenthesization; duplicate numeric results are retained and order is unrestricted.

### Examples
**Example 1**

- Input: `expression = "2-1-1"`
- Output: `[0,2]`

**Example 2**

- Input: `expression = "2*3-4*5"`
- Output: `[-34,-14,-10,-10,10]`

**Example 3**

- Input: `expression = "11"`
- Output: `[11]`
