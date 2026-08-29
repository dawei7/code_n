# Guided Example: First and Last Call On the Same Day

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 17:46:07"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 19:57:13"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 05:28:44"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 04:04:15"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 22:22:22"}]}}`
- **Required output:** `{"columns": ["user_id"], "rows": [[1], [4], [5], [8]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Calls`

The objective is to compute `{"columns": ["user_id"], "rows": [[1], [4], [5], [8]]}` from `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 17:46:07"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 19:57:13"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 05:28:44"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 04:04:15"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 22:22:22"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn every call into each participant's point of view

The table stores a call asymmetrically: one user appears in `caller_id` and the other appears in `recipient_id`. The question is symmetric, however. A user's call counts whether that user placed or received it. Trying to analyze only the original `caller_id` column would therefore miss every received call.

The first common table expression, `s`, normalizes this mismatch. Its first query keeps each original row as

`(caller_id, recipient_id, call_time)`.

Its second query reverses the two participant columns and keeps the same time:

`(recipient_id, caller_id, call_time)`.

Because the columns inherit the names from the first query, every row of `s` can now be read uniformly: `caller_id` is the user being analyzed, while `recipient_id` is the other person in that call. One physical call normally contributes two logical rows, one for each participant.

The query deliberately uses `UNION ALL`. It does not need the database to spend work removing duplicates, because the two perspectives are meaningful records for the later per-user analysis. If self-calls are possible, the two perspectives are identical, but their duplication still does not change the first or last partner.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 17:46:07"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 19:57:13"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 05:28:44"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 04:04:15"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 22:22:22"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Separate one user's days

First and last are not global properties of a user. They must be recomputed for every calendar day. Both window expressions therefore partition by two keys:

- `caller_id`, which now means the user whose perspective this row represents;
- `DATE_FORMAT(call_time, '%Y-%m-%d')`, which discards the clock portion and retains the day.

All calls made or received by the same user on the same date belong to one window partition. Calls by another user, or calls by the same user on another date, cannot affect that partition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find both boundary partners with window functions

Within each user-day partition, the first `FIRST_VALUE(recipient_id)` orders rows by `call_time ASC`. The first row in that ordering is the earliest call, so the expression writes that earliest partner into the `first` column of every row in the partition.

The second expression uses the same partition but orders by `call_time DESC`. The first row of the reversed order is the chronologically latest call, so this value becomes `last`.

This is an important window-function idea: the query does not collapse the partition into one row as `GROUP BY` would. It annotates each existing logical call row with the two boundary answers for its user and day. Consequently, every row in one user-day partition receives the same relevant `first` and `last` values.

For example, suppose user 8 has calls on one day with user 4 at 09:00, user 3 at 12:00, and user 4 at 18:00. Ascending order selects 4, and descending order also selects 4. All three annotated rows therefore satisfy `first = last`. The middle call is irrelevant to the required condition; it is allowed to involve anyone.

If a user has exactly one call on a day, that same row is simultaneously earliest and latest. Its partner is therefore equal in both columns, which correctly qualifies the user for that day.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id"], "rows": [[1], [4], [5], [8]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 17:46:07"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 19:57:13"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 05:28:44"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 04:04:15"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 22:22:22"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id"], "rows": [[1], [4], [5], [8]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation after ranking:** Rank earliest and latest rows and group by user and day, then compare conditional partner values. This is explicit but usually longer than two `FIRST_VALUE` annotations.
- **Join minimum and maximum times back to `Calls`:** It can work, but it needs both participant perspectives and careful joins; time ties can multiply rows.
- **`DENSE_RANK` plus grouping:** Keep rows ranked first in ascending or descending order, then require one distinct partner. This treats tied boundary times differently and can express a deliberate all-ties interpretation.
- **Analyze callers only:** This is incorrect because calls received by a user are part of that user's daily history.
- **One call in a day:** Its partner is both first and last, so the user qualifies.
- **Middle calls with other people:** They do not matter when the earliest and latest partners match.
- **Qualifying on only one of many days:** The user is included because the condition is existential.
- **Repeated qualifying rows:** `DISTINCT` ensures each user appears only once.
- **Calendar-day boundary:** Partitioning by the formatted date prevents a late call on one date from mixing with an early call on the next date.
- **Equal timestamps:** Without a secondary ordering key, different partners tied at a boundary make `FIRST_VALUE` nondeterministic; the exact source assumes an unambiguous boundary.
- **Self-call:** `UNION ALL` may create two identical perspective rows, but both name the same partner and do not change the equality result.
- **Result order:** No `ORDER BY` is needed because the contract allows any order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `Calls`. The normalized CTE has up to $2R$ rows. Producing it is linear, while the two window orderings may sort rows within user-day partitions. Across the data, the usual upper bound is $O(R\log R)$ time. The final filter and duplicate removal add linear work or hashing/sorting that remains within that bound.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
