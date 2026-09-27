# Guided Example: Merge Overlapping Events in the Same Hall

## 1. The instance and the exact overlap rule

The table `HallEvents` records one row per scheduled event, with a `hall_id`, a
`start_day`, and an `end_day`. Duplicate rows are allowed, and a hall may hold any
number of events. Two events **overlap** when they share at least one calendar day,
and both `start_day` and `end_day` are inclusive endpoints, so an event running from
day $s$ to day $e$ occupies every day in the closed interval $[s, e]$. Events held
in different halls never overlap, no matter how their dates line up: merging is
performed *inside* each hall independently.

The task is to replace, for each hall, every maximal chain of overlapping events by
a single event spanning from the earliest start to the latest end in that chain. The
output has one row per resulting event, with the same three columns, in any order.

We trace the official instance:

| `hall_id` | `start_day` | `end_day` |
|:---|:---|:---|
| 1 | `2023-01-13` | `2023-01-14` |
| 1 | `2023-01-14` | `2023-01-17` |
| 1 | `2023-01-18` | `2023-01-25` |
| 2 | `2022-12-09` | `2022-12-23` |
| 2 | `2022-12-13` | `2022-12-17` |
| 3 | `2022-12-01` | `2023-01-30` |

The expected result collapses this to four rows:

| `hall_id` | `start_day` | `end_day` |
|:---|:---|:---|
| 1 | `2023-01-13` | `2023-01-17` |
| 1 | `2023-01-18` | `2023-01-25` |
| 2 | `2022-12-09` | `2022-12-23` |
| 3 | `2022-12-01` | `2023-01-30` |

This instance is a good representative because it contains, in one table, an exact
endpoint touch (`2023-01-14`), a nested event (`2022-12-13`–`2022-12-17` lies inside
`2022-12-09`–`2022-12-23`), a genuine one-day gap (`2023-01-17` to `2023-01-18`),
and a hall with a single event. Those four situations are precisely where naive
merging goes wrong.

## 2. Overlap is a fact about parity of coverage, not about adjacency of rows

The relation "shares at least one day" is a relation on day sets, not on row order.
Two consequences drive the whole method.

**First, overlap is not transitive, but chains are what we must report.** If event
$A$ overlaps $B$ and $B$ overlaps $C$, $A$ need not overlap $C$ directly: in hall 4
of the authored trials, `2024-06-01`–`2024-06-20` and `2024-06-15`–`2024-06-25`
overlap, and so do `2024-06-15`–`2024-06-25` and `2024-06-02`–`2024-06-03`, yet the
last two share no day. The required output is still a single span, because the
merged day set of a connected chain is the union of its intervals, and that union is
again one interval.

**Second, the union of overlapping intervals is an interval.** For any family of
intervals whose union is connected, the union equals the closed span from the
smallest start to the largest end. Merging therefore never needs to remember the
individual events of a chain; it needs only two numbers per chain: the minimum start
seen so far and the maximum end seen so far. That is the reduction that makes a
single ordered sweep sufficient.

## 3. Sorting inside a hall turns merging into one sweep

Order the rows of one hall by `start_day` ascending. Process them left to right and
keep a running maximum

$$
M_i = \max\{\, \text{end\_day}_j : j \le i \,\},
$$

the latest end day seen among the first $i$ rows of that hall's ordering. The row at
position $i$ (with $i \ge 2$) continues the current chain exactly when

$$
\text{start\_day}_i \le M_{i-1}.
$$

The reasoning is a one-line exchange. Because rows are sorted by start, the current
chain occupies at least the day interval $[\text{start of the chain}, M_{i-1}]$; by
definition of the running maximum, no earlier row of the chain reaches beyond
$M_{i-1}$, and every earlier row starts no later than the chain's first start. So the
chain's coverage is exactly that interval, and asking whether row $i$ touches it is
the same as asking whether $\text{start\_day}_i \le M_{i-1}$. Equality counts as an
overlap, because day $M_{i-1}$ itself is shared.

Choosing $i = 1$ always opens a chain: it has no predecessor, so it starts the first
island of its hall. Every later row either joins the open island or opens the next
one, and the island identifier of a row is simply the number of openings up to and
including that row.

## 4. Worked trace on the official instance

Rows are grouped by hall first, then sorted by `start_day` inside the hall. The
column $M_{i-1}$ is the running maximum *before* the row is considered; the last
column is the running maximum *after* it. A row with no predecessor in its hall has
nothing to compare against and must open an island.

| `hall_id` | row in hall order | `start_day` | `end_day` | $M_{i-1}$ | `start_day` $\le M_{i-1}$? | island id | $M_i$ |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | `2023-01-13` | `2023-01-14` | none | opens the first island | 1 | `2023-01-14` |
| 1 | 2 | `2023-01-14` | `2023-01-17` | `2023-01-14` | yes, shares `2023-01-14` | 1 | `2023-01-17` |
| 1 | 3 | `2023-01-18` | `2023-01-25` | `2023-01-17` | no, one-day gap | 2 | `2023-01-25` |
| 2 | 1 | `2022-12-09` | `2022-12-23` | none | opens the first island | 1 | `2022-12-23` |
| 2 | 2 | `2022-12-13` | `2022-12-17` | `2022-12-23` | yes, nested inside the island | 1 | `2022-12-23` |
| 3 | 1 | `2022-12-01` | `2023-01-30` | none | opens the first island | 1 | `2023-01-30` |

Two rows deserve attention. Hall 1 row 3 starts on `2023-01-18`, exactly one day
after the running maximum `2023-01-17`; the strict gap breaks the chain, and because
rows are sorted by start, every later row of hall 1 would also start after
`2023-01-17`, so nothing can repair the split afterwards. Hall 2 row 2 is nested:
its `end_day` is smaller than the running maximum, so $M_i$ does not change, which
is exactly why the running maximum must be a maximum and not merely the previous
row's `end_day`.

Projecting each island to its span gives the answer rows:

| `hall_id` | island id | rows folded in | minimum `start_day` | maximum `end_day` | output row |
|:---|:---|:---|:---|:---|:---|
| 1 | 1 | rows 1 and 2 | `2023-01-13` | `2023-01-17` | `1, 2023-01-13, 2023-01-17` |
| 1 | 2 | row 3 | `2023-01-18` | `2023-01-25` | `1, 2023-01-18, 2023-01-25` |
| 2 | 1 | rows 1 and 2 | `2022-12-09` | `2022-12-23` | `2, 2022-12-09, 2022-12-23` |
| 3 | 1 | row 1 | `2022-12-01` | `2023-01-30` | `3, 2022-12-01, 2023-01-30` |

The result matches the expected four rows exactly. An island is identified by the
pair (hall, island id), so identical island numbers in different halls never mix:
island 1 of hall 1 and island 1 of hall 3 are separate output rows.

## 5. Invariant and correctness of the sweep

**Invariant (per hall, after processing the first $i$ rows).** The completed islands
are exactly the maximal overlapping chains of those $i$ rows, each represented by
its span $[\min \text{start}, \max \text{end}]$; the open island is represented by
the pair (first start of the island, $M_i$); and $M_i$ is the maximum `end_day` over
all $i$ processed rows.

**Maintenance.** Sorting guarantees $\text{start\_day}_i \ge \text{start\_day}_{i-1}$,
so row $i$ cannot start before the open island and cannot extend the island's
minimum start. If $\text{start\_day}_i \le M_{i-1}$, the interval
$[\text{start\_day}_i, M_{i-1}]$ is non-empty and lies inside both row $i$ and the
open island, so the two share at least one day: row $i$ joins the open island, and
the new maximum is $\max(M_{i-1}, \text{end\_day}_i)$. If instead
$\text{start\_day}_i > M_{i-1}$, row $i$ is disjoint from the open island's interval.

**Maximality (no chain is split).** Suppose the sweep closes an island at row $i$.
Then $\text{start\_day}_i > M_{i-1}$, and every row $j \ge i$ has
$\text{start\_day}_j \ge \text{start\_day}_i > M_{i-1}$, so no later row overlaps any
day of the closed island. Closing it is therefore forced, not a heuristic.

**Completeness (no chain is over-extended).** Rows are joined only after the
inequality proves a shared day, so no island contains two rows that fail to overlap
the island's interval. Since the union of overlapping intervals in a chain is a
single interval, reporting the span loses nothing: every day between the minimum
start and the maximum end is covered by some merged event.

Together these two directions show the output is exactly one row per maximal chain,
which is the required result. Only the two aggregates $\min \text{start}$ and
$\max \text{end}$ are needed per island, so the running maximum is sufficient state
and no pairwise overlap test between non-adjacent rows is ever required.

## 6. Boundaries and traps

Each trial case in the package isolates one boundary behaviour. The table states the
dates involved, the verdict under the rule $\text{start\_day}_i \le M_{i-1}$, and
the output.

| Situation | Dates involved | Verdict | Output |
|:---|:---|:---|:---|
| Exact endpoint touch | `2024-04-01`–`2024-04-03` then `2024-04-03`–`2024-04-09` | overlap, day `2024-04-03` is shared | one row `2024-04-01`–`2024-04-09` |
| Consecutive calendar days | `2024-05-01`–`2024-05-02` then `2024-05-03`–`2024-05-04` | no shared day | two rows, unchanged |
| Duplicate identical rows | `2024-03-10`–`2024-03-12` twice | overlap on every day | one row `2024-03-10`–`2024-03-12` |
| Nested short event | `2024-06-01`–`2024-06-20`, `2024-06-02`–`2024-06-03`, `2024-06-15`–`2024-06-25`, `2024-06-30`–`2024-07-01` | the middle rows do not lower the running maximum | rows `2024-06-01`–`2024-06-25` and `2024-06-30`–`2024-07-01` |
| Equal `start_day`, different `end_day` | `2024-07-01`–`2024-07-02`, `2024-07-01`–`2024-07-10`, `2024-07-09`–`2024-07-12` | ties order arbitrarily but all join | one row `2024-07-01`–`2024-07-12` |
| Same dates, different halls | hall 8 `2024-08-01`–`2024-08-05` with `2024-08-04`–`2024-08-07`; hall 9 `2024-08-02`–`2024-08-03` and `2024-08-10`–`2024-08-11` | hall 8 merges, hall 9 does not | `8, 2024-08-01, 2024-08-07` plus two hall-9 rows |
| Single-event hall | `2022-12-01`–`2023-01-30` | trivially one island | the row is returned unchanged |

The comparison table below contrasts the correct rule with the plausible shortcuts
that the boundary rows above are designed to catch.

| Alternative strategy | Behaviour on this package's cases | Why it fails or is unnecessary |
|:---|:---|:---|
| Carry the previous row's `end_day` instead of the running maximum | splits `2024-06-15` away from `2024-06-01`–`2024-06-20` | a nested event lowers the remembered end, so a later genuine overlap looks like a gap |
| Use strict `<` for the overlap test | splits the touching pair `2024-04-03` | an inclusive `end_day` means the boundary day is shared, so equality is overlap |
| Ignore `hall_id` while ordering | merges hall 8 dates with hall 9 dates | events in different halls can never overlap |
| Self-join every overlapping pair, then group transitively | correct but quadratic in the row count | overlap is not transitive, so the union span must be computed, and the join cost is far larger than one ordered sweep |
| One output row per hall using global min and max | turns hall 1 into `2023-01-13`–`2023-01-25` | it bridges the real `2023-01-17` to `2023-01-18` gap and loses an island |

## 7. Complexity: time and auxiliary space

Let $N$ be the number of rows in `HallEvents`. Each phase of the method has a
distinct cost, and the sort dominates everything else.

| Phase | Work | Cost |
|:---|:---|:---|
| Ordering rows by `hall_id` then `start_day` | comparison sort of $N$ rows | $O(N \log N)$ |
| Running maximum of `end_day` per hall | one ordered pass over the sorted rows | $O(N)$ |
| Island-opening test and island numbering | one ordered pass, constant work per row | $O(N)$ |
| Grouping islands into `min start` and `max end` | one pass, aggregation keyed by (hall, island) | $O(N)$ amortised |

Total time is therefore

$$
O(N \log N),
$$

with the window passes contributing only linear work. Date comparisons are constant
time, so they do not affect the bound. No cross join, recursion, or repeated
pairwise overlap test is used, which is what keeps the method near-linear even when
a hall holds thousands of events.

Auxiliary space is $O(N)$: the sorted copy of the table carries every input row once,
and each row needs only a constant number of derived values (the running maximum,
the opening flag, and the island identifier). The final aggregation keeps at most one
accumulator per island, which is again bounded by $N$. If the ordering is provided
by an index, the explicit copy can be avoided, but the asymptotic auxiliary space
remains $O(N)$ in the worst case.
