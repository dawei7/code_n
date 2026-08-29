# Guided Example: Viewers Turned Streamers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sessions": [{"user_id": 101, "session_start": "2023-11-06 13:53:42", "session_end": "2023-11-06 14:05:42", "session_id": 375, "session_type": "Viewer"}, {"user_id": 101, "session_start": "2023-11-22 16:45:21", "session_end": "2023-11-22 20:39:21", "session_id": 594, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-16 13:23:09", "session_end": "2023-11-16 16:10:09", "session_id": 777, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-17 13:23:09", "session_end": "2023-11-17 16:10:09", "session_id": 778, "session_type": "Streamer"}, {"user_id": 101, "session_start": "2023-11-20 07:16:06", "session_end": "2023-11-20 08:33:06", "session_id": 315, "session_type": "Streamer"}, {"user_id": 104, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 797, "session_type": "Viewer"}, {"user_id": 103, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 798, "session_type": "Streamer"}]}}`
- **Required output:** `{"columns": ["user_id", "sessions_count"], "rows": [[101, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sessions`

The objective is to compute `{"columns": ["user_id", "sessions_count"], "rows": [[101, 2]]}` from `{"tables": {"Sessions": [{"user_id": 101, "session_start": "2023-11-06 13:53:42", "session_end": "2023-11-06 14:05:42", "session_id": 375, "session_type": "Viewer"}, {"user_id": 101, "session_start": "2023-11-22 16:45:21", "session_end": "2023-11-22 20:39:21", "session_id": 594, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-16 13:23:09", "session_end": "2023-11-16 16:10:09", "session_id": 777, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-17 13:23:09", "session_end": "2023-11-17 16:10:09", "session_id": 778, "session_type": "Streamer"}, {"user_id": 101, "session_start": "2023-11-20 07:16:06", "session_end": "2023-11-20 08:33:06", "session_id": 315, "session_type": "Streamer"}, {"user_id": 104, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 797, "session_type": "Viewer"}, {"user_id": 103, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 798, "session_type": "Streamer"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate first-session classification from streamer counting

The intended task has two parts for each user:

1. determine whether the earliest session was a Viewer session;
2. if so, count that user’s Streamer sessions.

CTE `T` selects `user_id` and `session_type` and assigns:

`RANK() OVER (PARTITION BY user_id ORDER BY session_start) AS rk`.

The final query joins rank information back to raw `Sessions` by `user_id`. It keeps CTE rows where `rk = 1` and `t.session_type = 'Viewer'`, while the raw joined row must satisfy `s.session_type = 'Streamer'`. `COUNT(1)` then counts those joined streamer rows per user.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sessions": [{"user_id": 101, "session_start": "2023-11-06 13:53:42", "session_end": "2023-11-06 14:05:42", "session_id": 375, "session_type": "Viewer"}, {"user_id": 101, "session_start": "2023-11-22 16:45:21", "session_end": "2023-11-22 20:39:21", "session_id": 594, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-16 13:23:09", "session_end": "2023-11-16 16:10:09", "session_id": 777, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-17 13:23:09", "session_end": "2023-11-17 16:10:09", "session_id": 778, "session_type": "Streamer"}, {"user_id": 101, "session_start": "2023-11-20 07:16:06", "session_end": "2023-11-20 08:33:06", "session_id": 315, "session_type": "Streamer"}, {"user_id": 104, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 797, "session_type": "Viewer"}, {"user_id": 103, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 798, "session_type": "Streamer"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the query behaves when the earliest timestamp is unique

Assume each user has one unique earliest `session_start`. Then `T` contains exactly one rank-one row for that user. If it is a Viewer, joining it to `Sessions` exposes every session for the same user, and the raw-side filter retains exactly the Streamer sessions. Each streamer row joins once to the single qualifying rank-one row, so `COUNT(1)` is the correct count.

If the unique earliest row is a Streamer, the CTE-side Viewer condition fails and the user disappears. If it is a Viewer but the user never streams, no raw joined row passes the Streamer condition, so the user also disappears, matching the sample’s treatment of user 104.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the output order is correct

The query groups by `user_id`, producing one result per surviving user. It names the count `sessions_count`.

`ORDER BY 2 DESC, 1 DESC` sorts first by the second selected column, the streaming count, greatest first. Ties are broken by `user_id` descending, exactly as requested.


The sole rank-one CTE row correctly classifies the first session. A qualifying viewer-first row is paired with every and only raw Streamer row for that user after filtering. One-to-one pairing makes the aggregate equal the number of streaming sessions. Grouping ensures one output row per user.

This explains the intended algorithm and why the sample works.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "sessions_count"], "rows": [[101, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sessions": [{"user_id": 101, "session_start": "2023-11-06 13:53:42", "session_end": "2023-11-06 14:05:42", "session_id": 375, "session_type": "Viewer"}, {"user_id": 101, "session_start": "2023-11-22 16:45:21", "session_end": "2023-11-22 20:39:21", "session_id": 594, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-16 13:23:09", "session_end": "2023-11-16 16:10:09", "session_id": 777, "session_type": "Streamer"}, {"user_id": 102, "session_start": "2023-11-17 13:23:09", "session_end": "2023-11-17 16:10:09", "session_id": 778, "session_type": "Streamer"}, {"user_id": 101, "session_start": "2023-11-20 07:16:06", "session_end": "2023-11-20 08:33:06", "session_id": 315, "session_type": "Streamer"}, {"user_id": 104, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 797, "session_type": "Viewer"}, {"user_id": 103, "session_start": "2023-11-27 03:10:49", "session_end": "2023-11-27 03:30:49", "session_id": 798, "session_type": "Streamer"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "sessions_count"], "rows": [[101, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` with `session_id` tie-break:** This selects one deterministic first session and prevents count multiplication.
- **Find minimum timestamp then join:** It still needs a rule when several sessions share that minimum.
- **Conditional aggregation:** After deterministic numbering, group once and require the first type Viewer while summing Streamer rows; this avoids joining rank rows back to facts.
- **Unique earliest Viewer, no streamers:** The exact inner join/filter yields no output row, as required.
- **Unique earliest Streamer:** The user is excluded even if later Viewer sessions exist.
- **Several later streamers:** Each is counted once under the unique-earliest assumption.
- **Tied earliest sessions:** The exact source is ambiguous and can overcount because the schema does not forbid ties.
- **Count ordering:** Greater `sessions_count` comes first, then greater `user_id`.
- **Manifest complexity:** $O(R\log R)$ is conditional on one rank-one classifier row; exact worst-case joined cardinality is quadratic.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(J)$. With one unique earliest row per user, ranking requires a general $O(R\log R)$ sort, and joining/filtering/grouping can be $O(R)$ expected plus final output sorting. Space is $O(R)$ for the windowed relation and execution buffers.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
