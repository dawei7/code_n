# Guided Example: Confirmation Rate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Signups": [{"user_id": 3, "time_stamp": "2020-03-21 10:16:13"}, {"user_id": 7, "time_stamp": "2020-01-04 13:57:59"}, {"user_id": 2, "time_stamp": "2020-07-29 23:09:44"}, {"user_id": 6, "time_stamp": "2020-12-09 10:39:37"}], "Confirmations": [{"user_id": 3, "time_stamp": "2021-01-06 03:30:46", "action": "timeout"}, {"user_id": 3, "time_stamp": "2021-07-14 14:00:00", "action": "timeout"}, {"user_id": 7, "time_stamp": "2021-06-12 11:57:29", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-13 12:58:28", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-14 13:59:27", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-01-22 00:00:00", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-02-28 23:59:59", "action": "timeout"}]}}`
- **Required output:** `{"columns": ["user_id", "confirmation_rate"], "rows": [[3, 0.0], [7, 1.0], [2, 0.5], [6, 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Signups`

The objective is to compute `{"columns": ["user_id", "confirmation_rate"], "rows": [[3, 0.0], [7, 1.0], [2, 0.5], [6, 0.0]]}` from `{"tables": {"Signups": [{"user_id": 3, "time_stamp": "2020-03-21 10:16:13"}, {"user_id": 7, "time_stamp": "2020-01-04 13:57:59"}, {"user_id": 2, "time_stamp": "2020-07-29 23:09:44"}, {"user_id": 6, "time_stamp": "2020-12-09 10:39:37"}], "Confirmations": [{"user_id": 3, "time_stamp": "2021-01-06 03:30:46", "action": "timeout"}, {"user_id": 3, "time_stamp": "2021-07-14 14:00:00", "action": "timeout"}, {"user_id": 7, "time_stamp": "2021-06-12 11:57:29", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-13 12:58:28", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-14 13:59:27", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-01-22 00:00:00", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-02-28 23:59:59", "action": "timeout"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from every signed-up user

The result must contain each user in `Signups`, including users who never requested confirmation. Therefore `SignUps` is the left side of a `LEFT JOIN` with `Confirmations`. The `USING (user_id)` clause matches confirmation rows to the corresponding signup and exposes one shared `user_id` column.

If a user has several confirmation requests, the join produces one row for each request. If a user has none, a left join still produces one placeholder row for that signup, with the confirmation-side columns set to `NULL`. Preserving that placeholder is what lets the query report a zero rate instead of losing the user.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Signups": [{"user_id": 3, "time_stamp": "2020-03-21 10:16:13"}, {"user_id": 7, "time_stamp": "2020-01-04 13:57:59"}, {"user_id": 2, "time_stamp": "2020-07-29 23:09:44"}, {"user_id": 6, "time_stamp": "2020-12-09 10:39:37"}], "Confirmations": [{"user_id": 3, "time_stamp": "2021-01-06 03:30:46", "action": "timeout"}, {"user_id": 3, "time_stamp": "2021-07-14 14:00:00", "action": "timeout"}, {"user_id": 7, "time_stamp": "2021-06-12 11:57:29", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-13 12:58:28", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-14 13:59:27", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-01-22 00:00:00", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-02-28 23:59:59", "action": "timeout"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn the action condition into a numeric count

In MySQL, the expression `action = 'confirmed'` evaluates to `1` when true and `0` when false. Summing it within a user group counts confirmed messages:

`SUM(action = 'confirmed')`.

For a user with actual confirmation rows, `COUNT(1)` counts every joined row, so it is the total number of requested messages. Dividing the Boolean sum by this count produces

$$
\frac{\text{confirmed requests}}{\text{all requests}}.
$$

For example, actions `confirmed`, `timeout`, and `confirmed` contribute $1+0+1=2$ to the numerator and three to the denominator.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle users with no requests

The no-confirmation case deserves careful attention. The left join supplies one placeholder row. Its `action` is `NULL`, so `action = 'confirmed'` is also `NULL`. `SUM` over that expression returns `NULL`. Meanwhile, `COUNT(1)` counts the placeholder row and returns one.

The division therefore remains `NULL`, and `COALESCE(..., 0)` replaces it with zero. This yields the required rate. The placeholder is not accidentally treated as a timeout contributing a meaningful request: its null numerator propagates until `COALESCE` applies the specified default.

An alternative expression such as `COUNT(action)` would return zero for the placeholder and would require explicit protection against division by zero. The exact query's null propagation plus `COALESCE` is concise and correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "confirmation_rate"], "rows": [[3, 0.0], [7, 1.0], [2, 0.5], [6, 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Signups": [{"user_id": 3, "time_stamp": "2020-03-21 10:16:13"}, {"user_id": 7, "time_stamp": "2020-01-04 13:57:59"}, {"user_id": 2, "time_stamp": "2020-07-29 23:09:44"}, {"user_id": 6, "time_stamp": "2020-12-09 10:39:37"}], "Confirmations": [{"user_id": 3, "time_stamp": "2021-01-06 03:30:46", "action": "timeout"}, {"user_id": 3, "time_stamp": "2021-07-14 14:00:00", "action": "timeout"}, {"user_id": 7, "time_stamp": "2021-06-12 11:57:29", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-13 12:58:28", "action": "confirmed"}, {"user_id": 7, "time_stamp": "2021-06-14 13:59:27", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-01-22 00:00:00", "action": "confirmed"}, {"user_id": 2, "time_stamp": "2021-02-28 23:59:59", "action": "timeout"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "confirmation_rate"], "rows": [[3, 0.0], [7, 1.0], [2, 0.5], [6, 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional average:** In MySQL, `AVG(action = 'confirmed')` directly averages ones and zeroes for users with requests. It still needs `COALESCE` for users whose only joined action is null.
- **Conditional count:** `SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END)` is more portable across SQL systems that do not coerce Boolean expressions to numbers.
- **Inner join:** This is wrong because users with no confirmation requests would disappear instead of receiving rate zero.
- **Count of `action`:** It excludes the null placeholder and accurately counts real actions, but the zero-request case then needs `NULLIF` or a separate branch to avoid dividing by zero.
- **No requests:** The left-join placeholder produces a null aggregate expression, and `COALESCE` returns `0.00` after rounding.
- **All timeouts:** The Boolean sum is zero and the positive request count gives rate zero.
- **All confirmed:** The numerator equals the denominator and the rate is one.
- **Mixed actions:** Each confirmation row contributes exactly one to the denominator and either zero or one to the numerator.
- **Rounding:** `ROUND` is applied to the quotient with two requested decimal places; result display formatting can still be client-dependent, but its numeric value is rounded.
- **Duplicate signup users:** The schema says `user_id` is unique, so grouping cannot merge distinct signup records for one identifier.
- **Result order:** No ordering clause is needed because any order is accepted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+C)$. Let $S$ be the number of `Signups` rows and $C$ the number of `Confirmations` rows.
- **Auxiliary Space Complexity:** $O(S+C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
