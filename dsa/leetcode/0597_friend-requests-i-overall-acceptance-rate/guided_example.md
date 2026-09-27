# Guided Example: Friend Requests I: Overall Acceptance Rate

Two event logs sit side by side. `FriendRequest` records the moments when one user asked another to connect; `RequestAccepted` records the moments when such an invitation was accepted. Neither relation carries a primary key — the contract says plainly that both may hold duplicates — so a single relationship can generate several request rows and several acceptance rows on different dates. The requested figure is the *overall acceptance rate*: the number of accepted relationships divided by the number of requested relationships, rounded to two decimal places, with the stated convention that a log holding no requests at all reports `0.00`.

The work below uses the official logs. They are ideal for teaching because the two relations have the same raw row count while their deduplicated counts differ — the exact situation in which a careless formulation produces a confidently wrong number.

## 1. Instance, Contract, and the Metric

The request log:

| `sender_id` | `send_to_id` | `request_date` |
|:---:|:---:|:---|
| $1$ | $2$ | `2016/06/01` |
| $1$ | $3$ | `2016/06/01` |
| $1$ | $4$ | `2016/06/01` |
| $2$ | $3$ | `2016/06/02` |
| $3$ | $4$ | `2016/06/09` |

The acceptance log:

| `requester_id` | `accepter_id` | `accept_date` |
|:---:|:---:|:---|
| $1$ | $2$ | `2016/06/03` |
| $1$ | $3$ | `2016/06/08` |
| $2$ | $3$ | `2016/06/08` |
| $3$ | $4$ | `2016/06/09` |
| $3$ | $4$ | `2016/06/10` |

The required output:

| `accept_rate` | Derivation |
|:---:|:---|
| $0.80$ | Four distinct accepted pairs against five distinct requested pairs |

### The rules the contract fixes

- **Duplicates collapse.** If a sender asks the same receiver repeatedly, or a request is accepted more than once, the repeated events contribute **one** unit to the metric, not several.
- **The two sides are counted independently.** An accepted relationship need not appear in the request log at all. The numerator and the denominator are separate aggregates; the metric is a ratio, not an intersection.
- **Orientation is part of a pair's identity.** $(u, v)$ and $(v, u)$ are different pairs, because a request travels from sender to receiver.
- **Zero denominator.** With no requests recorded, the rate is defined as $0.00$ rather than an error or a null. The result is rounded to two decimals.

## 2. Independent Aggregation: Why the Two Relations Are Never Joined

The most seductive wrong answer joins the logs on the user pair and then counts matched rows. That formulation quietly substitutes an intersection for a ratio, and the substitution is visible in the data above: the acceptance of $(3,4)$ on `2016/06/09` and again on `2016/06/10` is a relationship between the same two users, but the metric never asks whether the request log contains it — it asks how large each side is.

| Candidate counting rule | Numerator | Denominator | Duplicates counted? | Result on this instance |
|:---|:---|:---|:---|:---|
| Raw row counts | $5$ | $5$ | Yes, twice over | $1.00$ — wrong |
| Distinct directed pairs, counted independently | $4$ | $5$ | No | $0.80$ — correct |
| Pairs surviving an equality join across both logs | Intersection size | Intersection size | No | $1.00$ — and structurally wrong |
| Distinct users involved | Distinct users | Distinct users | Irrelevant | $1.00$ — ignores which user paired with which |

The third row deserves emphasis: pairing the relations on the shared user columns discards exactly the accepted pairs that have no surviving request row, so it cannot represent the metric even in principle. The fourth row loses the pairing itself; a user with several distinct partners would be collapsed into a single unit.

## 3. Dyadic Deduplication Invariant

Let $R$ be the multiset of request rows and $A$ the multiset of acceptance rows, with $R$ and $A$ as their respective row counts. Project each row onto its ordered user pair and then collapse the resulting multiset to a set:

$$
P_{req} = \{\, (r.\text{sender\_id},\; r.\text{send\_to\_id}) \;\mid\; r \in R \,\},
\qquad
P_{acc} = \{\, (a.\text{requester\_id},\; a.\text{accepter\_id}) \;\mid\; a \in A \,\}.
$$

Write $N_{req} = \lvert P_{req} \rvert$ and $N_{acc} = \lvert P_{acc} \rvert$. The metric is then

$$
\text{accept\_rate} \;=\; \operatorname{round}\!\left( \frac{N_{acc}}{N_{req}},\; 2 \right),
\qquad N_{req} > 0 .
$$

> **Deduplication invariant.** Two event rows that project to the same ordered pair denote the same relationship and therefore contribute exactly one element to the corresponding set. Timestamps influence neither $P_{req}$ nor $P_{acc}$; they are payload carried alongside the pair and dropped by the projection.

The projection is the load-bearing step. Because it is applied *before* counting, the count is a set cardinality, and a set cardinality is invariant under any repetition or reordering of the rows that produced it. That is why the duplicate acceptance on two consecutive days cannot inflate the numerator, and why the answer does not change if the log rows are shuffled.

## 4. Worked Evaluation of the Official Logs

**Step 1 — Project the request log onto ordered pairs and collapse.**

| Request row | Projected pair | Already present? | $N_{req}$ after the row |
|:---|:---:|:---:|:---:|
| `(1, 2, "2016/06/01")` | $(1, 2)$ | No | $1$ |
| `(1, 3, "2016/06/01")` | $(1, 3)$ | No | $2$ |
| `(1, 4, "2016/06/01")` | $(1, 4)$ | No | $3$ |
| `(2, 3, "2016/06/02")` | $(2, 3)$ | No | $4$ |
| `(3, 4, "2016/06/09")` | $(3, 4)$ | No | $5$ |

Five request rows, five distinct pairs, so $N_{req} = 5$.

**Step 2 — Project the acceptance log the same way.**

| Acceptance row | Projected pair | Already present? | $N_{acc}$ after the row |
|:---|:---:|:---:|:---:|
| `(1, 2, "2016/06/03")` | $(1, 2)$ | No | $1$ |
| `(1, 3, "2016/06/08")` | $(1, 3)$ | No | $2$ |
| `(2, 3, "2016/06/08")` | $(2, 3)$ | No | $3$ |
| `(3, 4, "2016/06/09")` | $(3, 4)$ | No | $4$ |
| `(3, 4, "2016/06/10")` | $(3, 4)$ | **Yes — collapses onto the previous row** | $4$ |

Five acceptance rows but only four distinct pairs, so $N_{acc} = 4$. The fifth row is absorbed by the fourth because nothing in the pair distinguishes them.

**Step 3 — Form the ratio and round.**

$$
\text{accept\_rate} = \frac{N_{acc}}{N_{req}} = \frac{4}{5} = 0.8
\;\longrightarrow\;
\operatorname{round}(0.8,\, 2) = 0.80 .
$$

| Quantity | Symbol | Value | Note |
|:---|:---:|:---:|:---|
| Request rows read | $R$ | $5$ | Raw event count |
| Distinct requested pairs | $N_{req}$ | $5$ | Denominator of the metric |
| Acceptance rows read | $A$ | $5$ | Raw event count |
| Distinct accepted pairs | $N_{acc}$ | $4$ | Numerator of the metric |
| Final reported rate | — | $0.80$ | Two-decimal rounding of $4/5$ |

The coincidence $R = A = 5$ is exactly the trap: a formulation that counts rows never notices that the two logs are not comparable at that granularity.

## 5. Zero-Denominator and Rounding Boundaries

| Situation | $N_{req}$ | $N_{acc}$ | Naive quotient | Reported value | Reason |
|:---|:---:|:---:|:---:|:---:|:---|
| Empty request log | $0$ | anything | Division by zero | `0.00` | The contract defines the empty-denominator case explicitly |
| Requests but no acceptances | $5$ | $0$ | $0$ | $0.00$ | Legitimate zero numerator |
| Accepted pair absent from the request log | $1$ | $2$ | $2.0$ | $2.00$ | The numerator is independent and may exceed the denominator |
| Fraction needing a round | $3$ | $2$ | $0.666\ldots$ | $0.67$ | Round *after* dividing, never before |
| Exact two-decimal case | $5$ | $4$ | $0.8$ | $0.80$ | Trailing zero is part of the required formatting |

Two boundary facts are worth stating precisely. The rate is not constrained to the unit interval: an acceptance may exist without a corresponding request row in this log, so a rate above $1$ is a legitimate output rather than a data error. And rounding is a single terminal operation applied to the finished quotient; rounding the numerator or denominator first would change the result for fractions such as $2/3$.

## 6. Elimination of Tempting Alternatives

| Alternative | Why it attracts | Why it fails or costs more |
|:---|:---|:---|
| Joining the two logs on the user pair | Reuses one familiar join to "match" requests with acceptances | Computes an intersection, silently dropping accepted pairs that never appear as requests and altering the numerator |
| Counting raw rows on both sides | One aggregate per relation, no deduplication step | The final acceptance row above would inflate the numerator to $5$, yielding $1.00$ instead of $0.80$ |
| Deduplicating dates as well as pairs | Treats each day's event as separate | Directly contradicts the rule that repeated events between the same pair count once |
| Dividing with integer arithmetic | Natural when both counts are integers | Truncates $4/5$ to $0$; the ratio must be formed in a fractional domain |
| Omitting the empty-log guard | The data usually has requests | An empty request log is an explicitly listed case, and the unguarded quotient is not a number |
| Counting distinct users rather than distinct pairs | Simpler key to reason about | Loses the pairing: distinct users in the request log number $4$, not $5$ |

A natural extension of this instance — the follow-up the statement raises — groups the same two logs by calendar month or running day and reports one rate per bucket. The aggregation structure is unchanged; only the partition key changes from "the whole table" to "the month" or "the day up to now". Recognizing that the metric is a ratio of two independent pair sets is what makes the extension mechanical.

## 7. Cost of the Method

Let $R$ and $A$ denote the row counts of the two logs, and let $N_{req}$ and $N_{acc}$ be the distinct-pair counts derived above, so $N_{req} \le R$ and $N_{acc} \le A$.

**Time complexity.** Each relation is scanned once, and each row performs a single hash-set probe on its ordered pair: $O(R)$ expected for the request log and $O(A)$ expected for the acceptance log. Forming the quotient and rounding it are constant work. Total:

$$
O(R) + O(A) + O(1) = O(R + A).
$$

The deduplication is not a separate pass — it is the probe itself, so no sort is required; a sort-based distinct would instead cost $O(R \log R + A \log A)$.

**Auxiliary-space complexity.** The method keeps one hash entry per distinct pair, so the sets $P_{req}$ and $P_{acc}$ occupy $O(N_{req} + N_{acc})$ and therefore $O(R + A)$ in the worst case, when every row is unique. This is genuine working memory proportional to the *distinct* relationships rather than to the raw row count — a log that repeats the same pair a million times still stores only one entry for it. Trimming the memory further is possible by counting one side first and streaming the other, but the bound remains $O(R + A)$ because the larger distinct-pair set must be retained to be probed.
