## Description

The `Members` table identifies store members. `Visits` records each member's trips to the store, and `Purchases` contains at most one purchase associated with a visit. A member's conversion rate is the percentage of visits that resulted in a purchase:

$$
\text{conversion rate}
=
\frac{100 \cdot \text{number of purchases}}{\text{number of visits}}.
$$

Report every member's ID, name, and category. A member with no visits is `Bronze`. Otherwise, a conversion rate of at least $80$ is `Diamond`, a rate from $50$ up to but not including $80$ is `Gold`, and a rate below $50$ is `Silver`. The result rows may appear in any order.
