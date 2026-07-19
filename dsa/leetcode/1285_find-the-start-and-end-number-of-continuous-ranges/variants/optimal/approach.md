## General
**A stable key for one continuous run.** Sort identifiers conceptually by `log_id` and assign `ROW_NUMBER()` values beginning at one. Within a continuous range, both `log_id` and the row number increase by one at each row, so their difference remains constant. When an identifier is missing, `log_id` jumps by more than the row number and the difference changes.

Compute `log_id - ROW_NUMBER() OVER (ORDER BY log_id)` as a range key. Group rows by that key, take `MIN(log_id)` and `MAX(log_id)`, and order the resulting ranges by their starts. Every continuous run has one constant key. Conversely, two adjacent sorted rows with the same key must differ by exactly one, so a group cannot cross a gap. The grouped minima and maxima are therefore precisely the maximal ranges.

## Complexity detail
For $n$ input rows, the window ordering costs $O(n \log n)$ in the general database execution model. Computing keys and aggregating the groups is linear after ordering. The ordered window and grouped intermediate relation may require $O(n)$ working space; the final result contains $r$ rows.

## Alternatives and edge cases
- **Start/end anti-joins:** Identify values without predecessors and values without successors, then pair each start with its next end. This is valid but can create an expensive start-by-end join without careful indexing or window functions.
- **User variables:** MySQL session variables can track the preceding identifier, but their evaluation order is less portable and easier to misuse than a window expression.
- **Singleton range:** An identifier with neither consecutive neighbor must produce equal `start_id` and `end_id`.
- **Multiple gaps:** Every missing integer terminates the preceding maximal range, even when the next identifier is much larger.
- **Input order:** Table rows have no inherent order; the window and final result must both specify ordering explicitly.
