## General

**Pair each current day with the exact calendar day before it**

The query reads `Weather` twice through aliases `w1` and `w2`. Alias `w1`
represents the candidate current day whose ID might be returned. Alias `w2`
represents that candidate's possible yesterday row.

This self-join is needed because current and previous temperatures live in two
different table rows. Joining places both values into one logical result row so
they can be compared.

**Use date arithmetic rather than row order**

`DATEDIFF(w1.recordDate, w2.recordDate) = 1` requires `w1` to be exactly one
calendar day after `w2`. In MySQL, `DATEDIFF(later, earlier)` returns their day
difference, so argument order matters. Reversing the arguments would identify
tomorrow relative to `w1` instead of yesterday.

The condition does not mean “the previous row” and does not depend on IDs being
consecutive. IDs are merely unique labels; dates determine chronology. It also
does not compare with the nearest earlier available record if a date is
missing. A gap of two or more days fails the equality and correctly provides no
yesterday comparison.

**Require a strict temperature increase**

The second join predicate is `w1.temperature > w2.temperature`. Equality is not
a rise, so it must not use `>=`. A lower current temperature also fails.

Both date adjacency and temperature increase appear in the `ON` clause. Since
this is an inner join, placing the temperature predicate in a `WHERE` clause
would produce the same result. Keeping both pair-validity conditions together
makes the meaning of a qualifying pair explicit.

**Why date uniqueness simplifies cardinality**

The Reference guarantees no two different rows have the same `recordDate`.
Therefore a current day can match at most one yesterday row. The self-join does
not produce duplicate copies of a current ID through several observations for
the same prior date.

If duplicate dates were allowed, the query could compare one current record
with several prior records and potentially emit the same ID multiple times.
The stored query correctly relies on the uniqueness guarantee and needs no
`DISTINCT`.

**Trace the example**

January 1 has no December 31 row, so it forms no adjacent-date pair. January 2
pairs with January 1; temperature 25 is greater than 10, so ID 2 is selected.

January 3 pairs with January 2, but 20 is not greater than 25, so ID 3 is not
selected. January 4 pairs with January 3, and 30 is greater than 20, so ID 4 is
selected.

The output may list IDs 2 and 4 in either order because the Reference explicitly
allows any result order.

**Why every returned ID is valid**

Any joined row satisfies a one-day date difference, so `w2` is the calendar day
immediately before `w1`. It also satisfies the strict temperature comparison,
so `w1` is warmer than yesterday. Selecting `w1.id` therefore never returns an
invalid day.

Conversely, suppose a represented date is warmer than its represented
yesterday. The unique yesterday row provides a `w2` whose date difference is
one and whose temperature is lower. Both join predicates succeed, and the
current row's ID is returned. Thus every qualifying date is found.

**Missing yesterday means no answer for that date**

An inner join removes a current row that has no date exactly one day earlier.
This is correct: without a yesterday record, the table provides no temperature
against which to prove a rise. Comparing with an older record would change the
meaning from “yesterday” to “previous observation.”

This distinction is a common mistake in window-function solutions. A `LAG`
approach must check both the previous temperature and that the lagged date is
exactly one day earlier.

**Column naming and null considerations**

The projection `w1.id` naturally has output heading `id`, matching the local
contract. No alias is needed.

The Reference describes concrete dates and temperatures but does not list
explicit null constraints. SQL comparisons involving null yield unknown, so a
null date cannot join and a null temperature cannot pass `>`. Such rows are
omitted, a reasonable result when a rise cannot be established, though a
broader nullable domain should state that policy explicitly.

**Manifest summary versus exact expression**

The manifest summary says each previous date is transformed once and direct
equality finds the following day. The exact source instead applies `DATEDIFF`
to candidate row pairs. An optimizer may transform the condition, but the SQL
text does not explicitly materialize `DATE_ADD(w2.recordDate, INTERVAL 1 DAY)`
once. The approach documentation follows the actual `DATEDIFF` self-join.

## Complexity detail

Let $n$ be the number of Weather rows. A naive self-join evaluates up to $n^2$
row pairs and applies the two predicates, giving the manifest time bound
$O(n^2)$. Applying a function across both date columns can make ordinary index
lookup less direct than equality on a precomputed date.

The manifest records $O(n)$ space, covering join structures or materialized
rows. A nested-loop plan may use less auxiliary memory, while a hash-like
transformation may use linear memory. SQL execution cost is plan and index
dependent; the conservative pairwise time bound remains honest for the exact
query.

## Alternatives and edge cases

- **Date-add equality join:** Join `w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)`; this states the transformed-yesterday relation directly.
- **`LAG()` window function:** Sort by date, retrieve prior date and temperature, then verify the date gap is exactly one day.
- **Correlated subquery:** Look up temperature at `DATE_SUB(w1.recordDate, INTERVAL 1 DAY)` for each current row.
- **Pandas shifted merge:** Add one day to a copied date column and merge, as the local editorial describes.
- **Missing calendar day:** Do not compare with the nearest older observation.
- **Equal temperature:** Strict `>` rejects it.
- **Duplicate dates:** Excluded by contract; otherwise duplicate output or ambiguous comparison could occur.
- **First represented date:** Qualifies only if its actual yesterday is also represented.
- **Null data:** Cannot establish both predicates and is omitted by SQL three-valued logic.
- **Any order:** No `ORDER BY` is required.
