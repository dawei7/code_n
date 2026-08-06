## General
**Keep every book that is at least one month old.** The statement excludes books available for less than one month as of `2019-06-23`. Its one-month boundary is therefore `2019-05-23`, and equality is eligible: filter with `available_from <= '2019-05-23'`.

**Restrict orders in the join condition.** Left join each eligible book to orders dispatched from `2018-06-23` through `2019-06-23`, inclusive. Keeping the date predicate in `ON` rather than `WHERE` preserves books with no matching order.

**Aggregate recent quantities per book.** Group by the book's identifier and name, sum the matched quantities, and replace the null sum for an unmatched book with zero. Retain groups whose total is strictly less than 10. Orders outside the window never enter the aggregate, regardless of their quantity.

The release filter selects exactly the books not excluded by the age rule, including the exact one-month boundary. For each selected book, the restricted left join contains every and only order in the stated year while still producing one null-extended row when there are none. The grouped sum is therefore the required sold-copy total, and the final threshold selects exactly the unpopular books.

## Complexity detail
A standard sort-based join and grouping plan takes $O((B + O) \log(B + O))$ time and $O(B + O)$ working space. Hash joins and hash aggregation can approach $O(B + O)$ expected time. The actual plan depends on the database engine and available indexes.

## Alternatives and edge cases
- **Pre-aggregate recent orders:** Group the one-year orders by `book_id` first and left join those totals to `Books`; this is equally valid and can reduce join rows.
- **Correlated quantity subquery:** Summing `Orders` separately for every book is concise but may require $O(BO)$ work without an index.
- **No recent orders:** The book's one-year total is zero, so `COALESCE` must allow it to qualify.
- **Exactly ten copies:** The book is not unpopular because the threshold is strictly fewer than 10.
- **Release cutoff:** A book available on `2019-05-23` is exactly one month old and remains eligible; only later release dates are excluded.
- **Order-window endpoints:** Orders on both `2018-06-23` and `2019-06-23` count toward the total.
