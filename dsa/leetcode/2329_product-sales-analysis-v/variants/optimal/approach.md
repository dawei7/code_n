## General

Each sale supplies a quantity but not its monetary value, so first join it to the matching product price. The expression `quantity * price` then gives that row's spending contribution.

Group these contributions by `user_id` and sum them. Grouping at the user level combines purchases of different products as well as repeated purchases of the same product, yielding exactly one total for each user represented in `Sales`.

Finally, sort the grouped rows by the computed `spending` in descending order. Add ascending `user_id` as the second key so every spending tie has the required deterministic order.

## Complexity detail

Let $s$ be the number of sales and $p$ the number of products. A conservative general database bound for the join, grouping, and ordered output is $O((s+p)\log s)$ time. Join structures, user aggregates, and sorting workspace can use $O(s+p)$ space. Appropriate indexes or hash aggregation may reduce physical work, but the declared bounds do not assume a particular execution plan.

## Alternatives and edge cases

- **Sum quantities only:** Products can have different prices, so quantity alone is not a spending measure.
- **Group by user and product:** That produces several rows per user; this problem asks for one total across all products.
- **Sort only by spending:** Equal totals would lack the required ascending user-ID tie-breaker.
- **Repeated purchases:** Every sale row contributes independently to the user's sum.
- **Equal spending:** The numeric total remains unchanged; only the secondary ordering decides row position.
