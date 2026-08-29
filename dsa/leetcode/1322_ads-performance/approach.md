## General

Click-through rate for one advertisement is:

$$
\frac{\text{clicks}}
{\text{clicks}+\text{views}}\times 100.
$$

Ignored actions do not belong in either the numerator or denominator. The exact MySQL query computes both counts with conditional aggregation, handles the all-ignored division-by-zero case, rounds the result, and sorts by the required two keys.

**One group per advertisement**

`GROUP BY 1` groups by the first selected expression, `ad_id`. Every interaction row for one advertisement is evaluated together, while actions for different advertisements stay separate.

The result contains one row for every distinct advertisement appearing in `Ads`. An ad with only `Ignored` actions still forms a group and therefore remains in the output.

Writing `GROUP BY ad_id` would be more explicit, but ordinal grouping has the same meaning here.

**Counting clicks with Boolean arithmetic**

In MySQL, the expression `action = 'Clicked'` evaluates to one when true and zero when false. Therefore:

`SUM(action = 'Clicked')`

counts exactly the clicked rows in the current ad group.

The denominator uses:

`SUM(action IN ('Clicked', 'Viewed'))`.

`IN` is true for either a click or a view, so this sum counts both relevant action types. An ignored row contributes zero to both aggregates.

This denominator is equivalent to:

`SUM(action = 'Clicked') + SUM(action = 'Viewed')`,

but the `IN` form expresses the combined relevant-action count directly.

**Computing a percentage**

The click count is divided by the relevant-action count and multiplied by 100. MySQL performs numeric division here, producing a fractional rate rather than truncating to an integer.

For ad 1 in the reference example, there are two clicked rows, one viewed row, and one ignored row. The ignored action is excluded, so:

$$
\frac{2}{2+1}\times100=66.666\ldots.
$$

`ROUND(..., 2)` produces `66.67`.

**Handling an ad with only ignored actions**

If an ad has no clicks and no views, both Boolean sums in the fraction are zero. The division is $0/0$, which yields `NULL` in this MySQL context.

`COALESCE(expression, 0)` replaces that null result with zero. Rounding then produces the required zero CTR.

The placement of `COALESCE` is important. It wraps the complete percentage expression, so it handles the null created by division. It does not remove the all-ignored group.

**Sorting by rate and then identifier**

`ORDER BY 2 DESC, 1` uses select-list ordinals:

- column two is `ctr`, sorted descending;
- column one is `ad_id`, sorted ascending by default.

Thus, higher-performing ads appear first. Equal rounded CTR values are ordered by the smaller identifier.

The task asks to sort by returned `ctr`, so ordering by the second projected value uses the rounded result. Using explicit names, `ORDER BY ctr DESC, ad_id ASC` would be easier to maintain.

**Why every output row is correct**

Within each ad group, Boolean sums count exactly the numerator and denominator specified by the CTR formula. Ignored rows contribute to neither. The division and multiplication compute the percentage, `COALESCE` gives zero when the denominator is zero, and `ROUND` applies the required precision.

Grouping preserves every ad represented in the table, and the two ordering keys match the result contract. Therefore, the query returns the correct metric and order for each distinct ad.

**SQL-specific assumptions**

Boolean expressions producing zero and one are a MySQL feature used by the exact source. In database systems that do not sum Boolean predicates directly, each count would need a `CASE WHEN ... THEN 1 ELSE 0 END` expression.

The composite primary key `(ad_id, user_id)` ensures one action row per user for a given ad. The query counts rows, which therefore also counts users taking each action under this schema.

## Complexity detail

Let $r$ be the number of action rows and $a$ the number of distinct advertisements.

Hash grouping can scan all rows and maintain constant-sized counters per ad in expected $O(r)$ time and $O(a)$ space. Sorting the $a$ aggregate rows by CTR and identifier costs $O(a\log a)$ time.

Total intended time is $O(r+a\log a)$ and working space is $O(a)$, matching the manifest. A sort-based aggregation may instead introduce an $O(r\log r)$ component, depending on indexes and the database execution plan.

The output contains $a$ rows. SQL complexity is plan-dependent, but the logical query performs one aggregation and one result sort.

## Alternatives and edge cases

- **Conditional `CASE` aggregation:** `SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END)` is portable across more SQL engines.
- **Separate click and view subqueries:** Joining independent counts can work but is longer and must preserve ads missing one action type.
- **Only ignored actions:** The denominator is zero, division yields null, and `COALESCE` returns zero.
- **Clicks but no views:** Numerator equals denominator, so CTR is 100.
- **Views but no clicks:** Numerator is zero with a positive denominator, so CTR is zero without needing `COALESCE`.
- **Ignored rows mixed with relevant actions:** They do not change either count or the rate.
- **Rounding ties:** Ordering uses the selected rounded CTR because `ORDER BY 2` references the projected column.
- **Tie-breaking:** Ascending `ad_id` is mandatory after equal CTR values.
- **Ordinal clauses:** `GROUP BY 1` and `ORDER BY 2 DESC, 1` are concise but fragile if the select list changes.
- **Every ad remains represented:** Grouping starts from all `Ads` rows, so an ignored-only ad is not lost.
- **MySQL Boolean sums:** A different SQL dialect may require explicit `CASE` expressions.
