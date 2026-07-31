## General

The eligibility rule depends only on the three newest reviews for each employee. Assign `ROW_NUMBER()` inside each employee partition, ordering review dates from newest to oldest. Rank `1` is the latest rating, rank `2` is the middle rating, and rank `3` is the earliest rating in the relevant window. Reviews with larger ranks can be discarded immediately.

Join those ranked rows to `employees` and group by employee. Conditional aggregates place each of the three ratings into its chronological role without creating three separate joins. `COUNT(*) = 3` enforces the minimum history requirement after the rank filter. Because the ranks run newest to oldest, strict chronological improvement is exactly `rating(rank 1) > rating(rank 2) > rating(rank 3)`.

For each surviving group, subtract the rank-3 rating from the rank-1 rating to obtain `improvement_score`. The final order first places larger improvements ahead and then compares names alphabetically. Each review receives one rank and contributes to at most one employee group, so older history cannot accidentally affect the result.

## Complexity detail

Let $R$ be the number of review rows and $E$ the number of employees. Without assuming a supporting index, partitioned ordering costs $O(R\log R)$ in the comparison model. Aggregation is linear after ranking, and ordering at most $E$ result rows costs $O(E\log E)$. Total time is therefore $O(R\log R+E\log E)$ with $O(R+E)$ working space. A database may exploit an index on `(employee_id, review_date)` to reduce sorting work.

The benchmark uses $E=S$ employees and $R=4S$ reviews, with every employee qualifying. The accepted window query ranks the review relation once. The calibrated alternative evaluates repeated correlated counts and rating lookups against the full review table for every employee, creating quadratic rescanning without appropriate indexes.

## Alternatives and edge cases

- **Three self-joins:** Joining review rows into chronological triples can generate many obsolete combinations before the latest-three condition is established.
- **Correlated rating lookups:** Separate subqueries for each rank are readable but may rescan the review table repeatedly for every employee.
- **Aggregate all history:** Comparing global minimum and maximum ratings is wrong because only the latest three reviews matter and their order must be preserved.
- **Exactly three reviews:** Such an employee is eligible when all three ratings rise strictly; no older row is required.
- **Fewer than three reviews:** The employee must be excluded even if every available rating improves.
- **Plateau:** Equal consecutive ratings violate strict improvement.
- **Older decline:** A decline outside the latest three does not affect eligibility.
- **Ordering tie:** Equal improvement scores are resolved by ascending employee name.
