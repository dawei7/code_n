# Guided Example: Number of Accounts That Did Not Stream

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Subscriptions": [{"account_id": 9, "start_date": "2020-02-18", "end_date": "2021-10-30"}, {"account_id": 3, "start_date": "2021-09-21", "end_date": "2021-11-13"}, {"account_id": 11, "start_date": "2020-02-28", "end_date": "2020-08-18"}, {"account_id": 13, "start_date": "2021-04-20", "end_date": "2021-09-22"}, {"account_id": 4, "start_date": "2020-10-26", "end_date": "2021-05-08"}, {"account_id": 5, "start_date": "2020-09-11", "end_date": "2021-01-17"}], "Streams": [{"session_id": 14, "account_id": 9, "stream_date": "2020-05-16"}, {"session_id": 16, "account_id": 3, "stream_date": "2021-10-27"}, {"session_id": 18, "account_id": 11, "stream_date": "2020-04-29"}, {"session_id": 17, "account_id": 13, "stream_date": "2021-08-08"}, {"session_id": 19, "account_id": 4, "stream_date": "2020-12-31"}, {"session_id": 13, "account_id": 5, "stream_date": "2021-01-05"}]}}`
- **Required output:** `{"columns": ["accounts_count"], "rows": [[2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Subscriptions`

The objective is to compute `{"columns": ["accounts_count"], "rows": [[2]]}` from `{"tables": {"Subscriptions": [{"account_id": 9, "start_date": "2020-02-18", "end_date": "2021-10-30"}, {"account_id": 3, "start_date": "2021-09-21", "end_date": "2021-11-13"}, {"account_id": 11, "start_date": "2020-02-28", "end_date": "2020-08-18"}, {"account_id": 13, "start_date": "2021-04-20", "end_date": "2021-09-22"}, {"account_id": 4, "start_date": "2020-10-26", "end_date": "2021-05-08"}, {"account_id": 5, "start_date": "2020-09-11", "end_date": "2021-01-17"}], "Streams": [{"session_id": 14, "account_id": 9, "stream_date": "2020-05-16"}, {"session_id": 16, "account_id": 3, "stream_date": "2021-10-27"}, {"session_id": 18, "account_id": 11, "stream_date": "2020-04-29"}, {"session_id": 17, "account_id": 13, "stream_date": "2021-08-08"}, {"session_id": 19, "account_id": 4, "stream_date": "2020-12-31"}, {"session_id": 13, "account_id": 5, "stream_date": "2021-01-05"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify subscriptions overlapping 2021

An account bought/held a subscription in 2021 when its subscription interval overlaps that calendar year. The source tests

`YEAR(start_date) <= 2021`

and

`YEAR(end_date) >= 2021`.

Together these keep subscriptions starting no later than 2021 and ending no earlier than 2021. Under date granularity, that expresses overlap with some part of the year.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Subscriptions": [{"account_id": 9, "start_date": "2020-02-18", "end_date": "2021-10-30"}, {"account_id": 3, "start_date": "2021-09-21", "end_date": "2021-11-13"}, {"account_id": 11, "start_date": "2020-02-28", "end_date": "2020-08-18"}, {"account_id": 13, "start_date": "2021-04-20", "end_date": "2021-09-22"}, {"account_id": 4, "start_date": "2020-10-26", "end_date": "2021-05-08"}, {"account_id": 5, "start_date": "2020-09-11", "end_date": "2021-01-17"}], "Streams": [{"session_id": 14, "account_id": 9, "stream_date": "2020-05-16"}, {"session_id": 16, "account_id": 3, "stream_date": "2021-10-27"}, {"session_id": 18, "account_id": 11, "stream_date": "2020-04-29"}, {"session_id": 17, "account_id": 13, "stream_date": "2021-08-08"}, {"session_id": 19, "account_id": 4, "stream_date": "2020-12-31"}, {"session_id": 13, "account_id": 5, "stream_date": "2021-01-05"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the left join produces

`Subscriptions AS sub LEFT JOIN Streams USING (account_id)` joins every subscription with all of that account's stream sessions.

If an account has several sessions, it produces several rows. If it has no sessions at all, the subscription is retained once with null stream columns.

A correct anti-join solution would use this null-extended row to identify accounts with no relevant stream.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the exact source actually filters

The final stream predicate is

`YEAR(stream_date) != 2021 OR stream_date > end_date`.

This keeps an individual joined session row when its year is not 2021 or when it occurs after the subscription ended. It does not prove that the account had no 2021 session.

The query then applies `COUNT(sub.account_id)` to surviving joined rows. It counts session rows, not distinct subscription accounts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["accounts_count"], "rows": [[2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Subscriptions": [{"account_id": 9, "start_date": "2020-02-18", "end_date": "2021-10-30"}, {"account_id": 3, "start_date": "2021-09-21", "end_date": "2021-11-13"}, {"account_id": 11, "start_date": "2020-02-28", "end_date": "2020-08-18"}, {"account_id": 13, "start_date": "2021-04-20", "end_date": "2021-09-22"}, {"account_id": 4, "start_date": "2020-10-26", "end_date": "2021-05-08"}, {"account_id": 5, "start_date": "2020-09-11", "end_date": "2021-01-17"}], "Streams": [{"session_id": 14, "account_id": 9, "stream_date": "2020-05-16"}, {"session_id": 16, "account_id": 3, "stream_date": "2021-10-27"}, {"session_id": 18, "account_id": 11, "stream_date": "2020-04-29"}, {"session_id": 17, "account_id": 13, "stream_date": "2021-08-08"}, {"session_id": 19, "account_id": 4, "stream_date": "2020-12-31"}, {"session_id": 13, "account_id": 5, "stream_date": "2021-01-05"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["accounts_count"], "rows": [[2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`NOT EXISTS`:** For each overlapping subscription, reject it when any stream row has year 2021; this directly expresses absence.
- **Conditional left anti-join:** Put the 2021 condition in `ON` and require the joined key to be null.
- **`NOT IN`:** Can work with a nonnull account subquery, but null semantics make `NOT EXISTS` safer.
- **No streams at all:** Should qualify if the subscription overlaps 2021; the exact query incorrectly drops it.
- **Both 2020 and 2021 streams:** Should not qualify; the exact query can count the 2020 row.
- **Several old streams:** One account should count once; the exact query can count several rows.
- **Only a 2021 stream:** Correctly should be excluded.
- **Subscription spanning the full year:** Meets both overlap conditions.
- **Subscription ending in 2020:** Does not overlap 2021.
- **SQL null logic:** Comparisons with null are unknown, not true.
- **Counting unit:** The requested result counts accounts, not sessions.
- **Exact-source status:** Its filter is not a valid absence test.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Let $S$ be subscriptions and $T$ stream rows. With hashing/indexing, a properly formulated anti-join can run in expected $O(S+T)$ time and use $O(T)$ lookup space, matching the manifest.
- **Auxiliary Space Complexity:** $O(T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
