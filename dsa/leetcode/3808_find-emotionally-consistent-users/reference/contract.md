## Function Contract

**Input table**

- `reactions`: One row per distinct (`user_id`, `content_id`) pair, with the three columns defined in the Description.

For a user with $R_u$ reaction rows, let $C_{u,t}$ be the number whose `reaction` is type $t$. The user qualifies only when $R_u \ge 5$ and some type satisfies

$$
\frac{C_{u,t}}{R_u} \ge 0.60.
$$

Because 60% is greater than half, at most one reaction type can satisfy this condition for a user.

**Result table**

Return exactly these columns:

- `user_id`
- `dominant_reaction`, the qualifying reaction type
- `reaction_ratio`, the qualifying type's count divided by the user's total reaction count

Include one row for each qualifying user. Sort the rows by `reaction_ratio DESC, user_id ASC`.
