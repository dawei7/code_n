## General

**Begin with books so zero-sale books survive**

The query starts from `Books` and uses a `LEFT JOIN Orders USING (book_id)`. This direction matters. A book with no matching order must still be considered, because zero sales is less than ten. An inner join would delete that book before aggregation.

For a book without orders, the joined order columns are null. The later conditional aggregate converts nonqualifying rows to zero, allowing the book’s sales total to be treated as zero.

**Apply the protected query’s release cutoff**

The `WHERE` clause keeps rows satisfying `available_from < '2019-05-23'`. Because this predicate references only the Books side, it safely filters book eligibility without turning the left join into an inner join.

The strict operator is an exact detail of the protected SQL: a book first available on May 23 is excluded, while one available on May 22 is included. The local Reference contract describes old-enough books with `available_from <= '2019-05-23'`, so that boundary is broader by one date. To implement that written boundary literally, the operator would need to be `<=`.

**Aggregate quantities per book**

`GROUP BY 1` groups by the first selected expression, `book_id`. Since `book_id` is the Books primary key, one group corresponds to one book and determines one `name`. At most one result row is emitted for each qualifying book.

The conditional expression `IF(dispatch_date >= '2018-06-23', quantity, 0)` contributes an order’s quantity when its dispatch date is on or after the lower boundary, and zero otherwise. `SUM` then totals those contributions across the book’s joined order rows.

For a book with no orders, `dispatch_date` is null. The comparison is not true, so `IF` chooses zero. The aggregate receives a numeric zero rather than only nulls, and the book can pass the threshold.

**Use a strict sales threshold**

`HAVING ... < 10` applies after grouping because it tests an aggregate. Totals zero through nine qualify; a total exactly ten does not. Quantities across multiple orders are summed, so three orders of two copies each count as six rather than three orders.

The result order is unrestricted, so no sorting clause is required.

**Understand the exact date-window assumption**

The protected query checks only `dispatch_date >= '2018-06-23'`. It does not explicitly require `dispatch_date <= '2019-06-23'`. It therefore matches a closed last-year window only if the data contains no orders after the assumed “today” date. Under that source-domain assumption, the missing upper predicate changes nothing.

The local Reference contract explicitly states the closed interval from June 23, 2018 through June 23, 2019. For arbitrary data that may contain future orders, an exact implementation should use `dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'` inside the conditional. This distinction is material: the approach should explain what the shipped query proves rather than silently attributing a predicate it does not contain.

Subject to its strict release cutoff and no-future-order assumption, the left join preserves every eligible book, conditional summation computes its relevant sales including zero, and the `HAVING` test returns exactly those below ten.

## Complexity detail

Let $B$ be the number of Books rows and $O$ the number of Orders rows. A general sort-based join and grouping plan can take $O((B+O)\log(B+O))$ time, matching the manifest. Indexed lookup, hashing, or streaming aggregation may improve the practical plan.

A conservative database plan may materialize joined rows and grouping state proportional to $B+O$, giving $O(B+O)$ space. With an index on `Orders.book_id` and streaming aggregation, working memory can be lower, but SQL does not force one physical execution strategy.

The output has at most $B$ rows because book ID is unique and grouping emits one row per book.

## Alternatives and edge cases

- **Preaggregate the date window:** Group qualifying Orders by `book_id` first, then left join those totals to eligible Books and use `COALESCE(total, 0) < 10`. This often makes the zero-sale logic especially clear.
- **Correlated subquery:** For each book, compute the sum of its in-window orders. With an appropriate index this can be efficient, but the grouped left join is usually easier to inspect.
- **`NOT EXISTS` with grouped orders:** Exclude books whose in-window quantity reaches ten. This is possible but less direct than comparing an aggregate total.
- **Inner join:** Incorrectly removes books with zero relevant orders, even though they should qualify when old enough.
- **Date predicate in `WHERE` on Orders:** This would reject null-extended left-join rows and again lose books with no matching order unless the condition is moved into `ON` or the aggregate.
- **Exactly ten copies:** The strict `< 10` comparison excludes the book.
- **No orders:** The null joined row contributes zero through `IF`, so the book passes the sales threshold if it passes the release cutoff.
- **Only old orders:** Orders before June 23, 2018 contribute zero and do not prevent qualification.
- **Future orders:** The exact query counts them because it lacks an upper bound. Adding the closed-window upper predicate is necessary if such rows are possible.
- **Release on May 23, 2019:** The exact query excludes it because it uses `<`; the local Reference’s `<=` statement would include it.
- **Duplicate book names:** Grouping by primary-key book ID keeps distinct books separate even when names match.
- **Any result order:** Omitting `ORDER BY` is correct and avoids unnecessary sorting solely for presentation.
