## General

Every policy row must satisfy two conditions at the same time:

1. its `tiv_2015` value occurs in at least two policy rows;
2. its exact `(lat, lon)` pair occurs in exactly one policy row.

After finding rows that satisfy both, the query sums their `tiv_2016` values and rounds the final total. The challenge is that both conditions depend on how one row compares with the *whole table*. Window functions are a natural fit because they calculate group-level facts while still retaining one result row for every original policy.

**Annotating rather than collapsing**

The common table expression `T` reads `Insurance` and returns `tiv_2016` plus two counts:

```sql
COUNT(1) OVER (PARTITION BY tiv_2015) AS cnt1
```

and

```sql
COUNT(1) OVER (PARTITION BY lat, lon) AS cnt2
```

An ordinary `GROUP BY tiv_2015` would collapse all policies with the same investment value into one row. That is useful for discovering duplicate values, but the final sum needs each qualifying row’s own `tiv_2016`. A window aggregate instead writes the group count beside every member of that group.

For `cnt1`, `PARTITION BY tiv_2015` forms one logical partition per 2015 investment value. `COUNT(1)` counts every row in that partition because the literal 1 is never `NULL`. If `cnt1 > 1`, at least one other policy has the same `tiv_2015`.

For `cnt2`, partitioning by both `lat` and `lon` treats the two coordinates as one compound location. The count is one exactly when no other policy occupies the same coordinate pair. It would be incorrect to test latitude and longitude uniqueness separately: two policies could share a latitude while having different longitudes and therefore represent different locations.

Using the two columns directly is also safer than concatenating coordinate text. Concatenation can create ambiguous encodings—for example, components `(1, 23)` and `(12, 3)` can both become `"123"` without a robust delimiter and type representation. A multi-column SQL partition preserves tuple identity.

**Filtering requires both conditions**

The outer query applies:

```sql
WHERE cnt1 > 1 AND cnt2 = 1
```

`AND` is essential. Sharing a `tiv_2015` value is not enough if the location is duplicated, and having a unique location is not enough if the investment value occurs only once.

In the sample, policies 1, 3, and 4 all have `tiv_2015 = 10`, so each gets `cnt1 = 3`. Policy 2 has `tiv_2015 = 20` and gets `cnt1 = 1`. Locations `(10,10)` and `(40,40)` occur once, while `(20,20)` occurs twice. Policies 1 and 4 are the only rows with counts respectively greater than one and equal to one. Their 2016 values, 5 and 40, sum to 45.

**Aggregating and rounding at the end**

After filtering, `SUM(tiv_2016)` combines the 2016 investments from all qualifying policyholders. `ROUND(..., 2)` rounds the combined result to two decimal places:

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
```

Rounding after summation follows the requested operation. Rounding every individual value first and then adding can produce a different total when values contain more than two fractional digits. The alias gives the output its required column name.

**Why the query is correct**

Take any policy row $p$. Its `cnt1` equals the number of table rows whose `tiv_2015` equals $p$’s value because the first window partition contains exactly those rows. Thus, `cnt1 > 1` holds exactly when another policy shares that value.

Likewise, `cnt2` equals the number of rows whose latitude and longitude both equal $p$’s coordinates. Because `lat` and `lon` are non-`NULL`, `cnt2 = 1` holds exactly when $p$ is the only policy at that location.

The outer filter retains $p$ if and only if both required statements are true. No qualifying row is lost and no nonqualifying row remains. Summing the retained `tiv_2016` values therefore produces exactly the requested total, and final rounding supplies the requested numeric presentation.

The fact that `pid` is unique ensures each input row represents one policyholder record. `COUNT(1)` is counting policy rows, so no `DISTINCT` is needed.

## Complexity detail

Let $n$ be the number of `Insurance` rows. Computing the two window partitions usually requires hashing or sorting rows by `tiv_2015` and by `(lat, lon)`. A conventional sort-based plan takes $O(n\log n)$ time, matching the manifest. Hash-based partition counting may achieve expected $O(n)$ aggregation work, but SQL does not mandate that plan.

The annotated common table expression has $n$ logical rows. Partition state, sorting, or materialization can require $O(n)$ working space. The outer filter and sum make one linear pass over those annotated rows and use constant aggregate state. The declared auxiliary bound is therefore $O(n)$.

Float equality and rounding follow the database’s numeric types and rules. The asymptotic analysis counts row operations rather than bit-level numeric precision.

## Alternatives and edge cases

- **Two grouped subqueries and joins:** One subquery finds `tiv_2015` groups with count above one, another finds location groups with count one, and the base table joins both. This is correct but more verbose than annotating each row once with window counts.
- **Correlated `EXISTS` and `NOT EXISTS`:** Check for another row with equal `tiv_2015` and ensure none with the same location but a different `pid`. Clear logic, but without suitable indexes it may repeatedly scan the table.
- **Grouped counts joined back:** Precompute both count maps and join them to `Insurance`. This mirrors the window logic explicitly and can be portable where window functions are unavailable.
- **Concatenated location key:** Avoid it because formatting and delimiter collisions can merge different coordinate pairs. Partition by both columns.
- **Same latitude only:** Sharing one coordinate does not mean sharing a city; both `lat` and `lon` must match.
- **Location shared by two otherwise qualifying policies:** Both receive `cnt2 = 2` and both must be excluded.
- **A `tiv_2015` value occurring once:** Its row fails `cnt1 > 1` even if its location is unique.
- **More than two duplicate investments:** Every member qualifies for the first condition; “same as one or more” means count at least two, not exactly two.
- **No qualifying rows:** Standard SQL `SUM` over an empty set returns `NULL`, and `ROUND(NULL, 2)` remains `NULL`. The expected dataset generally supplies a result; `COALESCE` would be needed if the contract demanded numeric zero.
- **Rounding order:** Sum first, round once. Per-row rounding can alter the final answer.
- **Non-null coordinates:** The schema guarantee avoids special window grouping semantics for missing locations.
- **Exact float grouping:** SQL groups stored values according to their exact database equality semantics; visually similar floating-point inputs need not compare equal if stored differently.
