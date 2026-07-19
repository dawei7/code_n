## General
**Join each operand in its own role.** Join `Expressions` to `Variables` once as `left_variable` using `left_operand = name` and once as `right_variable` using `right_operand = name`. The aliases keep the two looked-up integer values distinct even when both operands name the same variable.

**Dispatch on the stored operator.** Use a `CASE` expression with one branch for each supported symbol. A `<` row compares `left_variable.value < right_variable.value`, a `>` row reverses the relation, and an `=` row tests equality.

**Convert the boolean to the required text.** SQL dialects represent comparison results differently, so return explicit string literals: emit `'true'` when the operator-specific predicate holds and `'false'` otherwise. Alias that expression as `value`.

**Why each output row is exact.** The foreign-key guarantee gives each operand name one matching variable row, so the two joins attach exactly the values named by the expression without duplicating it. The `CASE` branch selected by `operator` evaluates precisely that row's requested relation. The final projection preserves the original expression fields and adds only its textual truth value.

## Complexity detail
With the unique variable-name lookup indexed or hashed, building/accessing the $V$ variable entries and evaluating the $E$ expressions takes $O(V+E)$ logical time. The input relations, join lookup structure, and $E$-row result occupy $O(V+E)$ space in the database execution model.

## Alternatives and edge cases
- **Correlated scalar lookups:** Looking up each operand with a separate subquery for every expression can repeatedly scan `Variables` and take $O(VE)$ time.
- **One variable join:** A single alias cannot independently resolve two operand names; join the table twice.
- **Compare operand names:** The relation applies to the integer `value` columns, not the lexical order of variable names.
- **Equal operands:** `x = x` is true, while `x < x` and `x > x` are false.
- **Equal values under different names:** Equality depends on values, not name identity.
- **Output spelling:** Return lowercase strings `"true"` and `"false"` rather than database booleans or numeric flags.
- **Negative values:** Ordinary integer comparison semantics still apply.
- **Row order:** The logical result is one row per expression; an explicit order can make local verification deterministic.
