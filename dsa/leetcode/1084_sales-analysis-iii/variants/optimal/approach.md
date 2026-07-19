## General
**Require a real sale through the join:** Inner-join `Product` with `Sales`. This both supplies each output name and excludes products with no sales, which must not qualify merely because they have no outside-window row.

**Reduce all dates to two boundaries:** Group by the product's identifier and name. All of a product's sale dates lie inside an inclusive interval exactly when its minimum date is at least `2019-01-01` and its maximum date is at most `2019-03-31`.

**Apply inclusive comparisons:** Keep only groups meeting both `HAVING` predicates. Duplicate sales do not change either date boundary, although they remain valid input rows.

Every retained group contains at least one sale because of the inner join, and its minimum and maximum bound every other date within the required quarter. Conversely, if every sale of a product is within the quarter, its minimum and maximum satisfy both predicates, so the product is returned.

## Complexity detail
A hash join can build a $P$-row product lookup and process $R$ sales in expected $O(P+R)$ time. Sort-based grouping and deterministic output ordering can add $O(R\log R)$ time. Join, grouping, and sort state use up to $O(P+R)$ execution space.

## Alternatives and edge cases
- **Conditional outside-date count:** Group sales and require the count of dates outside the quarter to be zero. It is equally valid but expresses a contiguous range less directly than minimum and maximum.
- **Correlated minimum and maximum:** Compute both boundaries separately for each product. It is correct but can repeatedly rescan `Sales` and approach quadratic time.
- **Filter dates before grouping:** It is incorrect because it erases outside-quarter evidence and can admit a product sold both inside and outside the quarter.
- **Boundary dates:** Sales on `2019-01-01` and `2019-03-31` are included.
- **Unsold product:** Exclude it because the product was not sold during the quarter.
- **Duplicate rows:** They do not change qualification.
- **Any outside sale:** A sale before January or after March disqualifies the product even if it also sold inside the quarter.
