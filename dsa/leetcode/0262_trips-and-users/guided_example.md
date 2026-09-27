# Guided Example: Trips and Users

## 1. The Daily Cancellation-Rate Task and Its Instance

Two relations describe a ride-hailing service. `Trips` holds one row per trip
request, with a unique `id`, a `client_id` and a `driver_id` that are both foreign
keys into `Users`, a `city_id`, a `status` drawn from the enumerated outcomes
`completed`, `cancelled_by_client`, and `cancelled_by_driver`, and a `request_at`
date string. `Users` holds one row per account, keyed by `users_id`, with a `banned`
flag whose values are `Yes` and `No` and a `role` whose values are `client`,
`driver`, and `partner`.

For each day in the inclusive window from `2013-10-01` through `2013-10-03` that has
at least one qualifying request, the task asks for the fraction of qualifying
requests that were cancelled by either party, rounded to two decimal places. A
request qualifies only when **both** its client and its driver are unbanned.

| `id` | `client_id` | `driver_id` | `city_id` | `status` | `request_at` |
|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 1 | 10 | 1 | `completed` | `2013-10-01` |
| 2 | 2 | 11 | 1 | `cancelled_by_driver` | `2013-10-01` |
| 3 | 3 | 12 | 6 | `completed` | `2013-10-01` |
| 4 | 4 | 13 | 6 | `cancelled_by_client` | `2013-10-01` |
| 5 | 1 | 10 | 1 | `completed` | `2013-10-02` |
| 6 | 2 | 11 | 6 | `completed` | `2013-10-02` |
| 7 | 3 | 12 | 6 | `completed` | `2013-10-02` |
| 8 | 2 | 12 | 12 | `completed` | `2013-10-03` |
| 9 | 3 | 10 | 12 | `completed` | `2013-10-03` |
| 10 | 4 | 13 | 12 | `cancelled_by_driver` | `2013-10-03` |

| `users_id` | `banned` | `role` |
|:---:|:---:|:---|
| 1 | `No` | `client` |
| 2 | `Yes` | `client` |
| 3 | `No` | `client` |
| 4 | `No` | `client` |
| 10 | `No` | `driver` |
| 11 | `No` | `driver` |
| 12 | `No` | `driver` |
| 13 | `No` | `driver` |

Account 2 is the single banned participant in this instance, and it appears as the
client of trips 2, 6, and 8. Those three trips are the interesting part of the
example: each one is cancelled nowhere near the day's true rate, so a solution that
forgets to check the ban flag will produce visibly wrong numbers.

The required output is:

| `Day` | `Cancellation Rate` |
|:---:|:---:|
| `2013-10-01` | `0.33` |
| `2013-10-02` | `0.00` |
| `2013-10-03` | `0.50` |

## 2. Eligibility: Two Independent Ban Checks

Each trip row contains *two* foreign keys into the same `Users` relation. They
answer different questions, so both must be resolved independently: one lookup
identifies the client row, and a second, separate lookup identifies the driver row.
Reading `Users` once cannot serve both roles, because a single row of `Users`
describes only one account.

Define the eligibility predicate for a trip $t$ as the conjunction of three
conditions:

1. the account referenced by $t.\text{client\_id}$ exists and has
   $\text{banned} = \text{No}$;
2. the account referenced by $t.\text{driver\_id}$ exists and has
   $\text{banned} = \text{No}$; and
3. $t.\text{request\_at}$ lies in the inclusive window
   $[\,\texttt{2013-10-01},\, \texttt{2013-10-03}\,]$.

Because the stored dates are fixed-width ISO strings of the form `YYYY-MM-DD`, their
lexical order coincides with chronological order, so the inclusive string range and
the inclusive calendar range describe the same set of days.

For an eligible trip, define a cancellation indicator

$$\text{cancel}(t) = \begin{cases} 1 & \text{if } t.\text{status} \ne \texttt{completed},\\[2pt] 0 & \text{if } t.\text{status} = \texttt{completed}.\end{cases}$$

The allowed status values make "not completed" exactly equivalent to "cancelled by
one of the two parties", so the indicator needs no separate enumeration of the two
cancellation labels. The daily rate is the average of that indicator over the
eligible trips of the day:

$$\text{rate}(d) = \frac{1}{\lvert E(d) \rvert} \sum_{t \in E(d)} \text{cancel}(t),$$

where $E(d)$ is the set of eligible trips whose `request_at` equals $d$. Rounding the
average to two decimals gives the reported value.

> **Invariant.** The numerator and the denominator of every reported rate are drawn
> from the *same* eligible row set $E(d)$. A trip involving a banned participant is
> removed from the row set entirely, so it can never enlarge the denominator while
> contributing nothing to the numerator.

That invariant is the whole point of the instance. Excluding banned trips only from
the numerator would inflate the denominator of every day that contains one, which is
exactly what the sample data is built to expose.

## 3. Worked Trace of Eligibility Filtering

Resolve the two foreign keys for each trip and test the window.

| Trip | Date | Client | Client banned? | Driver | Driver banned? | In window? | Eligible? | Status | Indicator |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `2013-10-01` | 1 | `No` | 10 | `No` | yes | **yes** | `completed` | 0 |
| 2 | `2013-10-01` | 2 | `Yes` | 11 | `No` | yes | no — banned client | `cancelled_by_driver` | dropped |
| 3 | `2013-10-01` | 3 | `No` | 12 | `No` | yes | **yes** | `completed` | 0 |
| 4 | `2013-10-01` | 4 | `No` | 13 | `No` | yes | **yes** | `cancelled_by_client` | 1 |
| 5 | `2013-10-02` | 1 | `No` | 10 | `No` | yes | **yes** | `completed` | 0 |
| 6 | `2013-10-02` | 2 | `Yes` | 11 | `No` | yes | no — banned client | `completed` | dropped |
| 7 | `2013-10-02` | 3 | `No` | 12 | `No` | yes | **yes** | `completed` | 0 |
| 8 | `2013-10-03` | 2 | `Yes` | 12 | `No` | yes | no — banned client | `completed` | dropped |
| 9 | `2013-10-03` | 3 | `No` | 10 | `No` | yes | **yes** | `completed` | 0 |
| 10 | `2013-10-03` | 4 | `No` | 13 | `No` | yes | **yes** | `cancelled_by_driver` | 1 |

Every row of this instance falls inside the window, so the date predicate removes
nothing; the work is done entirely by the two ban predicates. Trip 2 is instructive
twice over: it is a cancellation, so keeping it would push the first day's rate from
$1/3$ to $2/4 = 0.50$; and its client is banned, so the row must vanish from both
the numerator and the denominator.

## 4. Daily Aggregation of the Cancellation Indicator

Group the surviving rows by `request_at` and average the indicator within each
group.

| Day $d$ | Eligible trips | Indicators | $\sum \text{cancel}$ | $\lvert E(d) \rvert$ | Exact average | Rounded |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `2013-10-01` | 1, 3, 4 | $0, 0, 1$ | 1 | 3 | $\tfrac{1}{3} = 0.333\ldots$ | `0.33` |
| `2013-10-02` | 5, 7 | $0, 0$ | 0 | 2 | $\tfrac{0}{2} = 0.00$ | `0.00` |
| `2013-10-03` | 9, 10 | $0, 1$ | 1 | 2 | $\tfrac{1}{2} = 0.50$ | `0.50` |

Two details in this table are worth naming. First, a day whose eligible trips are all
completed yields an average of exactly zero rather than an absent value: the
denominator is positive and the numerator is zero, so the day is reported as `0.00`.
Second, the grouping key is the date value itself, so a day with no eligible trip
simply produces no group and therefore no output row. No calendar table and no
artificial zero row are needed; the requirement to report only days with at least
one request is satisfied automatically by grouping the surviving rows.

## 5. Why the Reasoning Is Correct

**Soundness of the denominator.** Every row in $E(d)$ has been shown to possess an
unbanned client row and an unbanned driver row, so the denominator counts exactly the
trips the statement calls requests with unbanned users. No banned-participant trip
can reach the aggregation stage, because the failing ban predicate eliminates its
row rather than merely marking it.

**Soundness of the numerator.** A row contributes one exactly when its status differs
from `completed`. The enumerated status domain contains precisely two other values,
and both mean the trip was cancelled by one of the two parties, so the numerator
counts exactly the cancelled eligible requests of that day.

**Completeness.** Suppose a day $d$ in the window contains at least one trip whose
client and driver are both unbanned. That trip's row satisfies all three eligibility
conditions, so it enters $E(d)$, and the group for $d$ exists and is reported. Every
such day is therefore returned, and no day outside the window can enter because the
window predicate is part of eligibility.

**Why the ratio is well defined.** The grouping key is constant within a group by
construction, so all rows averaged together share one date. The denominator is the
size of a set that contains at least one row, hence never zero, so no division by
zero or undefined average can occur.

## 6. Traps This Instance Exposes

| Trap | What the instance shows | Why it is wrong |
|:---|:---|:---|
| Checking only the client, or only the driver | Account 2 is banned and is always a client here, so omitting the driver check would not change this particular output | The contract requires *both* participants to be unbanned; a banned driver alone must remove the trip, as the authored trial inputs demonstrate |
| Reading `Users` once for both roles | A trip needs the client row and the driver row at the same time | One row of `Users` describes one account, so the relation must be consulted under two distinct roles |
| Removing banned trips from the numerator only | Trip 2, a cancellation with a banned client, sits on the first day | The denominator must shrink too, otherwise the first day reports $2/4$ instead of $1/3$ |
| Counting both cancellation statuses as two units | Trips 4 and 10 are cancelled by different parties | Either cancellation contributes exactly one to the numerator; the rate is a fraction of trips, not of parties |
| Treating `completed` as the only unaffected value but relying on ordering | The status domain is an enumeration, not a numeric scale | Membership in the "completed" value is the only distinction that matters |
| Enumerating every calendar day in the window | Day groups come from surviving rows | A day with no eligible request must not appear, and a day with eligible requests must appear exactly once |
| Reversing or stretching the window | `BETWEEN` is inclusive at both ends | `2013-10-01` and `2013-10-03` themselves qualify; an exclusive bound would drop a required day |
| Forgetting to round | The first day's exact average is a repeating decimal | The reported value must carry two decimal places, so `0.333…` is reported as `0.33` |
| Expecting a particular row order | The contract permits any order | Without an explicit ordering, the engine may return days in any sequence |

## 7. Complexity Derivation

Let $t$ be the number of rows in `Trips` and $u$ the number of rows in `Users`. The
physical cost of a relational plan depends on the optimizer, the available indexes,
and the chosen join order, so the bounds below are the representative ones recorded
in the package manifest and are stated as the cost of a typical plan.

- **Eligibility resolution.** `users_id` is the primary key of `Users`, so resolving
  one foreign key is a single keyed lookup. A trip needs two such lookups, one for
  the client and one for the driver. With a B-tree primary-key index each lookup is
  $O(\log u)$, giving $O(t \log u)$ for the eligibility phase; a hash-based access
  path makes each lookup expected $O(1)$ and the phase expected $O(t)$ instead.
- **Window filtering.** Testing the inclusive date range is a constant number of
  string comparisons per row, so the filter is $\Theta(t)$ and does not change the
  asymptotic class. An index on `request_at` can reduce the number of rows actually
  read, since the engine can then seek directly to the qualifying date range.
- **Grouping and aggregation.** Each surviving row belongs to exactly one date group,
  and there are only three candidate dates in the window. Maintaining the running sum
  and count per group is $O(1)$ work per row, so hash aggregation is expected
  $O(t)$; sort-based grouping is $O(t \log t)$ because it orders the surviving rows
  by date first. The final division and rounding of one value per group is $O(g)$
  where $g \le 3$ is the number of reported days, which is asymptotically negligible.
- **Total time.** $O(t \log u)$ for a nested-loop plan over an indexed primary key,
  or expected $O(t)$ with hash access paths. Both are linear in the trip count up to
  the logarithm of the user count.
- **Auxiliary space.** The already-stored tables and indexes are not working memory.
  A hash plan may build $O(u)$ join state or an $O(t)$ hash table for grouping, so
  the manifest records the conservative $O(t)$ bound; a plan that probes indexes
  directly and streams the surviving rows uses only $O(g)$ accumulator space. The
  output itself holds one row per reported day.
