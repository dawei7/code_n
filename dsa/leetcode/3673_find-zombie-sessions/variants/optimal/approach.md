## General

**Summarize one session with one aggregate row.** Group by both `session_id` and `user_id`, then compute the earliest and latest timestamp and conditional counts for scrolls, clicks, and purchases. The timestamp difference supplies `session_duration_minutes`, while the three counts contain everything needed by the remaining predicates. Other event types and `event_value` do not affect eligibility.

Apply the four rules after aggregation. Duration must be strictly greater than 30, the scroll count must be at least five, and the purchase count must be zero. If a group contains $C$ clicks and $R$ scrolls, its ratio condition is

$$
\frac{C}{R}<\frac{1}{5}.
$$

The scroll threshold guarantees $R>0$, so multiplying by $5R$ preserves the comparison and gives $5C<R$. This integer form avoids floating-point rounding and excludes the exact $0.20$ boundary correctly.

Every retained aggregate row satisfies all four conditions and therefore represents a zombie session. Conversely, every zombie session has aggregate measurements that pass each filter, so it is retained. Sorting by scroll count descending and then session identifier ascending establishes the required output order.

## Complexity detail

Let $N$ be the number of event rows and $S$ the number of session groups. Under a general comparison-based database plan, grouping can require $O(N\log N)$ work and ordering the retained groups costs $O(S\log S)$. Sort-based grouping can use $O(N+S)$ working space. A hash aggregate or suitable indexes may reduce practical costs, but the query does not depend on a particular execution plan.

The benchmark defines its size as $S$ and supplies seven events per session, so $N=7S$. The accepted strategy aggregates the table once. The calibrated principal slower alternative recomputes every session statistic with correlated full-table scans for each outer event row, yielding the same result but quadratic growth.

## Alternatives and edge cases

- **Floating-point ratio division:** Dividing click and scroll counts directly is readable, but integer cross-multiplication is exact and exposes the strict one-fifth boundary.
- **Correlated aggregate subqueries:** Separate subqueries can reproduce every statistic, but repeated scans for outer rows can grow quadratically.
- **Exactly 30 minutes:** The duration condition is strict, so a session lasting exactly 30 minutes is excluded.
- **Exactly five scrolls:** The scroll threshold is inclusive, so five scroll events are sufficient when all other criteria pass.
- **Exactly 0.20 clicks per scroll:** One click with five scrolls is excluded because equality does not satisfy a strict lower-than test.
- **Any purchase:** A single purchase disqualifies the session regardless of its duration or activity counts.
- **Unrelated event types and values:** Opens, closes, scroll distances, and purchase amounts do not change the conditional event counts beyond establishing timestamps.
- **Ordering ties:** Sessions with equal scroll counts must be ordered by `session_id` ascending.
