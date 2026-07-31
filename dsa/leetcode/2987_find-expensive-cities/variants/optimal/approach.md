## General

**Establish the national baseline.** A scalar aggregate over all rows computes
the national average listing price. This is listing-weighted by definition;
averaging city averages instead would incorrectly give cities equal weight
regardless of how many homes they contain.

**Compare grouped city averages.** Group `Listings` by `city` and use `HAVING`
to retain only groups whose `AVG(price)` is strictly greater than the scalar
national average. Project the city name and apply ascending ordering. Every
listing contributes to exactly one city aggregate and to the national
aggregate, so this comparison directly implements the requested condition.

## Complexity detail

Let $R$ be the number of listings. Grouping and ordered output take
$O(R\log R)$ time in the general comparison-based model. The grouped state can
use $O(R)$ space in the worst case.

## Alternatives and edge cases

- **National-average CTE:** Computing the scalar aggregate in a CTE and cross joining it into the grouped query is equivalent.
- **Correlated city averages per row:** This can return the same distinct cities but may rescan a city's rows repeatedly and become quadratic.
- **Average of city averages:** This is wrong when cities contain different numbers of listings.
- **Equality:** The contract says `exceed`, so a city equal to the national average is excluded.
- **Single city:** Its city and national averages are identical, producing an empty result.
- **Output order:** Sort city names ascending after filtering.
