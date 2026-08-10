## General

**The output needs rows even for empty categories**

For every represented date, the result must contain desktop, mobile, and both, including categories with zero users. Aggregating Spending directly cannot create a group that has no source row.

CTE `P` builds the complete date-category skeleton. Each distinct spending date is paired once with each of the three literal platform labels through three `UNION` branches.

Using `UNION` deduplicates rows across branch outputs, although the labels differ and each branch already selects distinct dates.

This skeleton establishes the output grain before measures are calculated: exactly one row per represented date and requested category. Later joins may attach zero, one, or many classified users, but the final grouping returns to this predetermined grain.

**Classify each user separately on each date**

CTE `T` groups by `user_id` and `spend_date`. The primary key allows at most one desktop and one mobile row for that user-date.

`SUM(amount)` combines all money the user spent that date. If only one platform row exists, `COUNT(platform) = 1` and the classification remains that row’s platform. If both rows exist, count is two and classification becomes literal `'both'`.

Thus a two-platform user contributes one combined record to both rather than one record to each single-platform category.

**Join classified users onto the skeleton**

`P LEFT JOIN T USING (spend_date, platform)` preserves every date-category row. Matching classified user records attach their amounts and IDs. A category with no users remains as one null-extended row.

Grouping by date and platform then computes category totals.

`SUM(amount)` adds every classified user’s daily amount. For an empty category it sees only null, so `COALESCE(..., 0)` returns numeric zero.

`COUNT(t.user_id)` counts non-null user IDs. It returns zero for a null-extended skeleton row. Since `T` has exactly one row per user-date, ordinary count is the number of users without needing `DISTINCT`.

Counting a column from `T` rather than `COUNT(*)` is essential. A left join always retains one skeleton row even without a match, so `COUNT(*)` would incorrectly report one user for an empty category.

**Why each purchase is counted exactly once**

Each Spending row belongs to one user-date group in `T`. That group becomes exactly one of desktop, mobile, or both. Its amount is summed once and joins exactly one skeleton category.

Therefore, no amount or user is duplicated across categories. The skeleton adds only empty placeholders and does not create extra matches for real classified records.

**A MySQL grouping-mode nuance**

Inside `T`, expression `IF(COUNT(platform) = 1, platform, 'both')` references `platform` even though it is neither grouped nor aggregated. When count is one, there is only one platform value and the intended result is unambiguous; when count is two, the other branch ignores the arbitrary platform.

MySQL configurations enforcing `ONLY_FULL_GROUP_BY` may still reject this syntactically because `platform` is not functionally determined by `user_id, spend_date` when two rows exist. A portable formulation can use `MIN(platform)` in the count-one branch or classify through counts of each platform.

The protected query relies on a permissive SQL mode or engine acceptance of this expression. The logical classification remains as described.

**Why the final output is complete**

P contains three rows for every represented date. The left join preserves all three. Aggregation converts missing measures to zeros and real groups to correct sums and counts. Thus every required date-category combination appears exactly once.

Result order is unrestricted, so no `ORDER BY` is needed.

## Complexity detail

Let $R$ be the number of Spending rows. Distinct-date generation, user-date grouping, joining, and final grouping can require sorting, giving a conservative $O(R\log R)$ time bound.

The CTEs and aggregation state may materialize $O(R)$ rows, matching the manifest’s $O(R)$ space. There are at most three skeleton rows per distinct date.

Hash-based plans and suitable indexes can improve practical behavior, but SQL leaves the physical strategy to the optimizer.

## Alternatives and edge cases

- **Cross join dates with a three-row platform table:** This explicitly constructs the same skeleton and can be clearer than three UNION branches.
- **Conditional aggregation:** Classify user-date rows first, then aggregate CASE expressions. A skeleton is still needed to emit zero categories.
- **Separate queries per category:** Compute desktop-only, mobile-only, and both, then union them with missing-row handling. It is more repetitive.
- **User spends on both platforms:** Their two amounts combine and the user counts once in both.
- **User spends on one platform:** They remain in that single category.
- **Empty category:** Left join plus `COALESCE` and non-null count produce zero and zero.
- **Same user on different dates:** Classification is independent per date.
- **Primary key:** It limits one row per user-date-platform, making platform count one or two.
- **No Spending rows:** There are no represented dates, so the result is empty.
- **Amount zero:** The user still counts, while total amount may remain zero.
- **ONLY_FULL_GROUP_BY:** The unaggregated platform reference in `T` may require a portable rewrite.
- **Any result order:** No final sorting is required.
