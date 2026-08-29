## General

**Carry one remembered drink through the presented rows**

The required transformation is a forward fill: a non-null `drink` becomes the current remembered value, while a null `drink` receives the most recently remembered non-null value.

The exact MySQL query stores that memory in the session user variable `@cur`. Each output row evaluates:

```sql
CASE
    WHEN drink IS NOT NULL THEN @cur := drink
    ELSE @cur
END
```

For a non-null row, assignment expression `@cur := drink` both updates the variable and evaluates to the assigned drink, so the original value is returned. For a null row, no assignment occurs; the expression returns whatever drink the variable remembers from an earlier row.

**Why the first-row guarantee matters**

The statement guarantees that the first presented row has a non-null drink. On that row, `@cur` is assigned before any null row needs it. Every later null can therefore inherit a real drink value.

If the first row were null and `@cur` had no value, the query would return null there because no preceding non-null drink exists. The guarantee removes that undefined logical case.

In a fresh MySQL session, an unset user variable reads as `NULL`. The source does not explicitly initialize `@cur`, so it relies on the first processed row overwriting it before the else branch is used. In a reused session where `@cur` had an old value, proper first-row processing still replaces it immediately.

**Trace the example state**

Assume rows are evaluated in the displayed sequence.

- ID `9` contains `"Rum and Coke"`. The true branch assigns that string to `@cur` and returns it.
- ID `6` is null. The else branch returns the remembered `"Rum and Coke"`.
- ID `7` is also null and receives the same value.
- ID `3` contains `"St Germain Spritz"`, so `@cur` changes.
- ID `1` then changes it again to `"Orange Margarita"`.
- ID `2` is null and receives that latest value.

The output ID and computed drink are selected together, so every row retains its ID while only the drink field may be filled.

**Why consecutive nulls work**

A null row reads `@cur` but does not change it. Therefore, an arbitrary run of consecutive null rows all receive the same preceding non-null drink. The remembered value changes only when a real drink is encountered, which exactly matches “previous row that is not null” rather than simply “immediately previous row.”

**The ordering assumption is material**

SQL tables are unordered relations unless a query has a defined ordering. The source query has no `ORDER BY`, and the schema's `id` is not the desired order—the example order `9, 6, 7, 3, 1, 2` demonstrates that sorting by ID would be wrong.

The exact query therefore relies on the problem platform preserving the input's presented row sequence during evaluation and output. It also relies on MySQL evaluating the user-variable assignment row by row in that same sequence. These are environment-specific behaviors, not a portable SQL guarantee.

This is more than a cosmetic caveat: “previous” has no relational meaning without an ordering attribute. A fully portable solution would need an explicit column that encodes row order, or platform-specific access to that order. The local statement asks for the same input order but exposes no such column.

**Exact source versus the manifest summary**

The manifest describes assigning sequence numbers and recursively carrying values. The actual source contains neither a row number nor a recursive CTE; it uses a mutable session variable in a single scan.

Accordingly, the algorithm explained here is the stateful MySQL scan actually executed. A recursive forward-fill method belongs among alternatives and would still require a trustworthy ordering key.

**Conditional correctness under the platform order**

Assume rows are evaluated in the required input order and `@cur` is assigned on the first non-null row as guaranteed. Maintain the invariant that immediately before each row after the first, `@cur` equals the nearest non-null drink among all preceding rows.

If the current drink is null, returning `@cur` supplies exactly that nearest value and leaves the invariant unchanged for the next row. If it is non-null, returning it is correct and assigning it makes it the nearest non-null value for the next row. The first row establishes the invariant.

By induction, every computed drink is correct under the platform's presented-order behavior. Because the query performs no explicit sort or filter, it also returns one row per input row in the provider-preserved order.

## Complexity detail

Let $R$ be the number of rows. Under the intended streaming execution, the query examines each row once, performs one null test and at most one variable assignment, so its logical time is $O(R)$. The mutable state `@cur` uses $O(1)$ additional space beyond the $R$-row result.

The manifest's $O(R\log R)$ time and $O(R)$ space describe a different sequence-number/recursive implementation that may sort or materialize rows. Those are not the exact operational bounds of this source query.

Database engines may materialize result rows internally, but that physical result handling is separate from the query's constant-size forward-fill state.

## Alternatives and edge cases

- **Recursive CTE with an order column:** Number rows, then recurse from row `r` to `r+1` carrying `COALESCE(current_drink, previous_drink)`. This is more explicit but needs a real ordering attribute.
- **Window function with `IGNORE NULLS`:** `LAST_VALUE` over a defined row order can express forward fill on engines supporting the needed null semantics; MySQL support and syntax vary.
- **Correlated previous-row lookup:** Find the greatest earlier ordered row with non-null drink. It is portable only when “earlier” has a schema key and may be less efficient.
- **Consecutive null rows:** They all reuse the same unchanged `@cur` value.
- **First row:** Its non-null guarantee initializes the carried value.
- **Later non-null row:** It replaces `@cur` and begins a new fill region.
- **No nulls:** Every row assigns and returns its own drink.
- **No explicit order column:** This is the central portability limitation; primary-key `id` does not encode displayed order.
- **Session-variable state:** A clean first processed row overwrites old state, but user-variable evaluation order remains MySQL-specific.
- **Output order:** The exact query relies on provider row presentation because it has no relational `ORDER BY` expression that can reproduce the requested sequence.
