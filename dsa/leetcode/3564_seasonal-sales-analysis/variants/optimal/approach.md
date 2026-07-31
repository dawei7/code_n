## General

Join each sale to its product so that the sale's quantity, price, and date are available beside the product category. Convert the month into one of the four named seasons. December must wrap around to Winter together with January and February; the other seasons are consecutive three-month blocks.

Group the joined rows by season and category. Summing `quantity` produces `total_quantity`, while summing `quantity * price` produces `total_revenue`. This grouping deliberately combines products from the same category and combines matching seasons across calendar years.

Apply `ROW_NUMBER()` independently within each season. Order candidate categories by total quantity descending, total revenue descending, and category ascending. Those keys exactly encode the contract's priority rules, so row number one is the unique required category for that season. Filtering to that row and sorting the four possible season names completes the result.

## Complexity detail

Let $S$, $P$, and $G$ have the meanings defined in the function contract. Under a comparison-based database plan, joining and grouping cost $O(S\log S + P\log P)$, and ranking the grouped relation costs $O(G\log G)$. The total time is $O(S\log S + P\log P + G\log G)$ and materialized working space is $O(S + P + G)$. Hash joins and hash aggregation can make their corresponding stages expected-linear before the ranking sort.

The benchmark size is $S$. It grows the number of categories with the sales relation, so $G=\Theta(S)$. The accepted structure aggregates the joined relation once, whereas the calibrated slower query recomputes each category total by rescanning sales and therefore performs quadratic work.

## Alternatives and edge cases

- **Aggregate once, then anti-join:** A `NOT EXISTS` comparison against better groups can select winners without a window function, but a naive plan may compare every pair of category groups within a season.
- **Correlated totals per sale:** Recomputing quantity and revenue for every candidate is correct after deduplication, but repeatedly scans the sales relation and can become quadratic.
- **December boundary:** Month 12 belongs to Winter, not to a separate block after Fall.
- **Multiple calendar years:** January and December rows from different years still contribute to the same `Winter` aggregate.
- **Several products in one category:** Their sales must be combined before categories are ranked.
- **Quantity tie:** Higher total revenue wins even when its category name is lexicographically larger.
- **Complete tie:** The lexicographically smaller category wins when quantity and revenue are both equal.
- **Missing season:** A season with no sales contributes no output row.
- **Final ordering:** The result is sorted by the season strings, yielding Fall, Spring, Summer, then Winter when all four are present.
