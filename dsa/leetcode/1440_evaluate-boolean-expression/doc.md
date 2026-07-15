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

### Required Complexity

- **Time:** $O(V+E)$
- **Space:** $O(V+E)$

<details>
<summary>Approach</summary>

#### General

**Join each operand in its own role.** Join `Expressions` to `Variables` once as `left_variable` using `left_operand = name` and once as `right_variable` using `right_operand = name`. The aliases keep the two looked-up integer values distinct even when both operands name the same variable.

**Dispatch on the stored operator.** Use a `CASE` expression with one branch for each supported symbol. A `<` row compares `left_variable.value < right_variable.value`, a `>` row reverses the relation, and an `=` row tests equality.

**Convert the boolean to the required text.** SQL dialects represent comparison results differently, so return explicit string literals: emit `'true'` when the operator-specific predicate holds and `'false'` otherwise. Alias that expression as `value`.

**Why each output row is exact.** The foreign-key guarantee gives each operand name one matching variable row, so the two joins attach exactly the values named by the expression without duplicating it. The `CASE` branch selected by `operator` evaluates precisely that row's requested relation. The final projection preserves the original expression fields and adds only its textual truth value.

#### Complexity detail

With the unique variable-name lookup indexed or hashed, building/accessing the $V$ variable entries and evaluating the $E$ expressions takes $O(V+E)$ logical time. The input relations, join lookup structure, and $E$-row result occupy $O(V+E)$ space in the database execution model.

#### Alternatives and edge cases

- **Correlated scalar lookups:** Looking up each operand with a separate subquery for every expression can repeatedly scan `Variables` and take $O(VE)$ time.
- **One variable join:** A single alias cannot independently resolve two operand names; join the table twice.
- **Compare operand names:** The relation applies to the integer `value` columns, not the lexical order of variable names.
- **Equal operands:** `x = x` is true, while `x < x` and `x > x` are false.
- **Equal values under different names:** Equality depends on values, not name identity.
- **Output spelling:** Return lowercase strings `"true"` and `"false"` rather than database booleans or numeric flags.
- **Negative values:** Ordinary integer comparison semantics still apply.
- **Row order:** The logical result is one row per expression; an explicit order can make local verification deterministic.

</details>
