## General

**Aggregate every customer once.** Group `restaurant_orders` by `customer_id`. `COUNT(*)` gives all orders, while a conditional `SUM` counts rows whose time component lies in either inclusive peak interval. `COUNT(order_rating)` counts only rated rows because SQL aggregates ignore `NULL`, and `AVG(order_rating)` likewise averages only the rated orders.

Use exact integer comparisons for both percentage thresholds. If $P$ of $T$ orders are in peak hours, the requirement $P/T\ge0.60$ is equivalent to $5P\ge3T$. If $R$ orders are rated, $R/T\ge0.50$ is equivalent to $2R\ge T$. These cross-products avoid allowing display rounding to change eligibility. The minimum-order rule ensures $T>0$, and the rating-completion rule ensures at least one rating before the average comparison is evaluated.

Retain groups with at least three orders, both exact ratio conditions, and raw rated-order average at least 4.0. Project the peak percentage with whole-number rounding and the average rating with two-decimal rounding. Every retained group satisfies all four golden-hour criteria, and every qualifying customer has aggregates that pass these same predicates. The final two-key descending sort establishes the required order, including average-rating ties.

## Complexity detail

Let $R$ be the number of order rows and $C$ the number of customer groups. Under a general comparison-based plan, grouping may cost $O(R\log R)$ and sorting the retained groups costs $O(C\log C)$, for $O(R\log R+C\log C)$ time. A sort-based aggregate may use $O(R+C)$ working space. Hash aggregation or indexes can improve the physical plan, but the query does not assume them.

The benchmark defines size as $C$ and contributes five rows per customer, so $R=5C$. The accepted query aggregates the input once. The calibrated slower control repeats correlated table scans for each outer customer row while returning the same metrics.

## Alternatives and edge cases

- **Rounded ratios in `HAVING`:** Comparing a displayed percentage can admit or reject a boundary incorrectly; cross-multiplication tests the exact fraction.
- **Correlated aggregate subqueries:** They can reproduce the result but rescan the order table repeatedly and can grow quadratically.
- **Unrated orders:** They count in both ratio denominators but not in the rating numerator or average.
- **Exactly 60% peak:** Equality qualifies, so three peak orders out of five must pass.
- **Exactly 50% rated:** Equality also qualifies, so two rated orders out of four pass when the other rules hold.
- **Peak endpoints:** Orders exactly at 11:00, 14:00, 18:00, or 21:00 are inside the inclusive intervals.
- **Percentage formatting:** `peak_hour_percentage` is rounded to a whole number; for example, two peak orders out of three are reported as `67`.
- **Ordering tie:** Equal average ratings are resolved by larger `customer_id` first.
