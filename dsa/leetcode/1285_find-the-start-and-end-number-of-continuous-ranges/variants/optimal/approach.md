## General

**Derive an island key from two synchronized sequences**

Sort identifiers conceptually by `log_id` and assign `ROW_NUMBER()` values beginning at one. Within a continuous range, both `log_id` and the row number increase by one at each row, so their difference remains constant. When an identifier is missing, `log_id` jumps by more than the row number and the difference increases. The source guarantee that `log_id` is unique is essential: every row number advances exactly once for one distinct identifier.

Compute `log_id - CAST(ROW_NUMBER() OVER (ORDER BY log_id) AS SIGNED)` as `range_key`. The signed cast matters in MySQL because `ROW_NUMBER()` is unsigned; without it, a negative difference can become an out-of-range unsigned result. Group rows by that key, take `MIN(log_id)` and `MAX(log_id)`, and order the resulting ranges by their starts.

**Why one key is exactly one maximal range**

Every consecutive step changes both terms by one, leaving `range_key` unchanged. At a gap of size at least two, `log_id` increases by more than the row number, so the key strictly increases and never returns to an earlier value. Each group is therefore one complete maximal range, and no group can cross a missing identifier. Its minimum and maximum are exactly the required endpoints.

## Complexity detail

For $n$ input rows, the window ordering costs $O(n \log n)$ in the general database execution model. Computing keys and aggregating the groups is linear after ordering. The ordered window and grouped intermediate relation may require $O(n)$ working space; the final result contains $r$ rows.

## Alternatives and edge cases

- **Start/end anti-joins:** Identify values without predecessors and values without successors, then pair each start with its next end. This is valid but can create an expensive start-by-end join without careful indexing or window functions.
- **User variables:** MySQL session variables can track the preceding identifier, but their evaluation order is less portable and easier to misuse than a window expression.
- **Empty table:** The CTE and aggregation produce no groups, so the result is empty.
- **Singleton range:** An identifier with neither consecutive neighbor must produce equal `start_id` and `end_id`.
- **Multiple gaps:** Every missing integer terminates the preceding maximal range, even when the next identifier is much larger.
- **Signed identifiers:** The difference key works across negative values and zero because it depends only on adjacent differences. Cast MySQL's unsigned row number to `SIGNED` before subtraction so a negative key remains legal.
- **Input order:** Table rows have no inherent order; the window and final result must both specify ordering explicitly.
