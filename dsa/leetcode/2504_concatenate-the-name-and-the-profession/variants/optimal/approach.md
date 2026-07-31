## General

**Build the required display value.** Select `person_id` unchanged. For the second column, concatenate the complete `name`, an opening parenthesis, the first character of `profession`, and a closing parenthesis. Alias that expression as `name`, matching the required output schema. Keeping the punctuation inside the concatenation ensures there is no inserted whitespace. The accepted MySQL artifact uses `CONCAT` with `LEFT`; the app-local SQLite artifact expresses the same operation with `||` and `SUBSTR`.

**Apply the required row order.** Sort the projected rows with `ORDER BY person_id DESC`. Since `person_id` is the primary key, every row has a distinct ordering key and the descending result is deterministic.

Every input row is projected exactly once. `LEFT(profession, 1)` produces the requested profession initial for each allowed enum value, so the concatenated text is correct; the final ordering clause then places all output rows in the required sequence.

## Complexity detail

Let $r$ be the number of rows in `Person`. Reading and formatting the rows costs $O(r)$ work. Ordering arbitrary distinct identifiers costs $O(r\log r)$ in the comparison model and dominates the query, while materializing the ordered result requires $O(r)$ space. A database may use a primary-key index to stream rows in descending order and improve the concrete execution to $O(r)$ time beyond this conservative bound.

## Alternatives and edge cases

- **`SUBSTRING(profession, 1, 1)`:** This is equivalent to `LEFT(profession, 1)` in MySQL but is more verbose for a prefix of length one.
- **Separate punctuation columns:** Returning the name, initial, and parentheses separately violates the required two-column schema; they must form one aliased value.
- **Inserted space:** `CONCAT(name, ' (', ...)` is incorrect because the contract forbids whitespace between the name and opening parenthesis.
- **Profession abbreviation:** Only the first letter belongs inside the parentheses, not the complete profession.
- **Names containing spaces:** Preserve the name exactly; only the boundary between the name and `(` must have no added whitespace.
- **Ordering direction:** Omitting `DESC` or relying on storage order can return the correct values in the wrong sequence.
