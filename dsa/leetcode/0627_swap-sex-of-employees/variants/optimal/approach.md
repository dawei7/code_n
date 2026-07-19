## General
**Map both legal values in one expression**

Run one `UPDATE` over `Salary`. A `CASE` expression returns `f` when the current value is `m` and returns `m` otherwise; the schema guarantees that the only alternative is `f`.

**Rely on row-local assignment semantics**

Each row's new value is computed from that row's original `sex` value during the statement. Updating one employee does not become input to another employee's expression, so every row flips exactly once.

**Why no other data changes**

The `SET` clause assigns only the `sex` column and the statement has no filtering predicate, so all rows participate while `id`, `name`, and `salary` are untouched. The conditional mapping is an involution: applying it once sends each allowed value to precisely its opposite.

## Complexity detail
For `R` employee rows, the update reads and writes each row once, giving $O(R)$ time. The conditional expression uses constant state per row and $O(1)$ auxiliary space beyond database transaction storage.

## Alternatives and edge cases
- **String replacement trick:** `REPLACE('fm', sex, '')` returns the opposite one-character value, but a `CASE` states the domain mapping more clearly.
- **Arithmetic or character-code mapping:** transform the two character codes algebraically; it is compact but obscure and encoding-dependent.
- **Two sequential updates:** changing `m` to `f` and then `f` to `m` flips the first group twice unless an invalid temporary marker is introduced, and it violates the one-statement requirement.
- A table containing only one sex still updates every row.
- Duplicate names or salaries do not affect row-local mutation.
- Input row order is irrelevant to the update.
- The schema's two-value constraint makes the `ELSE 'm'` branch exact.
