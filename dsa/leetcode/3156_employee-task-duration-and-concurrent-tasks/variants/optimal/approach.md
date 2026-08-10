## General

**Split time only where activity can change**

For one employee, the set of active tasks can change only at a task start or task end. Between two consecutive distinct boundary timestamps, no task begins or ends, so concurrency is constant throughout that entire elementary interval.

CTE `T` collects all starts and ends as the common column `st`. `UNION DISTINCT` removes duplicate boundaries, including times when several tasks begin or end together.

CTE `P` partitions boundaries by `employee_id`, orders them chronologically, and uses `LEAD(st)` to create the next boundary `ed`. Each row now represents elementary interval `[st, ed]` between adjacent event times. The final boundary has no successor and receives `NULL`.

**Count tasks covering each elementary interval**

CTE `S` joins each interval to every task of the same employee. Conditions

`P.st >= Tasks.start_time`

and

`P.ed <= Tasks.end_time`

retain a task only when it covers the complete elementary interval. Because all start and end times are boundaries, a task cannot cover merely part of such an interval. Coverage is all or nothing.

Grouping back by the three `P` columns counts the retained tasks. `concurrent_count` is therefore the number of simultaneously active tasks during that positive-duration segment.

Intervals not covered by any task disappear through the inner join. This is exactly what total active duration needs: idle gaps should not be added.

The last `P` row has `ed = NULL`. Comparisons involving that null are unknown, so it also produces no `S` row.

**Aggregate union duration and maximum concurrency**

Every surviving elementary interval belongs to the union of the employee's task intervals. The intervals are disjoint except at boundaries, so summing their durations counts each active second once, even if many tasks overlap there.

`TIMEDIFF(ed, st)` obtains the interval duration, `TIME_TO_SEC` converts it to seconds, and division by 3600 expresses hours. `SUM` combines all active segments. `FLOOR` is applied after the sum so partial hours from different segments can combine before the final downward rounding.

`MAX(concurrent_count)` returns the largest number of covering tasks among all elementary intervals.

The outer grouping produces one row per employee, and `ORDER BY 1` sorts by the first selected column, `employee_id`, ascending.

**Example of overlap handling**

For tasks 08:00–09:00 and 08:30–10:30, boundaries are 08:00, 08:30, 09:00, and 10:30. The elementary intervals have concurrency 1, 2, and 1. Their union duration is 30 + 30 + 90 = 150 minutes, not the separate-task total 180 minutes. Maximum concurrency is 2.

If a later task begins at 11:00, the idle interval 10:30–11:00 has coverage count zero and is absent from `S`, so it does not inflate total task time.


Every instant with positive-duration task coverage lies in exactly one elementary interval between consecutive boundaries. All tasks active there cover the interval fully and are counted by the join. Thus `concurrent_count` is exact.

The covered elementary intervals form a disjoint partition of the union of task durations, so summing them gives total time during which the employee handled at least one task. Taking the maximum of exact segment counts gives peak concurrency. Final conversion and floor implement the output unit.

**Endpoint convention**

The query measures concurrency over nonzero intervals. A task ending exactly when another starts does not create a shared positive-duration segment and is not counted as overlap. If “at any point” were intended to count an instantaneous closed-endpoint coincidence, a separate endpoint ordering convention would be required. Duration analytics normally treats task intervals as half-open for this purpose.

## Complexity detail

Let $r$ be the number of task rows and $b$ the number of distinct employee-boundary rows, with $b\le2r$.

Building, deduplicating, and ordering boundaries costs roughly $O(r\log r)$. However, the exact source is not the event-delta sweep described by the manifest. CTE `S` joins each elementary interval with tasks sharing its employee and tests containment.

For one employee with $r$ heavily overlapping tasks and $O(r)$ distinct intervals, the join can produce $\Theta(r^2)$ covered segment-task rows before grouping. A conservative worst-case time bound is $O(r^2+r\log r)=O(r^2)$, and intermediate working space may also reach $O(r^2)$ depending on the database plan.

Indexes and optimizer strategies can reduce practical work, but interval containment joins do not have a general $O(r\log r)$ guarantee. The manifest's $O(n\log n)$ time and $O(n)$ space belong to a true signed-event sweep, not this exact SQL.

The final result has at most one row per represented employee.

## Alternatives and edge cases

- **Signed event sweep:** Emit +1 at starts and -1 at ends, aggregate equal timestamps, and use cumulative concurrency. It can compute active duration and peak in $O(r\log r)$ without the quadratic containment join.
- **Merge intervals only:** Sorting and merging yields union duration but does not by itself preserve maximum concurrency.
- **Sum task durations:** Incorrect because overlap would be counted multiple times.
- **Duplicate boundary times:** `UNION DISTINCT` ensures they define one boundary rather than zero-length repeated segments.
- **Idle gaps:** They have no covering joined task and are excluded from total duration.
- **Nested tasks:** The inner segments receive higher covering counts while union duration remains counted once.
- **Back-to-back tasks:** They form continuous active duration but no positive-duration concurrency of two.
- **Several tasks with identical intervals:** Each joins the same segments, so concurrency equals their multiplicity.
- **Partial hours:** Durations are summed before `FLOOR` so fractions can combine.
- **Final boundary:** Its null `ed` cannot form a segment and drops from the containment join.
- **Employees remain separate:** Every window and join is partitioned or keyed by `employee_id`.
- **Long MySQL time differences:** `TIMEDIFF`/`TIME_TO_SEC` behavior should be checked if task spans exceed MySQL's TIME range; the local statement provides no such extreme example.
