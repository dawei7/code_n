# Guided Example: Snaps Analysis

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activities": [{"activity_id": 7274, "user_id": 123, "activity_type": "open", "time_spent": 4.5}, {"activity_id": 2425, "user_id": 123, "activity_type": "send", "time_spent": 3.5}, {"activity_id": 1413, "user_id": 456, "activity_type": "send", "time_spent": 5.67}, {"activity_id": 2536, "user_id": 456, "activity_type": "open", "time_spent": 3.0}, {"activity_id": 8564, "user_id": 456, "activity_type": "send", "time_spent": 8.24}, {"activity_id": 5235, "user_id": 789, "activity_type": "send", "time_spent": 6.24}, {"activity_id": 4251, "user_id": 123, "activity_type": "open", "time_spent": 1.25}, {"activity_id": 1435, "user_id": 789, "activity_type": "open", "time_spent": 5.25}], "Age": [{"user_id": 123, "age_bucket": "31-35"}, {"user_id": 789, "age_bucket": "21-25"}, {"user_id": 456, "age_bucket": "26-30"}]}}`
- **Required output:** `{"columns": ["age_bucket", "send_perc", "open_perc"], "rows": [["31-35", 37.84, 62.16], ["26-30", 82.26, 17.74], ["21-25", 54.31, 45.69]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activities`

The objective is to compute `{"columns": ["age_bucket", "send_perc", "open_perc"], "rows": [["31-35", 37.84, 62.16], ["26-30", 82.26, 17.74], ["21-25", 54.31, 45.69]]}` from `{"tables": {"Activities": [{"activity_id": 7274, "user_id": 123, "activity_type": "open", "time_spent": 4.5}, {"activity_id": 2425, "user_id": 123, "activity_type": "send", "time_spent": 3.5}, {"activity_id": 1413, "user_id": 456, "activity_type": "send", "time_spent": 5.67}, {"activity_id": 2536, "user_id": 456, "activity_type": "open", "time_spent": 3.0}, {"activity_id": 8564, "user_id": 456, "activity_type": "send", "time_spent": 8.24}, {"activity_id": 5235, "user_id": 789, "activity_type": "send", "time_spent": 6.24}, {"activity_id": 4251, "user_id": 123, "activity_type": "open", "time_spent": 1.25}, {"activity_id": 1435, "user_id": 789, "activity_type": "open", "time_spent": 5.25}], "Age": [{"user_id": 123, "age_bucket": "31-35"}, {"user_id": 789, "age_bucket": "21-25"}, {"user_id": 456, "age_bucket": "26-30"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Attach every activity to an age bucket.** `Activities` contains time and activity type, while `Age` contains the user's bucket. `JOIN Age USING (user_id)` combines rows with the same user identifier so every included activity carries its owner's `age_bucket`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activities": [{"activity_id": 7274, "user_id": 123, "activity_type": "open", "time_spent": 4.5}, {"activity_id": 2425, "user_id": 123, "activity_type": "send", "time_spent": 3.5}, {"activity_id": 1413, "user_id": 456, "activity_type": "send", "time_spent": 5.67}, {"activity_id": 2536, "user_id": 456, "activity_type": "open", "time_spent": 3.0}, {"activity_id": 8564, "user_id": 456, "activity_type": "send", "time_spent": 8.24}, {"activity_id": 5235, "user_id": 789, "activity_type": "send", "time_spent": 6.24}, {"activity_id": 4251, "user_id": 123, "activity_type": "open", "time_spent": 1.25}, {"activity_id": 1435, "user_id": 789, "activity_type": "open", "time_spent": 5.25}], "Age": [{"user_id": 123, "age_bucket": "31-35"}, {"user_id": 789, "age_bucket": "21-25"}, {"user_id": 456, "age_bucket": "26-30"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This is an inner join. An activity whose user has no `Age` row is excluded, and an age bucket with no joined activity produces no result row. Under the expected foreign-key-like data relationship, every relevant activity has exactly one matching age row because `Age.user_id` is unique.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Group all activity time by age bucket.** `GROUP BY 1` groups on the first selected expression, `age_bucket`. Each group therefore represents all send and open activity from all users in that age category, not an average of per-user percentages.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["age_bucket", "send_perc", "open_perc"], "rows": [["31-35", 37.84, 62.16], ["26-30", 82.26, 17.74], ["21-25", 54.31, 45.69]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activities": [{"activity_id": 7274, "user_id": 123, "activity_type": "open", "time_spent": 4.5}, {"activity_id": 2425, "user_id": 123, "activity_type": "send", "time_spent": 3.5}, {"activity_id": 1413, "user_id": 456, "activity_type": "send", "time_spent": 5.67}, {"activity_id": 2536, "user_id": 456, "activity_type": "open", "time_spent": 3.0}, {"activity_id": 8564, "user_id": 456, "activity_type": "send", "time_spent": 8.24}, {"activity_id": 5235, "user_id": 789, "activity_type": "send", "time_spent": 6.24}, {"activity_id": 4251, "user_id": 123, "activity_type": "open", "time_spent": 1.25}, {"activity_id": 1435, "user_id": 789, "activity_type": "open", "time_spent": 5.25}], "Age": [{"user_id": 123, "age_bucket": "31-35"}, {"user_id": 789, "age_bucket": "21-25"}, {"user_id": 456, "age_bucket": "26-30"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["age_bucket", "send_perc", "open_perc"], "rows": [["31-35", 37.84, 62.16], ["26-30", 82.26, 17.74], ["21-25", 54.31, 45.69]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate each activity type separately:** Two grouped subqueries plus a join can produce the same columns but repeat scans and require careful handling of buckets missing one type.
- **Average per-user percentages:** This is generally wrong because it weights users equally rather than weighting every duration in the bucket.
- **Use `CASE` instead of `IF`:** `SUM(CASE WHEN ... THEN time_spent ELSE 0 END)` is standard SQL and has the same logic.
- **Bucket has only sends:** Send percentage is 100.00 and open percentage is 0.00, provided total time is positive.
- **Bucket has only opens:** The symmetric result is 0.00 and 100.00.
- **Zero total time:** The exact expressions return null through division by zero; the source does not define a replacement.
- **Missing age row:** The inner join removes that user's activities.
- **Age row without activity:** It creates no group and therefore no output row.
- **Rounding order:** Totals are divided first and the final percentage is rounded, avoiding accumulated rounding error from per-row percentages.
- **Any result order:** Group order is unspecified, which is allowed by the contract.
- **Percentage type behavior:** Multiplying by 100 before division makes the intended scale obvious. Because `time_spent` is decimal, MySQL performs decimal-style division rather than accidental integer truncation.
- **Shared denominator:** Both output percentages divide by the same total activity time for the age bucket, so under the declared send/open activity domain their unrounded values sum to 100 percent.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $A$ be the number of activity rows and $G$ the number of age buckets. With an indexed unique lookup on `Age.user_id`, joining and aggregating is logically $O(A)$ expected work, and the engine keeps $O(G)$ group state.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
