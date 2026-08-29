## General

**Compare each city with one listing-weighted national mean**

The national average home price is the average over every row in `Listings`:

`SELECT AVG(price) FROM Listings`.

This is not the average of the city averages. Every listing contributes one observation nationally, so a city with many listings contributes proportionally more to the national mean than a city with one listing.

The outer query groups rows by `city` and computes `AVG(price)` for each group. Its `HAVING` clause retains a city only when that group average is strictly greater than the scalar national average.

**Why `HAVING` appears instead of `WHERE`**

`WHERE` filters individual source rows before grouping and cannot directly test `AVG(price)` for a completed city group. `HAVING` is evaluated after grouping and may refer to aggregate expressions. The logical sequence is:

1. read all listing rows;
2. form one group per city;
3. calculate each group’s average;
4. compare that average with the scalar subquery result;
5. keep qualifying groups.

No row-level price threshold is applied. A city may have some cheap listings and still qualify if its overall mean exceeds the national mean.

**The scalar subquery is global**

The inner average has no correlation with the current outer city and no `GROUP BY`. It produces one value for the full table. MySQL can evaluate this uncorrelated scalar subquery once and reuse it for every city comparison.

Conceptually, if prices are $p_1,\ldots,p_R$, the national value is

$$
\frac{p_1+\cdots+p_R}{R}.
$$

For a city with $r$ listings and sum $S$, its value is $S/r$. The city survives only if $S/r$ is strictly larger than the national quotient.

**Why averaging city averages would be different**

Suppose city A has 100 listings averaging 100 and city B has one listing priced at 1,000. The national listing average is approximately 108.91, not $(100+1000)/2=550$. The exact query correctly weights every listing equally through the scalar `AVG(price)`.

This distinction also means a city’s own rows participate in the national benchmark. The query does not compare a city with “all other cities” or exclude its listings from the subquery.

**Strict inequality and output**

The condition is `AVG(price) > (...)`. A city whose average equals the national average is not expensive under the stated definition and is excluded.

The final projection contains only `city`. Since grouping produces one row per city, the values are already distinct without `DISTINCT`.

`ORDER BY 1` orders the first selected column, `city`, in ascending order by default. This supplies the deterministic ordering requested by the problem.


The scalar subquery calculates exactly one national mean from every listing. For each city, grouping collects exactly its listings and `AVG` computes exactly its city mean. The `HAVING` predicate mirrors the phrase “city average exceeds national average” with a strict comparison. Therefore every returned city satisfies the requirement, and any satisfying city passes the predicate.

Ordering affects only presentation and not the proven set.

**SQL behavior and assumptions**

The solution relies on the intended non-null `price` values. SQL `AVG` ignores nulls; if prices could be null, “every listing” would need a specified null policy. The reference schema presents integer prices and no alternate policy.

On an empty table, the scalar average is `NULL` and there are no outer groups, so the result is empty. With exactly one city, its city average equals the national average, so strict `>` returns no city.

## Complexity detail

Let $R$ be the listing-row count and $C$ the number of cities. The scalar subquery scans $R$ rows, and the outer grouping scans them again. This is still $O(R)$ aggregate work. Group construction may use hashing or sorting; a conservative general bound is $O(R\log R)$.

Final ordering of at most $C$ city names costs $O(C\log C)$, which is within $O(R\log R)$. Group state and sort buffers may use $O(R)$ space in the worst case, though hash aggregation needs only $O(C)$ logical group entries. Indexes and optimizer choices can improve physical execution.

## Alternatives and edge cases

- **Average the city averages:** This weights cities equally rather than listings and gives a different national statistic when city sizes differ.
- **Filter rows in `WHERE` by national average:** That would select expensive individual listings before averaging and solve a different problem.
- **CTE for the national mean:** Computing it once in a named CTE is equivalent; the uncorrelated scalar subquery is compact.
- **Window average:** `AVG(price) OVER ()` can attach the national value to rows before grouping, but introduces an intermediate relation.
- **One city only:** Its mean equals the national mean, so no result is returned.
- **City exactly at the national mean:** Strict `>` excludes it.
- **Cities with different row counts:** The national mean remains listing-weighted, as required.
- **Duplicate prices or names:** They are ordinary separate listings because `listing_id` identifies rows.
- **Output ordering:** `ORDER BY 1` sorts city names ascending.
