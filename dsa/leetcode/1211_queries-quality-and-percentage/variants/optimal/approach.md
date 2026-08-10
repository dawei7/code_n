## General

Each output row summarizes all source rows with one non-null `query_name`. The query uses two averages: one over rating-to-position ratios and one over Boolean poor-query indicators.

**Exclude unnamed groups**

`WHERE query_name IS NOT NULL` removes rows that cannot belong to a named result group. This matters if the table permits null query names. Ordinary duplicate rows are not removed; each row is an observation and contributes separately to both averages.

**Compute quality as an average of row ratios**

`rating / position` calculates the ratio for one row. MySQL’s division operator produces a non-integer numeric result, so values such as five divided by two contribute 2.5 rather than being truncated.

`AVG(rating / position)` then averages those per-row ratios within a query-name group. The order is important: average of ratios is not generally the same as total rating divided by total position.

`ROUND(..., 2)` rounds the final group average to two decimal places and aliases it as `quality`.

**Turn the poor condition into a percentage**

In MySQL, `rating < 3` evaluates to one when the row is poor and zero otherwise. Averaging this indicator gives the fraction of group rows that are poor:

$$
\frac{\text{poor row count}}{\text{total row count}}.
$$

Multiplying by 100 converts the fraction to a percentage, and rounding to two decimals produces `poor_query_percentage`.

For three rows with one poor rating, the Boolean values are zero, zero, and one. Their average is one third; multiplying by 100 and rounding gives 33.33.

**Group by the selected name**

`GROUP BY 1` refers to the first selected expression, `query_name`. Every non-null name produces one output row. The contract accepts any order, so no `ORDER BY` is needed.

For the Dog example, the row ratios are five, 2.5, and 0.005. Their average is 2.501666..., rounded to 2.50. Exactly one of three ratings is below three, producing 33.33 percent.

**Why both results are exact**

Every retained source row belongs to exactly one name group and contributes exactly one ratio and one poor indicator. `AVG` divides each sum by the same group row count. The formulas therefore match the definitions directly, and final rounding is applied only after aggregation rather than to individual observations.

**Why the quality formula cannot be simplified to two sums**

Quality gives every result row equal observational weight. For positions one and ten with ratings five and five, the required value is the average of five and one half, which is 2.75. Dividing total rating ten by total position eleven would give about 0.91 and answer a different question. The query correctly performs division inside `AVG`, once per row.

The percentage expression uses the same equal-row weighting. Each row contributes either zero or one before averaging. A row’s position and rating magnitude beyond the poor threshold do not make it count more than another row. A rating of one and a rating of two are both one poor observation.

**Rounding happens after the statistical calculation**

MySQL first computes the complete group average, then multiplies the poor fraction by 100 where applicable, and only then calls `ROUND`. Keeping full intermediate precision prevents accumulated rounding error. The aliases name the final rounded expressions, so downstream consumers see the requested two-decimal metrics even though their internal calculation used more precision.

The result is therefore stable at the requested presentation precision without changing which source observations contribute.

## Complexity detail

Let $n$ be the number of table rows and $g$ the number of non-null query-name groups.

Under hash aggregation, scanning, filtering, and updating two fixed aggregates per row take expected $O(n)$ time and $O(g)$ state. A sort-based database plan may instead require $O(n\log n)$ ordering work. The manifest’s $O(n)$ bound describes the standard hash-grouping model.

The output contains $g$ rows and uses $O(g)$ space. Physical temporary storage depends on the optimizer.

## Alternatives and edge cases

- **Explicit `CASE` for poor rows:** `AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END)` is more portable across SQL dialects.
- **Count-based percentage:** Compute `100 * SUM(rating < 3) / COUNT(*)`. It is algebraically equivalent when all ratings are non-null.
- **Round each ratio first:** This is incorrect because early rounding can change the average; round only the final aggregate.
- **Rating exactly three:** It is not poor because the condition is strictly less than three.
- **Duplicate rows:** They represent repeated observations and must each contribute; the query preserves them.
- **Null query name:** The `WHERE` clause deliberately excludes it rather than creating a null-named group.
- **One-row group:** Quality is that row’s ratio, and the poor percentage is either zero or 100.
- **Position is never zero:** The documented range starts at one, so division by zero cannot occur.
- **Any result order:** No presentation sort is required.
- **Ordinal grouping:** `GROUP BY 1` depends on `query_name` remaining the first selected expression.
