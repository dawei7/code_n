## General

Group the `prompts` rows by `user_id`. Within each group, `COUNT(*)` produces `prompt_count`, `AVG(tokens)` gives the user's average token usage, and `MAX(tokens)` identifies their largest individual prompt.

The existential requirement can be tested without another scan or join. Some prompt has `tokens` strictly above the group average exactly when the group's maximum is strictly above that average. Accordingly, the `HAVING` clause retains groups satisfying both `COUNT(*) >= 3` and `MAX(tokens) > AVG(tokens)`. This proves both directions: every returned user meets the count and above-average requirements, while every qualifying user has a maximum that witnesses the second predicate and is therefore retained.

Round `AVG(tokens)` only in the projected `avg_tokens` column. Keep the raw aggregate in the eligibility comparison so display rounding cannot change a strict boundary. Finally, order the projected rows by `avg_tokens DESC` and then `user_id ASC`, matching both source sort keys.

## Complexity detail

Let $R$ be the number of prompt rows and $U$ the number of distinct users. Under a general sort-based execution plan, grouping costs $O(R\log R)$ time and sorting the retained user groups costs $O(U\log U)$, for $O(R\log R+U\log U)$ total time. Such a plan can use $O(R+U)$ working space. A database may instead choose hash aggregation or exploit indexes, but the query does not depend on either optimization.

The benchmark defines size as $R$ and supplies three prompts for each user, so $R=3U$. The accepted query aggregates the table once; the slower control obtains the same aggregates with correlated per-user rescans.

## Alternatives and edge cases

- **Correlated aggregate subqueries:** Separate per-user `COUNT`, `AVG`, and `MAX` subqueries can reproduce the result, but repeatedly scanning `prompts` may grow quadratically.
- **Self-join against the average:** Joining every row to a per-user aggregate and filtering rows above the average is valid, but a direct `MAX(tokens) > AVG(tokens)` test is simpler and avoids duplicating group data.
- **Exactly three prompts:** The minimum is inclusive; a three-row group qualifies when its values are not all equal.
- **Equal token counts:** When every prompt uses the same number of tokens, the maximum equals the average, so the strict comparison excludes the user.
- **Average rounding:** Round the displayed value to two decimal places, but do not compare an individual prompt with that rounded value.
- **Sort ties:** Equal `avg_tokens` values are ordered by smaller `user_id` first.
