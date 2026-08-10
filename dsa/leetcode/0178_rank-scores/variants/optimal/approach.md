## General

**Use dense rank because ties must not create gaps**

The required sequence is a dense ranking:

- the highest distinct score receives rank one;
- equal scores receive the same rank;
- the next lower distinct score receives the next consecutive integer.

`DENSE_RANK()` implements exactly these rules. It differs from `ROW_NUMBER`,
which would give tied rows different numbers, and from `RANK`, which would skip
numbers after a tie.

The query applies the function as a window expression so that every input game
row remains in the output. A `GROUP BY score` would collapse ties into one row,
violating the requirement to retain every score row.

**Order the ranking window by score descending**

The window clause is:

`OVER (ORDER BY score DESC)`.

This tells `DENSE_RANK` to process higher score values before lower ones. Rows
with equal `score` are peers and receive the same rank. Whenever the score
changes to a lower distinct value, the rank increases by one.

No `PARTITION BY` appears, so all rows belong to one global competition. Adding
a partition would restart ranking separately for each partition and answer a
different question.

**Trace the sample ranks**

The highest distinct value is 4.00. Both rows with that value are peers and
receive rank one.

The next lower value is 3.85, so it receives rank two. The two rows at 3.65
share rank three. Finally, 3.50 receives rank four.

The rank after the two 4.00 rows is two rather than three. That no-gap behavior
is precisely why dense rank is selected.

**Project one result row per source row**

The `SELECT` list contains `score` and the window result aliased as `'rank'`.
Window functions calculate over related rows but do not combine them. If the
input contains six rows, the query returns six rows.

The alias matches the requested second column. In MySQL, single quotes can be
accepted for aliases in this position, though backticks or an unquoted
identifier are often clearer because single quotes normally denote string
literals.

The primary key `id` is not projected. It makes source rows unique but is not
part of the requested output.

No input row is otherwise filtered or aggregated away.

**Why the numeric rank is correct**

For any score value $s$, dense descending rank equals:

$$
1+\#\{\text{distinct score values greater than }s\}.
$$

`DENSE_RANK` computes this relationship internally. Equal rows have the same
set of greater distinct scores, so they share a rank. Moving to the next lower
distinct value adds exactly one new greater level, so ranks remain consecutive.

This proves both tie equality and absence of holes.

**Material final-order omission**

The Reference requires the returned table to be ordered by `score` descending.
The `ORDER BY` inside `OVER (...)` defines the order used to calculate the
window function; SQL does not generally promise that it also orders the final
result rows.

Many engines happen to emit rows in the same order because sorting is useful
for evaluating the window, but that is an execution-plan side effect rather
than a result contract.

To guarantee compliance, the query needs a final clause:

`ORDER BY score DESC`.

As stored, the ranks are correct, but output order is not formally guaranteed.

**Version and null considerations**

`DENSE_RANK` requires window-function support, available in MySQL 8.0 and
later. Older MySQL versions need a correlated subquery, self-join, or carefully
designed alternative.

If `score` can be null, MySQL's descending ordering places null after numeric
values and dense-ranks it as another peer group. The schema describes game
scores as decimal values; a production contract should state whether null
scores exist and whether they should be ranked.

## Complexity detail

Let $n$ be the score-row count. A typical window plan sorts rows by score in
$O(n\log n)$ time and uses $O(n)$ working space for sorting or window
processing. These bounds match the manifest.

An index ordered by descending score may reduce or avoid explicit sorting, and
actual memory can spill to disk. SQL complexity depends on the optimizer and
physical plan; the manifest describes a conventional sort-based execution.

## Alternatives and edge cases

- **Correlated distinct count:** Compute one plus the number of distinct greater scores for each row. It is clear mathematically but can be $O(n^2)$.
- **Self-join and grouping:** Join each row with scores greater than or equal to it, then count distinct joined values; also potentially quadratic.
- **`RANK()`:** Incorrect because ties create gaps in later ranks.
- **`ROW_NUMBER()`:** Incorrect because tied rows receive different numbers.
- **All scores equal:** Every row receives rank one.
- **Repeated ties:** Every peer is retained and shares one dense rank.
- **One row:** Receives rank one.
- **Required row order:** Add an outer `ORDER BY score DESC`; window ordering alone is insufficient.
- **MySQL version:** Window functions require MySQL 8.0 or newer.
- **Alias syntax:** `'rank'` works in MySQL's select alias context but an identifier quote is clearer.
