## General
**Turn every transfer into signed balance changes**

Project each transaction twice with `UNION ALL`: emit `-amount` for `paid_by` and `+amount` for `paid_to`. `UNION ALL` is essential because repeated equal changes are separate transfers and must not be deduplicated.

**Aggregate one net change per involved user**

Group the signed rows by `user_id` and sum them. This produces the exact total received minus total paid for every user who appears in at least one transaction.

**Preserve users without transactions**

Left-join the net changes to `Users`. Replace a missing aggregate with zero using `COALESCE`, add it to the stored credit, and apply the same expression in a `CASE` test for negativity. Every transaction contributes once negatively and once positively, so the aggregate gives each user exactly the required net movement. The left join then covers both involved and uninvolved users.

The source permits any result order; the local query orders by `user_id` only to make fixtures and display deterministic.

## Complexity detail
The signed intermediate relation contains $2t$ rows. Grouping and deterministic output ordering have a portable upper bound of $O(N\log N)$ time. The signed rows, grouped changes, and sorting workspace can use $O(N)$ auxiliary space. Hash aggregation may make the expected physical work closer to linear.

## Alternatives and edge cases
- **Two separate aggregate joins:** independently sum outgoing and incoming transfers, then join both totals to users; this is correct but more verbose.
- **Correlated subqueries per user:** compute incoming and outgoing sums separately for every user, which can repeat transaction scans and approach $O(ut)$ time.
- **Inner join to transactions:** this incorrectly omits users who never paid or received money.
- A final balance of exactly zero does not breach the limit.
- A user can have only incoming or only outgoing transactions.
- Multiple transfers between the same users must all be counted.
- Transaction dates do not affect the final all-time balance.
- `UNION` without `ALL` could discard duplicate signed changes.
- User names do not need to be unique because grouping and joining use `user_id`.
