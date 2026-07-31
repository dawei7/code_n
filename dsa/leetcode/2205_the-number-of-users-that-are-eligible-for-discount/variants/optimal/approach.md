## General

**Filter the events that establish eligibility**

A purchase can establish eligibility only when both independent conditions hold: its timestamp lies between `startDate` and `endDate`, inclusively, and its amount is at least `minAmount`. Apply these predicates before aggregation so irrelevant rows never enter the distinct-user state.

The date arguments represent midnight timestamps. An inclusive comparison therefore admits a purchase exactly at `endDate 00:00:00`, but not one later on that calendar day. A direct `BETWEEN` comparison expresses both inclusive boundaries.

**Count users rather than purchases**

One user can have several qualifying purchases, but must contribute only once. `COUNT(DISTINCT user_id)` performs that deduplication and returns zero when the filter selects no rows.

Every counted identifier belongs to a purchase satisfying both required predicates, so every counted user is eligible. Conversely, every eligible user has at least one such purchase, which survives the filter and contributes its identifier to the distinct aggregate. The result is therefore exactly the number of eligible users.

## Complexity detail

Let $r$ be the number of purchase rows and $u$ the number of distinct users among the qualifying rows. A full scan plus a comparison-based distinct aggregate costs $O(r\log u)$ time and $O(u)$ auxiliary space.

Database indexes, hash aggregation, and the query optimizer can improve the practical plan; the stated bound describes a conventional scan with an ordered distinct set.

## Alternatives and edge cases

- **Group and count:** Grouping qualifying rows by `user_id` in a subquery and counting the groups is equivalent, but more verbose than a distinct aggregate.
- **Correlated existence checks:** Testing eligibility separately for every user can be correct, but may repeatedly scan `Purchases` without a suitable index.
- **Counting rows:** Plain `COUNT(*)` overcounts users who make multiple qualifying purchases.
- **Inclusive amount threshold:** A purchase whose amount equals `minAmount` qualifies.
- **Midnight upper boundary:** A purchase exactly at `endDate 00:00:00` qualifies; one second later does not.
- **No qualifying purchases:** The aggregate returns `0`, not an absent result row.
