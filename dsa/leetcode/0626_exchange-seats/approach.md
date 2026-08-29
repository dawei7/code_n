## General

**Keep each output seat ID and fetch the student from its partner seat.** The result can be viewed in two equivalent ways: change every student's ID, or keep the ordered ID rows and replace each row's student with the student from the paired ID. The exact query uses the second view.

`Seat AS s1` is the output-seat side. The query always selects `s1.id`, so every original seat ID appears exactly once. `Seat AS s2` is the partner side. A self-join calculates which partner ID should provide the student for each `s1` row.

**Derive the partner transformation.** Consecutive pairs are `(1,2)`, `(3,4)`, `(5,6)`, and so on. The required mapping is:

- odd ID $j$ maps to $j+1$;
- even ID $j$ maps to $j-1$.

The join expresses both cases with

`(s1.id + 1) ^ 1 - 1`.

Here `^` is bitwise exclusive OR in MySQL. In the intended precedence, XOR is applied before the final subtraction; a fully parenthesized reading is `((s1.id + 1) ^ 1) - 1`.

To see why it works, examine the last binary bit.

- If `id` is odd, `id + 1` is even and ends in bit 0. XOR with 1 flips that bit to 1, increasing the value by 1. Subtracting 1 returns `id + 1`, the next seat.
- If `id` is even, `id + 1` is odd and ends in bit 1. XOR with 1 clears that bit, decreasing `id + 1` by 1 back to `id`. The final subtraction produces `id - 1`, the preceding seat.

For ID 1, the expression is `((2) ^ 1) - 1 = 3 - 1 = 2`. For ID 2, it is `((3) ^ 1) - 1 = 2 - 1 = 1`. Thus the two rows point to each other.

**Why a left join is necessary.** The IDs start at 1 and are continuous. Every complete odd-even pair therefore has both partner rows. If the row count is odd, however, the last ID is odd and the transformation requests the nonexistent next ID. An inner join would delete that final output row, violating the requirement that its seat remain unchanged.

The `LEFT JOIN` preserves every `s1` row. For the unmatched final seat, all `s2` columns are `NULL`.

**Use `COALESCE` to keep the unmatched final student.** The projected student is

`COALESCE(s2.student, s1.student)`.

For a complete pair, `s2.student` is present and becomes the student displayed at `s1.id`. For the unmatched final odd seat, `s2.student` is null because no partner row exists, so `COALESCE` falls back to the original `s1.student`. This implements the “last student is not swapped” rule without separately counting rows.

For the five-row sample, output ID 1 joins ID 2 and displays Doris; output ID 2 joins ID 1 and displays Abbot. IDs 3 and 4 exchange in the same way. ID 5 requests partner 6, the left join finds none, and the fallback retains Jeames.

**Why every row is correct.** Fix an output ID `j`. If `j` belongs to a complete pair, the bit expression computes exactly the other member of that pair. Continuity and primary-key uniqueness guarantee exactly one matching partner row, so the output receives that student's name. If `j` is the final unpaired odd ID, its computed partner is absent; the left join preserves `j` and `COALESCE` returns its original student. Those are precisely the two cases in the specification.

`ORDER BY 1` sorts by the first selected column, `s1.id`, in ascending order by default. This returns the required ID order. Writing `ORDER BY s1.id` would be clearer, but the positional form is valid.

**The schema guarantees are doing real work.** Continuous IDs make “next” and “previous” correspond to an existing consecutive seat except at the single allowed end case. The primary key prevents duplicate partner matches. If IDs had gaps, an interior odd ID could incorrectly be treated like an unmatched final seat and keep its student.

## Complexity detail

Let $R$ be the number of rows in `Seat`. The query scans $R$ output-side rows. Looking up each computed partner through the primary-key index can cost $O(\log R)$ per lookup in a general tree index, and the final ordering can cost $O(R\log R)$. The manifest's conservative total time bound is therefore $O(R\log R)$.

An optimizer may perform indexed lookups and emit rows already ordered by `s1.id`, reducing practical work, or use a hash join with expected linear matching. The logical result remains one row per input seat.

Join and sorting structures may use $O(R)$ auxiliary storage, matching the manifest. The parity transformation and `COALESCE` need only constant state per row.

## Alternatives and edge cases

- **`CASE` on odd and even IDs:** Count rows, map complete odd IDs to `id + 1`, even IDs to `id - 1`, and retain the final odd ID. This is more verbose but avoids bit manipulation.
- **Window functions:** Use `LEAD(student)` for odd rows and `LAG(student)` for even rows after ordering by ID. This states the neighboring-row intent clearly but still needs the last-row fallback.
- **Fully parenthesized bit expression:** Write `((s1.id + 1) ^ 1) - 1` to make precedence explicit.
- **Even number of rows:** Every ID has a partner, so `COALESCE` always chooses `s2.student`.
- **Odd number of rows:** Only the final odd ID lacks a partner and retains its original student.
- **One row:** Its computed partner is ID 2, which is absent, so the sole student remains unchanged.
- **Continuous-ID guarantee:** Without it, missing interior partners would silently trigger the fallback and no longer represent consecutive-seat swapping.
- **Primary-key guarantee:** It ensures each computed partner contributes at most one joined row.
- **Nullable student names:** If a real partner row existed with `student = NULL`, `COALESCE` would fall back to the wrong original name. The intended challenge data treats student names as present; otherwise partner existence should be tested separately.
- **`ORDER BY 1`:** It depends on the first projection remaining `s1.id`. Naming the column is more maintainable.
- **Dialect portability:** `^` is bitwise XOR in MySQL but can mean something else elsewhere; a `CASE` or modulo expression is easier to port.
