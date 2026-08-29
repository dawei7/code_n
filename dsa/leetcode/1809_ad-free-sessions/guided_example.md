# Guided Example: Ad-Free Sessions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Playback": [{"session_id": 1, "customer_id": 1, "start_time": 1, "end_time": 5}, {"session_id": 2, "customer_id": 1, "start_time": 15, "end_time": 23}, {"session_id": 3, "customer_id": 2, "start_time": 10, "end_time": 12}, {"session_id": 4, "customer_id": 2, "start_time": 17, "end_time": 28}, {"session_id": 5, "customer_id": 2, "start_time": 2, "end_time": 8}], "Ads": [{"ad_id": 1, "customer_id": 1, "timestamp": 5}, {"ad_id": 2, "customer_id": 2, "timestamp": 15}, {"ad_id": 3, "customer_id": 2, "timestamp": 20}]}}`
- **Required output:** `{"columns": ["session_id"], "rows": [[2], [3], [5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Playback`

The objective is to compute `{"columns": ["session_id"], "rows": [[2], [3], [5]]}` from `{"tables": {"Playback": [{"session_id": 1, "customer_id": 1, "start_time": 1, "end_time": 5}, {"session_id": 2, "customer_id": 1, "start_time": 15, "end_time": 23}, {"session_id": 3, "customer_id": 2, "start_time": 10, "end_time": 12}, {"session_id": 4, "customer_id": 2, "start_time": 17, "end_time": 28}, {"session_id": 5, "customer_id": 2, "start_time": 2, "end_time": 8}], "Ads": [{"ad_id": 1, "customer_id": 1, "timestamp": 5}, {"ad_id": 2, "customer_id": 2, "timestamp": 15}, {"ad_id": 3, "customer_id": 2, "timestamp": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: First identify sessions that did show an ad

The desired rows are sessions with no matching ad. The protected query solves the complementary problem in its subquery: find every `session_id` for which at least one ad belongs to the same customer and occurred during the session.

It joins `Playback AS p` to `Ads AS a` with two conditions:

1. `p.customer_id = a.customer_id` ensures an ad is attributed only to the customer who saw it;
2. `a.timestamp BETWEEN p.start_time AND p.end_time` ensures the ad occurred during that session.

SQL `BETWEEN` is inclusive at both ends. This exactly matches the stated inclusive session interval, so an ad at `start_time` or `end_time` disqualifies the session.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Playback": [{"session_id": 1, "customer_id": 1, "start_time": 1, "end_time": 5}, {"session_id": 2, "customer_id": 1, "start_time": 15, "end_time": 23}, {"session_id": 3, "customer_id": 2, "start_time": 10, "end_time": 12}, {"session_id": 4, "customer_id": 2, "start_time": 17, "end_time": 28}, {"session_id": 5, "customer_id": 2, "start_time": 2, "end_time": 8}], "Ads": [{"ad_id": 1, "customer_id": 1, "timestamp": 5}, {"ad_id": 2, "customer_id": 2, "timestamp": 15}, {"ad_id": 3, "customer_id": 2, "timestamp": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Exclude every matched session from Playback

The outer query scans `Playback` and retains rows whose `session_id` is `NOT IN` the subquery result.

If a session has one or more matching ads, its ID appears in the subquery and the outer predicate rejects it. If no matching ad exists, its ID is absent and the outer predicate accepts it.

The subquery may return the same session ID several times when multiple ads were shown during one session. `NOT IN` membership is unaffected by duplicates, so no `DISTINCT` is required for correctness.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why customer equality cannot be omitted

Timestamps alone are not enough. Two customers may have sessions covering the same time. An ad shown to one customer must not disqualify another customer's session. The join's customer condition prevents this cross-customer contamination.

The guarantee that one customer's sessions do not intersect also means one ad timestamp can belong to at most one session for that customer. That helps bound the number of actual matches, although the database execution plan still determines how efficiently they are found.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["session_id"], "rows": [[2], [3], [5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Playback": [{"session_id": 1, "customer_id": 1, "start_time": 1, "end_time": 5}, {"session_id": 2, "customer_id": 1, "start_time": 15, "end_time": 23}, {"session_id": 3, "customer_id": 2, "start_time": 10, "end_time": 12}, {"session_id": 4, "customer_id": 2, "start_time": 17, "end_time": 28}, {"session_id": 5, "customer_id": 2, "start_time": 2, "end_time": 8}], "Ads": [{"ad_id": 1, "customer_id": 1, "timestamp": 5}, {"ad_id": 2, "customer_id": 2, "timestamp": 15}, {"ad_id": 3, "customer_id": 2, "timestamp": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["session_id"], "rows": [[2], [3], [5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((P + A)\log(A + 1))$. Let $P$ be the number of playback sessions, $A$ the number of ads, and $M$ the number of qualifying session-ad matches. SQL is declarative, so physical complexity depends on indexes and the optimizer.
- **Auxiliary Space Complexity:** $O(P + A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
