## Function Contract

**Input table**

- `prompts`: One row per distinct (`user_id`, `prompt`) pair, with the three columns defined in the Description.

All counts and averages are computed within one user's group. The comparison with an individual prompt uses that group's unrounded average; only the displayed `avg_tokens` value is rounded.

**Result table**

Return exactly these columns:

- `user_id`
- `prompt_count`, the number of that user's rows
- `avg_tokens`, the average of that user's `tokens` values rounded to two decimal places

Include only groups with `prompt_count >= 3` and with at least one `tokens` value strictly greater than the group average. Sort by `avg_tokens DESC, user_id ASC`.
