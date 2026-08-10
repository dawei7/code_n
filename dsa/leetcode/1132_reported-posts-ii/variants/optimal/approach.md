## General

**Compute one percentage per reporting date**

The requested average is not one global ratio. Each date with spam-reported posts first receives its own percentage, and those daily percentages are then averaged with equal weight.

CTE `T` creates exactly that intermediate grain: one row per qualifying `action_date` containing column `percent`.

**Preserve every spam-reported post with a left join**

`Actions AS t1 LEFT JOIN Removals AS t2 ON t1.post_id = t2.post_id` keeps an action row even when its post was never removed. For a removed post, `t2.post_id` is non-null; for an unremoved post, it is null.

The removal date is not part of the join because the contract cares only whether the post appears in Removals, not when removal happened relative to reporting.

Removals has primary key `post_id`, so a post matches at most one removal row and is not multiplied by the join.

**Use distinct posts in both numerator and denominator**

Actions may contain duplicate rows and several users may report the same post. The daily denominator must be the number of distinct spam-reported posts, so it uses `COUNT(DISTINCT t1.post_id)`.

The numerator uses `COUNT(DISTINCT t2.post_id)`. SQL count ignores null, so only matched removed posts contribute, and distinct prevents multiple action rows from counting one removed post repeatedly.

Their quotient is the fraction removed. Multiplication by 100 converts it to a percentage.

**Group before averaging**

`GROUP BY action_date` calculates separate ratios. A post reported on two different dates participates once in each date’s distinct set, which the contract explicitly allows.

The outer `AVG(percent)` gives every date one equal contribution regardless of how many posts it had. This differs from dividing total removed posts across all days by total reported posts, which would weight high-volume dates more heavily.

`ROUND(..., 2)` rounds only the final average, avoiding cumulative error from rounding each daily value first.

For the example, July 4 has two distinct spam-reported posts and one removal, so its row in T is fifty. July 2 has one reported post and one removal, so its row is one hundred. AVG sees two rows and computes seventy-five. The two-post day does not receive twice the weight of the one-post day.

**Exact filter limitation**

The protected query filters only `extra = 'spam'`. The written contract requires both `action = 'report'` and `extra = 'spam'`.

If the source guarantees that literal spam can appear in `extra` only on report rows, the shorter predicate is equivalent. The local schema description does not make that exclusivity guarantee; `extra` can contain other action-specific information.

A non-report action with `extra = 'spam'` would incorrectly enter the denominator and possibly numerator. To implement the written contract for arbitrary legal rows, the `WHERE` clause must also require `action = 'report'`.

**Why the intended query is correct with that predicate**

After the two filters, each retained row concerns a spam report. Left joining labels removal membership, distinct counts form exact daily post sets, grouping produces one percentage per represented date, and the outer average gives those dates equal weight.

If no qualifying dates exist, `AVG` over an empty CTE returns null. The contract asks for one result row and does not specify replacing that null, so the exact aggregate behavior is preserved.

Division occurs after both distinct counts are known. Every represented date has at least one qualifying denominator post, so division by zero cannot occur inside T.

## Complexity detail

Let $R$ be Actions rows plus relevant Removals rows. A general sort-based join, daily grouping, and distinct aggregation can take $O(R\log R)$ time.

Join, distinct sets, and grouping state can require $O(R)$ space, matching the manifest. Hash aggregation or indexes may improve practical execution.

The output is always one aggregate row, while the CTE has at most one row per qualifying date.

## Alternatives and edge cases

- **Pre-deduplicate date-post pairs:** Select distinct spam report pairs first, left join removals, then average daily conditional counts.
- **Conditional numerator:** Count distinct `CASE WHEN removal matched THEN post_id END`; it makes the removed test explicit.
- **Global ratio:** Incorrect because it weights dates by their post counts.
- **Inner join:** Incorrect because it removes unremoved posts from the denominator.
- **Duplicate reports:** Distinct post counts prevent inflation.
- **Several reporters for one post:** The post contributes once on that date.
- **Same post on two dates:** It contributes independently to both daily percentages.
- **Removal date:** Its value is intentionally ignored.
- **Zero removed on a date:** Numerator zero produces a zero-percent daily value.
- **All removed on a date:** Numerator equals denominator and produces one hundred percent.
- **Non-report row with extra spam:** The exact query includes it; adding the action predicate is required by the written contract.
- **Final rounding:** Only the average is rounded to two decimals.
- **No qualifying rows:** The aggregate row contains null unless an explicit fallback is added.
- **Equal weighting across dates:** `AVG(percent)` gives every reporting date one vote regardless of how many distinct spam posts it contains, which is the required daily-average interpretation.
