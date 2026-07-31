## General

**Materialize the required output dimensions first.** The report always contains the four Fridays November 3, 10, 17, and 24, crossed with the two requested memberships `Premium` and `VIP`. Two small CTEs enumerate those dimensions, and their cross join creates the eight output keys before any purchase is considered. This is what makes a missing Friday-membership total appear as zero instead of disappearing.

**Attach members and only the matching Friday purchases.** Left join `Users` by membership so that each grid row receives exactly the users in its category. Then left join `Purchases` by both `user_id` and the exact Friday date. The date predicate belongs in the join condition: putting it in a `WHERE` clause would reject null-extended rows and undo the required zero fill. `Standard` users never match either dimension row and therefore cannot contribute.

Group by `week_of_month` and `membership`, sum `amount_spend`, and convert a null sum to zero with `COALESCE`. Every qualifying purchase joins the unique user row and exactly one Friday dimension row, so it contributes once to the correct total. Every required dimension pair existed before the left joins and therefore survives even without a contribution. Ordering by the two displayed keys produces the required ascending result.

## Complexity detail

Let $u$ and $p$ be the row counts of `Users` and `Purchases`. The Friday and membership CTEs contain fixed numbers of rows. With the table keys and normal join indexing, the query processes the relevant user and purchase rows in $O(u+p)$ time. A general database execution may materialize joins, grouping, or indexes using $O(u+p)$ working space; the final grouped result itself always has eight rows.

## Alternatives and edge cases

- **Aggregate purchases before building the grid:** A grouped fact query is useful, but it must still be outer-joined to all eight Friday-membership pairs or missing totals vanish.
- **Conditional aggregation:** Four Friday expressions and two membership expressions can compute the totals, but reshaping them into eight ordered rows is more repetitive than the dimension-grid join.
- **Recursive date generation:** Advancing November 3 by seven days is valid, but four explicit dates make the bounded calendar contract easier to audit.
- **Use `WEEK()` or day-of-month arithmetic:** Calendar week functions depend on modes and year boundaries; exact November dates avoid those semantics entirely.
- **Date predicate in `WHERE`:** This turns the purchase outer join into an effective inner filter and drops zero rows.
- **Non-Friday purchases:** They match none of the four date keys and do not affect a total.
- **Standard members:** They are outside the two-row membership dimension and must be excluded.
- **Multiple purchases:** Every qualifying row contributes its full `amount_spend`, including several purchases by one user on the same Friday.
- **No qualifying users or purchases:** The cross-joined dimension rows remain and `COALESCE` reports all totals as zero.
- **Ordering:** Sort by numeric `week_of_month` first and membership text second, both ascending.
