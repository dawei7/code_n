## Function Contract

**Inputs**

`Actions(user_id, post_id, action_date, action, extra)` may contain duplicate rows. `Removals(post_id, remove_date)` contains at most one removal row per post.

For a date, form the distinct set of `post_id` values whose rows satisfy both `action = 'report'` and `extra = 'spam'`. Its daily percentage is 100 times the fraction of those posts present in `Removals`. A post reported on two dates participates independently in both daily sets. Dates with no qualifying spam report do not enter the average.

**Return value**

- Return one column named `average_daily_percent` and one row.
- Average the daily percentages without weighting by each day's post count.
- Round only the final average to two decimal places.
- Ignore the value and relative timing of `remove_date`; only removal membership matters.
