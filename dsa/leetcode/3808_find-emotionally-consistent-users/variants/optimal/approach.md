## General

**Turn many reaction rows into one count per user and reaction type**

The input contains one row for every distinct user-and-content pair. A user can therefore have many rows, and the same reaction word can appear on several of them. The final answer does not care which content item received each reaction; it needs only two quantities for every user:

1. the user's total number of reaction rows, and
2. the largest number of those rows that share one reaction type.

The first common table expression, `t`, performs the useful compression. It groups by `user_id` and `reaction` and computes `COUNT(1)`. A row such as `(7, 'like', 8)` in `t` means that user 7 used `like` on eight different content items. Call the number of rows in the original table $R$, the number of users $U$, and the number of distinct user-and-reaction pairs $D$. The original $R$ rows become only $D$ grouped rows, where $D \le R$.

This first aggregation is important because the next step must compare reaction types within each user. Doing that from `t` is simpler than repeatedly recounting the original table. For one user, if the rows of `t` have counts $c_1,c_2,\ldots,c_k$, then `SUM(cnt)` is that user's total number of reactions:

$$
R_u = c_1+c_2+\cdots+c_k.
$$

Similarly, `MAX(cnt)` is the count of the user's most frequent reaction:

$$
M_u = \max(c_1,c_2,\ldots,c_k).
$$

**Build one summary row per user**

The second common table expression, `s`, groups the rows of `t` by `user_id`. It retains `MAX(cnt)` as `mx_cnt` and calculates `ROUND(MAX(cnt) / SUM(cnt), 2)` as `reaction_ratio`. It also applies two conditions in its `HAVING` clause:

- `SUM(cnt) >= 5` requires at least five reaction rows for the user.
- `reaction_ratio >= 0.60` requires the computed, two-decimal ratio to be at least 0.60.

Using `HAVING` is appropriate because these conditions depend on aggregate values that do not exist until all grouped rows for a user have been combined. A `WHERE` condition at this stage could filter individual rows, but it could not directly decide whether a user's total is at least five or whether their largest category reaches the threshold.

For the first example's user 1, `t` contains counts 4 for `like` and 1 for `wow`. The row constructed in `s` has `mx_cnt = 4`, total 5, and `reaction_ratio = 0.80`. User 2 has grouped counts 2, 2, and 1, so the largest ratio is 0.40 and no row for that user survives. User 3 has only one grouped count, 5, giving a ratio of 1.00.

**Recover the name belonging to the maximum count**

The summary row in `s` contains the maximum count but not the corresponding reaction string. The final query joins `s` back to `t` with `JOIN t USING (user_id)`. This temporarily pairs each qualifying user's summary with all of that user's reaction-type counts. The condition `WHERE cnt = mx_cnt` keeps the row whose count equals the recorded maximum, thereby recovering `reaction` and exposing it under the alias `dominant_reaction`.

Under the intended 60% condition, the dominant type is unique. Two different reaction types cannot each account for at least 60% of the same total because their combined share would be at least 120%. The source's rounded test also only admits displayed ratios of at least 0.60; every exact share that rounds that high is still greater than one half. Consequently, two categories cannot tie at `mx_cnt` for a row that this query admits, so the join produces one result row per admitted user rather than duplicate winners.

The last clause, `ORDER BY 3 DESC, 1`, refers to result columns by position. Column 3 is `reaction_ratio`, so larger ratios appear first. Column 1 is `user_id`, so users with the same displayed ratio appear in ascending identifier order. The selected columns are exactly the requested three: the user, the dominant reaction, and its two-decimal ratio.

**A threshold-order defect in the exact source**

The contract says that an exact share of at least 60% qualifies and separately says that the returned ratio should be rounded to two decimal places. Those instructions require testing

$$
\frac{M_u}{R_u} \ge 0.60
$$

before rounding the value for display. The exact source instead assigns `reaction_ratio = ROUND(MAX(cnt) / SUM(cnt), 2)` and tests that rounded alias in `HAVING`. This changes membership near the boundary.

For example, suppose a user has 42 reactions: 25 of one type and 17 of another. The exact dominant share is

$$
\frac{25}{42} \approx 0.595238,
$$

which is below 0.60 and should not qualify. Rounding it to two decimal places produces 0.60, so the written query includes the user. This is a genuine correctness defect, not merely a presentation detail. A contract-correct form would test the unrounded counts, such as `MAX(cnt) * 5 >= SUM(cnt) * 3`, and round only the selected output. Integer cross-multiplication also avoids floating-point boundary ambiguity. The rest of the aggregation and join strategy remains valid.

## Complexity detail

Let $R$ be the number of rows in `reactions`, $D$ the number of distinct `(user_id, reaction)` pairs, and $U$ the number of distinct users. The first grouping reads all $R$ rows and materializes $D$ counts. The second grouping reads those $D$ rows and materializes at most $U$ summaries. The join then processes the grouped data for the qualifying users, and the final ordering sorts at most $U$ result rows.

The manifest states $O(R\log R + U\log U)$ time and $O(R+U)$ space. That is a reasonable sort-based upper-bound model: grouping the original rows can require sorting $R$ keys, while ordering the final users costs $O(U\log U)$. Since $D\le R$, the intermediate work is covered by the $R\log R$ term. A database engine may instead use hash aggregation and a hash join, giving expected linear aggregation work followed by the unavoidable result sort. Physical indexes, memory limits, execution plans, and spilling can change real performance, so SQL complexity describes the logical scale rather than promising one exact implementation plan.

The grouped relation `t` occupies $O(D)$ rows and `s` occupies $O(U)$ rows. The final sort can also need $O(U)$ working memory, so a precise auxiliary bound is $O(D+U)$, which is at most the manifest's $O(R+U)$. The returned table itself contains at most one row per qualifying user.

## Alternatives and edge cases

- **Conditional window functions:** Windowed `COUNT(*)` values can attach each user's total and each user/type count to grouped data, after which a rank chooses the dominant type. This can be expressive, but it usually carries more repeated values and still needs careful handling of the threshold, uniqueness, and final ordering.
- **Rank every reaction type:** `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY cnt DESC)` can select the largest type directly instead of joining `s` back to `t`. It removes the recovery join, although the current join is safe because every admitted user has a unique maximum.
- **Test exact counts before formatting:** The essential repair is to use `MAX(cnt) * 5 >= SUM(cnt) * 3`, or an equivalent unrounded comparison, and apply `ROUND` only to the output expression. This prevents shares from roughly 59.5% through just under 60% from entering the result.
- **Exactly five reactions:** A user with five rows is eligible for consideration. Three matching reactions give exactly 60% and qualify; two give 40% and do not.
- **Fewer than five reactions:** Even a user whose reactions are all the same type must be excluded when the total is below five, because consistency alone does not satisfy the minimum-activity rule.
- **One reaction type:** If an eligible user has only one reaction type, `t` has one row for that user, `MAX(cnt)` equals `SUM(cnt)`, and the displayed ratio is 1.00.
- **Equal displayed ratios:** Different exact shares can round to the same two-decimal number. The query correctly breaks such output ties by ascending `user_id` because it orders by the displayed `reaction_ratio` and then the identifier.
- **No qualifying users:** Both `s` and the final result can be empty; SQL naturally returns an empty result table without requiring a special sentinel row.
- **Primary-key implication:** Because `(user_id, content_id)` is unique, `COUNT(1)` truly counts different content items for a user. No `COUNT(DISTINCT content_id)` is needed under the stated schema.
