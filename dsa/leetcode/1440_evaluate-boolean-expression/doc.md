# Evaluate Boolean Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1440 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/evaluate-boolean-expression/) |

## Problem Description

### Goal

The `Variables` table assigns an integer value to each variable name. Every row in `Expressions` names a left variable, one comparison operator, and a right variable.

Evaluate each expression using the current values of its two operands. Return the original `left_operand`, `operator`, and `right_operand` columns together with a `value` column containing the lowercase string `"true"` when the comparison holds and `"false"` otherwise. The supported operators are `<`, `>`, and `=`.

### Function Contract

**Inputs**

- `Variables(name, value)`: one row per variable, with `name` as its unique identifier and `value` as an integer.
- `Expressions(left_operand, operator, right_operand)`: comparison expressions whose two operand names both occur in `Variables`.
- `operator` is one of `"<"`, `">"`, or `"="`.

**Return value**

- One row per expression with columns `left_operand`, `operator`, `right_operand`, and `value`, where `value` is exactly `"true"` or `"false"`.

### Examples

**Example 1**

- Input: `Variables = [("x",66),("y",77)]`, `Expressions = [("x",">","y"),("x","<","y"),("x","=","y")]`
- Output: `[("x","<","y","true"),("x","=", "y","false"),("x",">","y","false")]`

**Example 2**

- Input: `Variables = [("a",5),("b",5)]`, `Expressions = [("a","=","b"),("a","<","b")]`
- Output: `[("a","<","b","false"),("a","=","b","true")]`

**Example 3**

- Input: `Variables = [("low",-2),("high",3)]`, `Expressions = [("high",">","low")]`
- Output: `[("high",">","low","true")]`
