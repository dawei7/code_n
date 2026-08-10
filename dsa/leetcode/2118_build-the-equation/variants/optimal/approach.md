## General

**Format one term according to its power**

The CTE `T` converts every `Terms` row into a text fragment `it` while retaining `power` for later ordering.

Every term begins with an explicit sign. For a positive factor, the expression creates `'+'` followed by the factor. For a negative factor, using `factor` directly converts its existing minus sign into the string.

The factor is therefore represented by its sign plus absolute magnitude, even though the implementation obtains the negative form through normal numeric-to-string coercion.

**Handle the three power shapes**

The `CASE power` expression separates the required syntax:

- power 0 returns only the signed factor, with no `X`;
- power 1 appends `X` but no exponent;
- every other power appends `X^` and the numeric power.

Thus factor 3 at power 1 becomes `+3X`, factor -3 at power 0 becomes `-3`, and factor 1 at power 2 becomes `+1X^2`.

The coefficient 1 is not omitted because the required format always includes `<fact>`.

**Sort terms by descending power during aggregation**

The final aggregate orders fragments by `power DESC` before concatenation. This is necessary because table row order has no semantic guarantee.

Concatenating the signed fragments needs no separator: each fragment already starts with `+` or `-`. Finally, `CONCAT(..., '=0')` appends the required right-hand side.

For powers 2, 1, and 0 with factors 1, -4, and 2, ordered fragments are `+1X^2`, `-4X`, and `+2`. Their concatenation plus `=0` gives `+1X^2-4X+2=0`.

**Why one output row is produced**

The final query contains a string aggregate and no `GROUP BY`, so all formatted terms belong to one aggregation group. The result is a single `equation` column and one row.

The primary-key guarantee on `power` means no two input terms compete for the same exponent in the main problem.

**Exact SQL syntax caveat**

The solution file is labeled as MySQL but writes:

`STRING_AGG(it ORDER BY power DESC SEPARATOR "", ',')`.

That expression is not standard MySQL aggregate syntax. MySQL normally uses:

`GROUP_CONCAT(it ORDER BY power DESC SEPARATOR '')`.

Other database systems expose `STRING_AGG` with different argument syntax, but not the MySQL `SEPARATOR` clause shown here. Therefore, the exact source expresses the intended algorithm but may fail to parse in an actual MySQL judge.

A faithful explanation must distinguish the formatting idea from this executability issue rather than claim the statement is portable valid SQL.

**Why the intended query is correct**

For every row, the `CASE` creates exactly the required signed term for its power category. Sorting places unique powers in descending order. Empty-string concatenation places terms adjacent, where their leading signs separate them unambiguously. Appending `=0` completes the equation.

Assuming a valid ordered string-aggregation function is used, every source term appears once and in the correct format, so the output is correct.

**Why signs double as separators**

The aggregate uses an empty separator rather than commas or spaces. This is safe because every formatted fragment begins with one explicit sign.

For example, joining `+2X^3` and `-5X` directly produces `+2X^3-5X`, whose term boundary remains unambiguous. Adding another separator would violate the required output grammar.

The first term also keeps its sign, so the complete LHS never needs special handling for its leading fragment.

**Follow-up with duplicate powers**

If `power` were not unique but the answer required one term per power, rows should first be grouped by power and their factors summed.

Any group whose summed factor becomes zero should be removed because factor zero is not a meaningful term. The remaining grouped rows can pass through the same formatting and descending concatenation stages.

## Complexity detail

Let $N$ be the number of term rows.

Formatting each row takes linear total work in the resulting small fragments. Ordering terms by power costs $O(N\log N)$ in a comparison-based execution plan, and concatenation is linear in output length. The manifest's total is $O(N\log N)$.

The CTE and ordered aggregation may materialize $O(N)$ fragments, so working space is $O(N)$, in addition to the output equation string.

Physical database plans can vary, especially because `power` is indexed as a unique key and may already support descending order.

## Alternatives and edge cases

- **Valid MySQL aggregation:** Use `GROUP_CONCAT(it ORDER BY power DESC SEPARATOR '')` instead of the nonstandard exact expression.
- **Concatenate without ordering:** Incorrect because SQL row order is not guaranteed and powers must descend.
- **Omit the leading plus:** The format requires an explicit sign even for the first positive term.
- **Power zero:** Include neither `X` nor an exponent.
- **Power one:** Include `X` but omit `^1`.
- **Coefficient one:** Preserve `1` because the specified term grammar includes the absolute factor.
- **Negative factor:** Its existing minus sign supplies the term sign.
- **Unique power:** Main-problem rows need no pre-aggregation by exponent.
- **Duplicate-power follow-up:** Sum factors by power, discard zero sums, then format.
- **Any input row order:** Ordered aggregation controls final order.
- **Right-hand side:** Append exactly `=0` once after the complete LHS.
- **Dialect mismatch:** The algorithm is sound, but the exact aggregate call is not standard MySQL syntax.
- **Empty separator:** Required because signs already delimit adjacent terms.
- **Single term:** Ordered aggregation returns that one signed fragment, followed by `=0`.
