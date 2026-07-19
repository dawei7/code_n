## General
**Classify each user-date once.** Group by `(user_id, spend_date)`. Sum all amounts for that user on that date. A group containing two platform rows is `both`; because of the composite primary key and two-value platform domain, a one-row group is classified by its sole platform. This avoids counting a user twice in the `both` category while still adding both purchase amounts.

**Build the complete reporting grid.** Extract distinct dates and cross join them with an explicit three-row relation containing `desktop`, `mobile`, and `both`. This produces every required `(spend_date, platform)` pair even when no classified user-date belongs to it.

**Aggregate through a left join.** Left join the classified user-date rows onto the grid. For each grid cell, `SUM(amount)` gives the total spending and `COUNT(user_id)` gives the number of classified users. `COUNT` naturally returns zero for an unmatched cell, while `COALESCE` converts the unmatched sum from `NULL` to `0`. Every source user-date joins exactly once, so totals are neither omitted nor duplicated.

## Complexity detail
Grouping the $R$ purchase rows by user and date and grouping the joined result may require sorting, giving a conservative $O(R \log R)$ logical time bound. The classified user-date relation, distinct dates, and grouping state require $O(R)$ space. Physical database costs depend on indexes and the chosen execution plan.

## Alternatives and edge cases
- **Three `UNION ALL` branches:** Separate queries for mobile-only, desktop-only, and both can work, but each branch repeats classification logic and still needs explicit zero rows for missing categories.
- **Correlated counterpart lookup:** Testing for an opposite-platform row separately for every purchase is correct, but without a supporting index it can repeatedly scan `Spending` and approach $O(R^2)$.
- **Both-platform user:** Add both row amounts but count the user once in `total_users`.
- **Missing category:** The date-platform grid must retain a row with `total_amount = 0` and `total_users = 0`.
- **Same user on different dates:** Platform classification is independent for each date; activity on one date cannot change another date's category.
