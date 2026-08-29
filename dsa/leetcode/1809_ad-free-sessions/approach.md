## General

**First identify sessions that did show an ad**

The desired rows are sessions with no matching ad. The protected query solves the complementary problem in its subquery: find every `session_id` for which at least one ad belongs to the same customer and occurred during the session.

It joins `Playback AS p` to `Ads AS a` with two conditions:

1. `p.customer_id = a.customer_id` ensures an ad is attributed only to the customer who saw it;
2. `a.timestamp BETWEEN p.start_time AND p.end_time` ensures the ad occurred during that session.

SQL `BETWEEN` is inclusive at both ends. This exactly matches the stated inclusive session interval, so an ad at `start_time` or `end_time` disqualifies the session.

**Exclude every matched session from Playback**

The outer query scans `Playback` and retains rows whose `session_id` is `NOT IN` the subquery result.

If a session has one or more matching ads, its ID appears in the subquery and the outer predicate rejects it. If no matching ad exists, its ID is absent and the outer predicate accepts it.

The subquery may return the same session ID several times when multiple ads were shown during one session. `NOT IN` membership is unaffected by duplicates, so no `DISTINCT` is required for correctness.

**Why customer equality cannot be omitted**

Timestamps alone are not enough. Two customers may have sessions covering the same time. An ad shown to one customer must not disqualify another customer's session. The join's customer condition prevents this cross-customer contamination.

The guarantee that one customer's sessions do not intersect also means one ad timestamp can belong to at most one session for that customer. That helps bound the number of actual matches, although the database execution plan still determines how efficiently they are found.

**Following the sample**

Customer 1's ad occurs at time 5. Session 1 spans `[1,5]`, so inclusive `BETWEEN` matches it. Session 2 spans `[15,23]` and does not match.

Customer 2 has ads at times 17 and 20. Both lie in session 4's `[17,28]` interval; time 17 counts because the start boundary is inclusive. Sessions 3 and 5 contain neither timestamp.

The subquery therefore returns IDs 1 and 4, possibly with 4 repeated. The outer query excludes those IDs and returns 2, 3, and 5.

**The `NOT IN` null consideration**

In general SQL, `NOT IN` behaves unexpectedly if its subquery can contain `NULL`: comparisons become unknown and may filter every row. Here the subquery selects `Playback.session_id`, described as a unique-value identifier and used as the session identity. Under the source schema it is not a nullable match value, so the problematic null case does not arise.

A `NOT EXISTS` anti-join is often preferred for defensive portability because it does not have this null sensitivity, but the exact protected query uses `NOT IN`.

**Why the result is correct**

For every returned session, its ID is absent from the join output. Therefore there is no ad satisfying both same-customer and inclusive-time conditions, so the session is ad-free.

Conversely, any ad-free session has no qualifying join row, so its ID cannot appear in the subquery and `NOT IN` retains it. These two directions prove that the query returns exactly all ad-free sessions.

No `ORDER BY` appears because the problem accepts any result order.

## Complexity detail

Let $P$ be the number of playback sessions, $A$ the number of ads, and $M$ the number of qualifying session-ad matches. SQL is declarative, so physical complexity depends on indexes and the optimizer.

With a useful index on `Ads(customer_id, timestamp)`, each playback row can perform a customer-and-time range lookup. A representative bound is $O(P\log(A+1)+M)$ after index availability. Because same-customer sessions do not overlap, $M\leq A$. Building or sorting index-like structures can add $O(A\log(A+1))$, consistent with the manifest's $O((P+A)\log(A+1))$ model.

The anti-membership result and join/index structures can require $O(P+A)$ working space, matching the manifest's broad bound.

Without helpful indexes or optimizer transformations, a nested-loop plan can compare many session-ad pairs and approach $O(PA)$ time. The SQL text alone cannot guarantee the manifest's physical bound; that bound assumes an efficient indexed or sorted execution plan.

## Alternatives and edge cases

- **`NOT EXISTS` correlated anti-join:** It expresses “no matching ad” directly and avoids `NOT IN` null semantics.
- **Left join with `IS NULL`:** Join sessions to qualifying ads and keep groups or rows with no ad match; duplicates must be handled carefully.
- **Count matches per session:** Group and retain count zero, but an outer join is required so sessions without ads are not lost.
- **Timestamp-only join:** It is incorrect because ads belong to specific customers.
- **Exclusive inequalities:** They would wrongly treat ads exactly at session boundaries as absent.
- **Multiple ads in one session:** The subquery may repeat the ID, but membership exclusion remains correct.
- **No ads table rows:** The subquery is empty and every session is returned.
- **Customer with several sessions:** Non-overlap ensures one timestamp cannot belong to two of that customer's sessions.
- **Ad outside every session:** It creates no join row and affects no result.
- **Ad at `start_time`:** Inclusive `BETWEEN` disqualifies the session.
- **Ad at `end_time`:** It also disqualifies the session.
- **Null-sensitive anti-membership:** The exact query relies on non-null session IDs in the subquery.
- **Any output order:** No sorting is required.
- **Index design:** A composite customer/timestamp index aligns with both join predicates.
- **Plan dependence:** Logical correctness is fixed even though runtime can differ substantially by database configuration.
