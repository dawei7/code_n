## General

**Rank each call direction independently.** Joining `Calls` to `Contacts` supplies the first name required in the output. A `ROW_NUMBER()` window partitions those joined rows by `type`, so incoming and outgoing calls receive separate rankings. Within each partition, descending duration puts the longest call first. Descending `first_name` matches the requested secondary ordering when durations tie, and descending `contact_id` gives otherwise indistinguishable name-and-duration ties a stable final choice.

**Filter only after assigning positions.** Keeping window positions 1 through 3 selects at most three calls from each direction. A global limit would be wrong because one call type could consume every result slot. Once the two per-type selections are combined, the outer `ORDER BY` applies the required descending order by type, raw duration, and first name.

**Format without changing the ranking key.** Ranking and final sorting use the integer duration. Only the selected output value is converted to `HH:MM:SS`; sorting a presentation string instead of the source seconds would mix display concerns into the selection logic. The app-local SQLite query builds the same fixed-width string with integer division and `printf`, while the separately verified MySQL source uses `TIME_FORMAT(SEC_TO_TIME(...))`.

Every call is assigned exactly one position within its own type, in the specified longest-first order. Therefore positions at most 3 are precisely that type's three longest rows, or all its rows when fewer than three exist. The final sort does not change membership, so the query returns exactly the required calls in the required presentation order.

## Complexity detail

Let $c$ be the number of rows in `Calls`. The indexed contact join is linear under standard database indexing, while the window operation sorts the call rows within the two type partitions and costs $O(c\log c)$ time in the worst case. The ranked intermediate relation and sort state require $O(c)$ auxiliary space. Formatting the at most six retained rows is constant additional work.

## Alternatives and edge cases

- **Two ordered queries with `UNION ALL`:** Taking three incoming rows and three outgoing rows separately is workable, but duplicates the selection logic and still needs a final global sort.
- **Correlated rank counting:** Counting how many same-type calls precede every row produces the correct top three, but repeatedly scans the call table and grows quadratically.
- **`RANK()` or `DENSE_RANK()`:** These functions may return more than three rows when durations tie; `ROW_NUMBER()` enforces the requested row count.
- **Fewer than three calls of one type:** Every available call from that partition is returned; the other partition is unaffected.
- **Equal durations:** Descending first name resolves the visible tie consistently with the final ordering, with contact id as a stable last tie-breaker.
- **Duration boundaries:** Values such as 59, 60, and 3600 seconds must render as `00:00:59`, `00:01:00`, and `01:00:00` respectively.
- **Contacts without calls:** They never enter the joined ranked relation and therefore produce no result row.
